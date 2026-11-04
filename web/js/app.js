/**
 * Application Controller for Chinese Vocal HSK Visualizer & Anki Flashcard System.
 * Coordinates SRS review loops, intra-session lapse re-queueing, keyboard shortcuts, and UI drawers.
 */

const App = (function() {
  let chapters = [];
  let currentChapter = null;
  let WORDS = [];
  let filteredWords = [];
  
  // Flashcard review queue & state
  let reviewQueue = []; // array of word IDs
  let queueIndex = 0;
  let currentCardSide = 'front'; // 'front' | 'back'
  let currentActiveTab = 'sentences';
  let studyMode = 'flashcard'; // 'flashcard' | 'browse'
  let reviewFilter = 'all'; // 'all' | 'due' | 'lapses' | 'remembered' | 'new'
  let currentPosFilter = 'ALL';
  let currentLang = 'both';

  // Current active word object
  function getCurrentWord() {
    if (studyMode === 'flashcard') {
      const wordId = reviewQueue[queueIndex];
      return WORDS.find(w => String(w.id) === String(wordId)) || WORDS[0] || null;
    } else {
      return WORDS[queueIndex] || WORDS[0] || null;
    }
  }

  // Initialize Theme
  function initTheme() {
    const savedTheme = localStorage.getItem('hsk_theme') || 'dark';
    document.body.setAttribute('data-theme', savedTheme);
  }

  // Build the review queue based on active review filter
  function buildReviewQueue() {
    if (!currentChapter) return;
    const reviews = StorageManager.getChapterReviews(currentChapter.dir);

    let candidates = [...WORDS];

    // Filter by POS if selected
    if (currentPosFilter !== 'ALL') {
      const posFilterLower = currentPosFilter.toLowerCase();
      candidates = candidates.filter(w => (w.part_of_speech || '').toLowerCase().includes(posFilterLower));
    }

    // Filter by Review Status
    if (reviewFilter === 'due') {
      candidates = candidates.filter(w => StorageManager.isDue(reviews[String(w.id)]));
    } else if (reviewFilter === 'lapses') {
      candidates = candidates.filter(w => reviews[String(w.id)]?.status === 'dont_remember');
    } else if (reviewFilter === 'remembered') {
      candidates = candidates.filter(w => reviews[String(w.id)]?.status === 'remembered');
    } else if (reviewFilter === 'new') {
      candidates = candidates.filter(w => !reviews[String(w.id)]);
    }

    const settings = StorageManager.getSettings();
    if (settings.studyOrder === 'shuffle') {
      candidates.sort(() => Math.random() - 0.5);
    }

    reviewQueue = candidates.map(w => w.id);
    queueIndex = 0;
    currentCardSide = 'front';
  }

  // Update Topbar Mastery Progress Bar & Stats
  function updateMasteryStats() {
    if (!currentChapter) return;
    const stats = StorageManager.getChapterStats(currentChapter.dir, WORDS);

    const countEl = document.getElementById('mastery-text');
    const barEl = document.getElementById('mastery-bar-fill');
    if (countEl) {
      countEl.textContent = `${stats.remembered}/${stats.total} (${stats.percent}%)`;
    }
    if (barEl) {
      barEl.style.width = `${stats.percent}%`;
    }

    // Update Counter
    const counterEl = document.getElementById('word-counter');
    if (counterEl) {
      if (studyMode === 'flashcard') {
        const totalInQueue = reviewQueue.length;
        const currentPos = totalInQueue > 0 ? queueIndex + 1 : 0;
        counterEl.textContent = `${String(currentPos).padStart(2, '0')} / ${String(totalInQueue).padStart(2, '0')}`;
      } else {
        const total = WORDS.length;
        const currentPos = queueIndex + 1;
        counterEl.textContent = `${String(currentPos).padStart(2, '0')} / ${String(total).padStart(2, '0')}`;
      }
    }
  }

  // Render the current view
  function renderCurrentWord() {
    const container = document.getElementById('detail-container');
    if (!container) return;

    if (studyMode === 'flashcard') {
      if (reviewQueue.length === 0 || queueIndex >= reviewQueue.length) {
        const stats = StorageManager.getChapterStats(currentChapter.dir, WORDS);
        renderCompletionScreen(stats);
        return;
      }

      const w = getCurrentWord();
      if (!w) return;

      const reviewItem = StorageManager.getWordReview(currentChapter.dir, w.id);

      if (currentCardSide === 'front') {
        container.innerHTML = renderFlashcardFront(w, currentChapter.dir, reviewItem);
      } else {
        container.innerHTML = renderFlashcardBack(w, currentChapter.dir, reviewItem, currentLang, currentActiveTab);
      }

      renderActionBar(currentCardSide, studyMode);
    } else {
      // Browse Mode
      const w = getCurrentWord();
      renderBrowseView(w, currentLang);
      renderActionBar('front', 'browse');
    }

    const reviews = StorageManager.getChapterReviews(currentChapter.dir);
    const activeWord = getCurrentWord();
    renderSidebar(filteredWords, WORDS, activeWord?.id, currentLang, selectWordById, reviews);
    updateMasteryStats();

    const scrollContainer = document.getElementById('main-scroll');
    if (scrollContainer) {
      scrollContainer.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  // Select word by ID
  function selectWordById(id) {
    if (studyMode === 'flashcard') {
      const idx = reviewQueue.findIndex(qid => String(qid) === String(id));
      if (idx !== -1) {
        queueIndex = idx;
      } else {
        // If not in current filtered queue, temporarily insert it
        reviewQueue.splice(queueIndex, 0, id);
      }
      currentCardSide = 'front';
    } else {
      const idx = WORDS.findIndex(w => String(w.id) === String(id));
      if (idx !== -1) queueIndex = idx;
    }
    renderCurrentWord();
  }

  // Show Answer action (flips card to back)
  function showAnswer() {
    if (currentCardSide === 'back') return;
    currentCardSide = 'back';
    renderCurrentWord();

    const settings = StorageManager.getSettings();
    if (settings.autoAudio) {
      const w = getCurrentWord();
      if (w) speak(w.hanzi);
    }
  }

  // Rate Card action (Remember / Don't Remember) with Intra-Session Lapse Loop
  function rateCard(status) {
    if (!currentChapter) return;
    const w = getCurrentWord();
    if (!w) return;

    // Record review in storage
    StorageManager.recordReview(currentChapter.dir, w.id, status);

    // Intra-session active recall lapse loop:
    // If the user forgot ("dont_remember"), re-insert this card into the session queue
    // so they are tested again before completing the round!
    if (status === 'dont_remember') {
      // Insert 3 cards ahead (or at queue end if fewer than 3 left)
      const reinsertIndex = Math.min(reviewQueue.length, queueIndex + 4);
      reviewQueue.splice(reinsertIndex, 0, w.id);
    }

    // Advance queue
    queueIndex++;
    currentCardSide = 'front';
    renderCurrentWord();
  }

  // Switch 8-Pill Tabs
  function switchTab(tabId) {
    currentActiveTab = tabId;
    const settings = StorageManager.getSettings();
    StorageManager.saveSettings({ activeTab: tabId });

    // Update active tab buttons
    document.querySelectorAll('.pill-btn').forEach(btn => {
      const isTarget = btn.getAttribute('onclick')?.includes(`'${tabId}'`);
      btn.classList.toggle('active', isTarget);
    });

    // Update tab panels
    document.querySelectorAll('.tab-panel').forEach(panel => {
      const isTarget = panel.id === `panel-${tabId}`;
      panel.classList.toggle('active', isTarget);
    });
  }

  // Toggle Flip (Front / Back)
  function toggleFlip() {
    currentCardSide = (currentCardSide === 'front') ? 'back' : 'front';
    renderCurrentWord();
    if (currentCardSide === 'back') {
      const settings = StorageManager.getSettings();
      if (settings.autoAudio) {
        const w = getCurrentWord();
        if (w) speak(w.hanzi);
      }
    }
  }

  // Filter Sidebar & Words
  function applyFilters() {
    const searchInput = document.getElementById('search-input');
    const query = searchInput ? searchInput.value.trim().toLowerCase() : '';

    filteredWords = WORDS.filter(w => {
      const pos = (w.part_of_speech || '').toLowerCase();
      const filter = currentPosFilter.toLowerCase();
      const matchesPos = currentPosFilter === 'ALL' || pos.includes(filter);

      const matchesQuery = !query ||
        (w.hanzi && w.hanzi.includes(query)) ||
        (w.pinyin && w.pinyin.toLowerCase().includes(query)) ||
        (w.meanings_summary?.en && w.meanings_summary.en.toLowerCase().includes(query)) ||
        (w.meanings_summary?.es && w.meanings_summary.es.toLowerCase().includes(query));

      return matchesPos && matchesQuery;
    });

    const reviews = StorageManager.getChapterReviews(currentChapter.dir);
    const activeWord = getCurrentWord();
    renderSidebar(filteredWords, WORDS, activeWord?.id, currentLang, selectWordById, reviews);
  }

  // Filter by Review Status
  function filterByReviewStatus(statusFilter) {
    reviewFilter = statusFilter;
    document.querySelectorAll('.review-chip').forEach(chip => {
      chip.classList.toggle('active', chip.getAttribute('data-status') === statusFilter);
    });
    buildReviewQueue();
    renderCurrentWord();
  }

  // Switch Chapter
  async function switchChapter(chapterDir) {
    const found = chapters.find(c => c.dir === chapterDir) || chapters[0];
    if (!found) return;

    currentChapter = found;
    const pillEl = document.getElementById('chapter-pill');
    if (pillEl) {
      pillEl.textContent = `CHP ${found.id}`;
    }

    const selectEl = document.getElementById('chapter-select');
    if (selectEl && selectEl.value !== found.dir) {
      selectEl.value = found.dir;
    }

    try {
      WORDS = await DataLoader.loadChapter(found.dir);
    } catch (err) {
      console.error(`Failed to load chapter ${found.dir}:`, err);
      return;
    }

    filteredWords = [...WORDS];
    buildReviewQueue();
    renderCurrentWord();
  }

  // Set Study Mode (Flashcard vs Browse)
  function setStudyMode(mode) {
    studyMode = mode;
    StorageManager.saveSettings({ studyMode: mode });

    document.querySelectorAll('.mode-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-mode') === mode);
    });

    currentCardSide = 'front';
    renderCurrentWord();
  }

  // Drawers & Modals
  function openLookupDrawer() {
    const drawer = document.getElementById('ankineitor-lookup-drawer');
    const overlay = document.getElementById('drawer-overlay');
    const w = getCurrentWord();
    if (!drawer || !w) return;

    const termBadge = document.getElementById('lookup-word-badge');
    if (termBadge) termBadge.textContent = w.hanzi;

    const listEl = document.getElementById('lookup-links-list');
    if (listEl) {
      listEl.innerHTML = `
        <a class="lookup-item" href="https://dict.youdao.com/search?q=${encodeURIComponent(w.hanzi)}" target="_blank" rel="noopener">
          <div class="lookup-item-icon">🔴</div>
          <div>
            <div class="lookup-item-name">Youdao (有道词典)</div>
            <div class="lookup-item-desc">Native audio, collocations & usage frequency</div>
          </div>
          <div class="lookup-item-arrow">↗</div>
        </a>
        <a class="lookup-item" href="https://hanyu.baidu.com/s?wd=${encodeURIComponent(w.hanzi)}" target="_blank" rel="noopener">
          <div class="lookup-item-icon">🔵</div>
          <div>
            <div class="lookup-item-name">Baidu Hanyu (百度汉语)</div>
            <div class="lookup-item-desc">Stroke order animations & radical origins</div>
          </div>
          <div class="lookup-item-arrow">↗</div>
        </a>
        <a class="lookup-item" href="https://hanzicraft.com/character/${encodeURIComponent(w.hanzi)}" target="_blank" rel="noopener">
          <div class="lookup-item-icon">🧩</div>
          <div>
            <div class="lookup-item-name">HanziCraft</div>
            <div class="lookup-item-desc">Phonetic/semantic decomposition & frequency</div>
          </div>
          <div class="lookup-item-arrow">↗</div>
        </a>
        <a class="lookup-item" href="https://www.pleco.com" target="_blank" rel="noopener">
          <div class="lookup-item-icon">🐟</div>
          <div>
            <div class="lookup-item-name">Pleco Chinese Dictionary</div>
            <div class="lookup-item-desc">Standard mobile lexicographical reference</div>
          </div>
          <div class="lookup-item-arrow">↗</div>
        </a>
      `;
    }

    drawer.classList.add('active');
    if (overlay) overlay.classList.add('active');
  }

  function openSettingsDrawer() {
    const drawer = document.getElementById('ankineitor-settings-drawer');
    const overlay = document.getElementById('drawer-overlay');
    if (!drawer) return;

    const settings = StorageManager.getSettings();
    const autoAudioCheck = document.getElementById('toggle-auto-audio');
    const toneColorsCheck = document.getElementById('toggle-tone-colors');
    const speechRateRange = document.getElementById('speech-rate-range');

    if (autoAudioCheck) autoAudioCheck.checked = !!settings.autoAudio;
    if (toneColorsCheck) toneColorsCheck.checked = !!settings.toneColors;
    if (speechRateRange) speechRateRange.value = settings.speechRate || 0.9;

    drawer.classList.add('active');
    if (overlay) overlay.classList.add('active');
  }

  function closeDrawers() {
    document.querySelectorAll('.ankineitor-drawer').forEach(d => d.classList.remove('active'));
    const overlay = document.getElementById('drawer-overlay');
    if (overlay) overlay.classList.remove('active');
    const modal = document.getElementById('shortcuts-modal');
    if (modal) modal.classList.remove('active');
  }

  function toggleShortcutsModal() {
    const modal = document.getElementById('shortcuts-modal');
    if (!modal) return;
    modal.classList.toggle('active');
  }

  // Reset chapter reviews with confirmation
  function resetCurrentChapterProgress() {
    if (!currentChapter) return;
    const confirmed = window.confirm(`Are you sure you want to reset all review progress and SRS stats for ${currentChapter.name}?`);
    if (confirmed) {
      StorageManager.resetChapter(currentChapter.dir);
      buildReviewQueue();
      renderCurrentWord();
      closeDrawers();
    }
  }

  // Keyboard Shortcuts Listener
  function setupKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
      // Ignore if user is typing in search or input fields
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') {
        if (e.key === 'Escape') {
          e.target.blur();
        }
        return;
      }

      // Escape to close drawers or modals
      if (e.key === 'Escape') {
        closeDrawers();
        return;
      }

      // Help shortcuts
      if (e.key === '?' || (e.shiftKey && e.key === '/')) {
        e.preventDefault();
        toggleShortcutsModal();
        return;
      }

      // Drawer shortcuts
      if (e.key === 'l' || e.key === 'L') {
        e.preventDefault();
        openLookupDrawer();
        return;
      }
      if (e.key === 's' || e.key === 'S') {
        e.preventDefault();
        openSettingsDrawer();
        return;
      }

      // Audio replay
      if (e.key === 'r' || e.key === 'R') {
        e.preventDefault();
        const w = getCurrentWord();
        if (w) speak(w.hanzi);
        return;
      }

      // Flip card
      if (e.key === 'f' || e.key === 'F') {
        e.preventDefault();
        toggleFlip();
        return;
      }

      if (studyMode === 'flashcard') {
        // Space / Enter handling
        if (e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          if (currentCardSide === 'front') {
            showAnswer();
          } else {
            rateCard('remembered');
          }
          return;
        }

        // When Back is showing:
        // Key 1: Don't Remember
        // Key 2: Remember
        if (currentCardSide === 'back') {
          if (e.key === '1') {
            e.preventDefault();
            rateCard('dont_remember');
            return;
          }
          if (e.key === '2') {
            e.preventDefault();
            rateCard('remembered');
            return;
          }
          if (e.key === 'a' || e.key === 'A' || e.key === 'ArrowLeft') {
            e.preventDefault();
            rateCard('dont_remember');
            return;
          }
          if (e.key === 'd' || e.key === 'D' || e.key === 'ArrowRight') {
            e.preventDefault();
            rateCard('remembered');
            return;
          }

          // Hotkeys 3-8 switch pill tabs on Back card
          const tabMap = {
            '3': 'idioms',
            '4': 'decomp',
            '5': 'mnemonics',
            '6': 'traps',
            '7': 'synonyms',
            '8': 'passages'
          };
          if (tabMap[e.key]) {
            e.preventDefault();
            switchTab(tabMap[e.key]);
            return;
          }
        } else {
          // On Front: Left / Right arrow navigation
          if (e.key === 'ArrowLeft' && queueIndex > 0) {
            e.preventDefault();
            queueIndex--;
            renderCurrentWord();
            return;
          }
          if (e.key === 'ArrowRight' && queueIndex < reviewQueue.length - 1) {
            e.preventDefault();
            queueIndex++;
            renderCurrentWord();
            return;
          }
        }
      } else {
        // Browse Mode navigation
        if (e.key === 'ArrowLeft' && queueIndex > 0) {
          queueIndex--;
          renderCurrentWord();
        } else if (e.key === 'ArrowRight' && queueIndex < WORDS.length - 1) {
          queueIndex++;
          renderCurrentWord();
        }
      }
    });
  }

  // Setup Event Listeners
  function setupEventListeners() {
    setupKeyboardShortcuts();

    // Search
    const searchInput = document.getElementById('search-input');
    if (searchInput) searchInput.addEventListener('input', applyFilters);

    // POS Filters
    document.querySelectorAll('.filter-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        currentPosFilter = chip.getAttribute('data-pos');
        applyFilters();
      });
    });

    // Review Status Filter Chips
    document.querySelectorAll('.review-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        filterByReviewStatus(chip.getAttribute('data-status'));
      });
    });

    // Mode Toggle Buttons
    document.querySelectorAll('.mode-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        setStudyMode(btn.getAttribute('data-mode'));
      });
    });

    // Language Toggle
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentLang = btn.getAttribute('data-lang');
        localStorage.setItem('hsk_lang', currentLang);
        renderCurrentWord();
      });
    });

    // Prev & Next Buttons
    const prevBtn = document.getElementById('prev-btn');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (queueIndex > 0) {
          queueIndex--;
          currentCardSide = 'front';
          renderCurrentWord();
        }
      });
    }

    const nextBtn = document.getElementById('next-btn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        const max = (studyMode === 'flashcard') ? reviewQueue.length - 1 : WORDS.length - 1;
        if (queueIndex < max) {
          queueIndex++;
          currentCardSide = 'front';
          renderCurrentWord();
        }
      });
    }

    // Sidebar toggle (mobile)
    const toggleBtn = document.getElementById('toggle-sidebar-btn');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        document.getElementById('sidebar')?.classList.toggle('open');
      });
    }

    // Theme toggle
    const themeBtn = document.getElementById('theme-btn');
    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const isLight = document.body.getAttribute('data-theme') === 'light';
        const newTheme = isLight ? 'dark' : 'light';
        document.body.setAttribute('data-theme', newTheme);
        localStorage.setItem('hsk_theme', newTheme);
      });
    }

    // Chapter Select
    const chapterSelect = document.getElementById('chapter-select');
    if (chapterSelect) {
      chapterSelect.addEventListener('change', (e) => {
        switchChapter(e.target.value);
      });
    }

    // Settings Drawer Controls
    const autoAudioCheck = document.getElementById('toggle-auto-audio');
    if (autoAudioCheck) {
      autoAudioCheck.addEventListener('change', (e) => {
        StorageManager.saveSettings({ autoAudio: e.target.checked });
      });
    }

    const toneColorsCheck = document.getElementById('toggle-tone-colors');
    if (toneColorsCheck) {
      toneColorsCheck.addEventListener('change', (e) => {
        StorageManager.saveSettings({ toneColors: e.target.checked });
        document.body.classList.toggle('hide-tone-colors', !e.target.checked);
        renderCurrentWord();
      });
    }

    const speechRateRange = document.getElementById('speech-rate-range');
    if (speechRateRange) {
      speechRateRange.addEventListener('input', (e) => {
        StorageManager.saveSettings({ speechRate: parseFloat(e.target.value) });
      });
    }
  }

  // Public App Interface
  return {
    async init() {
      initTheme();
      setupEventListeners();

      const savedSettings = StorageManager.getSettings();
      studyMode = savedSettings.studyMode || 'flashcard';
      currentActiveTab = savedSettings.activeTab || 'sentences';
      currentLang = savedSettings.lang || 'both';

      if (!savedSettings.toneColors) {
        document.body.classList.add('hide-tone-colors');
      }

      // Update mode button active state
      document.querySelectorAll('.mode-btn').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-mode') === studyMode);
      });

      // Update language buttons
      document.querySelectorAll('.lang-btn').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-lang') === currentLang);
      });

      // Load manifest
      try {
        chapters = await DataLoader.loadManifest();
      } catch (err) {
        console.error("Failed to load manifest:", err);
        chapters = [{ id: 1, dir: 'chapter_01', name: 'Chapter 1', title: '细节与人际关系', word_count: 38 }];
      }

      // Populate Chapter dropdown
      const chapterSelect = document.getElementById('chapter-select');
      if (chapterSelect) {
        chapterSelect.innerHTML = '';
        chapters.forEach(c => {
          const opt = document.createElement('option');
          opt.value = c.dir;
          opt.textContent = `${c.name}: ${c.title || c.dir} (${c.word_count} words)`;
          chapterSelect.appendChild(opt);
        });
      }

      // Load initial chapter
      const urlParams = new URLSearchParams(window.location.search);
      const requestedCh = urlParams.get('ch');
      let initialDir = chapters[0]?.dir || 'chapter_01';
      if (requestedCh) {
        const match = chapters.find(c => String(c.id) === requestedCh || c.dir === requestedCh);
        if (match) initialDir = match.dir;
      }

      await switchChapter(initialDir);
    },

    showAnswer,
    rateCard,
    switchTab,
    toggleFlip,
    setStudyMode,
    filterByReviewStatus,
    restartQueue() {
      buildReviewQueue();
      renderCurrentWord();
    },
    openLookupDrawer,
    openSettingsDrawer,
    closeDrawers,
    toggleShortcutsModal,
    resetCurrentChapterProgress
  };
})();

// Attach to window for inline onclick handlers
if (typeof window !== 'undefined') {
  window.App = App;
}

// Start on DOM ready
document.addEventListener('DOMContentLoaded', () => App.init());
