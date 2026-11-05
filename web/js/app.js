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

  // Intra-session stats & Auto-advance state
  let sessionGoodCount = 0;
  let sessionAgainCount = 0;
  let autoAdvanceTimer = null;
  let autoAdvanceSecondsLeft = 5;
  let isAutoAdvancePaused = false;

  // Clear running auto-advance timer
  function clearAutoAdvanceTimer() {
    if (autoAdvanceTimer) {
      clearInterval(autoAdvanceTimer);
      autoAdvanceTimer = null;
    }
  }

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

  // Web Audio API Micro-Feedback Synthesizer
  let audioCtx = null;
  function playAudioFeedback(type) {
    try {
      const settings = StorageManager.getSettings();
      if (settings.soundFx === false) return;

      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);

      const now = audioCtx.currentTime;

      if (type === 'flip') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(420, now);
        osc.frequency.exponentialRampToValueAtTime(560, now + 0.05);
        gain.gain.setValueAtTime(0.06, now);
        gain.gain.linearRampToValueAtTime(0.001, now + 0.05);
        osc.start(now);
        osc.stop(now + 0.05);
      } else if (type === 'good') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.setValueAtTime(659.25, now + 0.06);
        gain.gain.setValueAtTime(0.07, now);
        gain.gain.linearRampToValueAtTime(0.001, now + 0.15);
        osc.start(now);
        osc.stop(now + 0.15);
      } else if (type === 'again') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(320, now);
        osc.frequency.exponentialRampToValueAtTime(220, now + 0.08);
        gain.gain.setValueAtTime(0.07, now);
        gain.gain.linearRampToValueAtTime(0.001, now + 0.08);
        osc.start(now);
        osc.stop(now + 0.08);
      } else {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(600, now);
        gain.gain.setValueAtTime(0.03, now);
        gain.gain.linearRampToValueAtTime(0.001, now + 0.03);
        osc.start(now);
        osc.stop(now + 0.03);
      }
    } catch (e) {
      // AudioContext might be blocked until user interacts
    }
  }

  // Toast Notification
  let toastTimer = null;
  function showToast(message) {
    const toastEl = document.getElementById('app-toast');
    if (!toastEl) return;
    toastEl.textContent = message;
    toastEl.classList.add('active');
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toastEl.classList.remove('active');
    }, 2200);
  }

  function copyText(text, successMsg = 'Copied!') {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        showToast(`📋 ${successMsg}`);
        playAudioFeedback('click');
      }).catch(() => {
        showToast(`Selected: ${text}`);
      });
    } else {
      showToast(`Selected: ${text}`);
    }
  }

  // Dynamic Review Status Badges
  function updateFilterCountBadges() {
    if (!currentChapter) return;
    const reviews = StorageManager.getChapterReviews(currentChapter.dir);
    
    let due = 0, lapses = 0, remembered = 0, newWords = 0;
    WORDS.forEach(w => {
      const rev = reviews[String(w.id)];
      if (!rev) {
        newWords++;
        due++;
      } else {
        if (rev.status === 'remembered') remembered++;
        if (rev.status === 'dont_remember') lapses++;
        if (StorageManager.isDue(rev)) due++;
      }
    });

    const counts = {
      all: WORDS.length,
      due: due,
      lapses: lapses,
      remembered: remembered,
      new: newWords
    };

    document.querySelectorAll('.review-chip').forEach(chip => {
      const status = chip.getAttribute('data-status');
      const existingBadge = chip.querySelector('.review-chip-count');
      const countVal = counts[status] ?? 0;
      if (existingBadge) {
        existingBadge.textContent = countVal;
      } else {
        const badge = document.createElement('span');
        badge.className = 'review-chip-count';
        badge.textContent = countVal;
        chip.appendChild(badge);
      }
    });
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

  // Update Topbar Mastery Progress Bar & Stats HUD
  function updateMasteryStats() {
    if (!currentChapter) return;
    const stats = StorageManager.getChapterStats(currentChapter.dir, WORDS);

    // Update Counter & HUD Progress Bar
    const counterEl = document.getElementById('word-counter');
    const hudFillEl = document.getElementById('hud-bar-fill');
    if (counterEl) {
      if (studyMode === 'flashcard') {
        const totalInQueue = reviewQueue.length;
        const currentPos = totalInQueue > 0 ? queueIndex + 1 : 0;
        counterEl.textContent = `${String(currentPos).padStart(2, '0')} / ${String(totalInQueue).padStart(2, '0')}`;
        if (hudFillEl) {
          const pct = totalInQueue > 0 ? Math.round((currentPos / totalInQueue) * 100) : 0;
          hudFillEl.style.width = `${pct}%`;
        }
      } else {
        const total = WORDS.length;
        const currentPos = queueIndex + 1;
        counterEl.textContent = `${String(currentPos).padStart(2, '0')} / ${String(total).padStart(2, '0')}`;
        if (hudFillEl) {
          const pct = total > 0 ? Math.round((currentPos / total) * 100) : 0;
          hudFillEl.style.width = `${pct}%`;
        }
      }
    }

    // Update Session Counters in Topbar HUD
    const goodEl = document.getElementById('session-good-count');
    const againEl = document.getElementById('session-again-count');
    if (goodEl) goodEl.textContent = sessionGoodCount;
    if (againEl) againEl.textContent = sessionAgainCount;

    // Update Chapter Badge & Title in Topbar
    const badgeEl = document.getElementById('topbar-ch-badge');
    const titleEl = document.getElementById('topbar-ch-title');
    if (badgeEl) badgeEl.textContent = `CHP ${currentChapter.id}`;
    if (titleEl) titleEl.textContent = currentChapter.title || currentChapter.name;
  }

  // Auto-Advance Countdown Controller
  function startAutoAdvanceCountdown(stats, nextChapter, totalDelay) {
    clearAutoAdvanceTimer();
    autoAdvanceSecondsLeft = totalDelay;
    isAutoAdvancePaused = false;

    autoAdvanceTimer = setInterval(() => {
      if (isAutoAdvancePaused) return;
      autoAdvanceSecondsLeft--;

      if (autoAdvanceSecondsLeft <= 0) {
        clearAutoAdvanceTimer();
        skipToNextChapter();
      } else {
        const numEl = document.getElementById('countdown-seconds-num');
        const fillEl = document.getElementById('countdown-bar-fill');
        if (numEl) numEl.textContent = autoAdvanceSecondsLeft;
        if (fillEl) {
          const pct = Math.max(0, (autoAdvanceSecondsLeft / totalDelay) * 100);
          fillEl.style.width = `${pct}%`;
        }
      }
    }, 1000);
  }

  async function skipToNextChapter() {
    clearAutoAdvanceTimer();
    const currentIdx = chapters.findIndex(c => c.dir === currentChapter.dir);
    if (currentIdx !== -1 && currentIdx + 1 < chapters.length) {
      const nextChapter = chapters[currentIdx + 1];
      sessionGoodCount = 0;
      sessionAgainCount = 0;
      await switchChapter(nextChapter.dir);
    }
  }

  function pauseAutoAdvance() {
    isAutoAdvancePaused = true;
    const stats = StorageManager.getChapterStats(currentChapter.dir, WORDS);
    const currentIdx = chapters.findIndex(c => c.dir === currentChapter.dir);
    const nextChapter = (currentIdx !== -1 && currentIdx + 1 < chapters.length) ? chapters[currentIdx + 1] : null;
    const settings = StorageManager.getSettings();
    renderCompletionScreen(stats, currentChapter, nextChapter, autoAdvanceSecondsLeft, true, true, settings.autoAdvanceDelay || 5);
  }

  function resumeAutoAdvance() {
    isAutoAdvancePaused = false;
    const stats = StorageManager.getChapterStats(currentChapter.dir, WORDS);
    const currentIdx = chapters.findIndex(c => c.dir === currentChapter.dir);
    const nextChapter = (currentIdx !== -1 && currentIdx + 1 < chapters.length) ? chapters[currentIdx + 1] : null;
    const settings = StorageManager.getSettings();
    renderCompletionScreen(stats, currentChapter, nextChapter, autoAdvanceSecondsLeft, true, false, settings.autoAdvanceDelay || 5);
  }

  async function restartFromChapter1() {
    clearAutoAdvanceTimer();
    sessionGoodCount = 0;
    sessionAgainCount = 0;
    if (chapters.length > 0) {
      await switchChapter(chapters[0].dir);
    }
  }

  // Render the current view
  function renderCurrentWord() {
    const container = document.getElementById('detail-container');
    if (!container || !currentChapter) return;

    if (studyMode === 'flashcard') {
      if (reviewQueue.length === 0 || queueIndex >= reviewQueue.length) {
        const stats = StorageManager.getChapterStats(currentChapter.dir, WORDS);
        const currentIdx = chapters.findIndex(c => c.dir === currentChapter.dir);
        const nextChapter = (currentIdx !== -1 && currentIdx + 1 < chapters.length) ? chapters[currentIdx + 1] : null;
        const settings = StorageManager.getSettings();
        const totalDelay = settings.autoAdvanceDelay || 5;

        if (nextChapter && settings.autoAdvanceChapter) {
          if (!autoAdvanceTimer && !isAutoAdvancePaused) {
            startAutoAdvanceCountdown(stats, nextChapter, totalDelay);
          }
          renderCompletionScreen(stats, currentChapter, nextChapter, autoAdvanceSecondsLeft, true, isAutoAdvancePaused, totalDelay);
        } else {
          clearAutoAdvanceTimer();
          renderCompletionScreen(stats, currentChapter, nextChapter, 0, false, false, totalDelay);
        }

        updateMasteryStats();
        return;
      }

      // We are in an active card review
      clearAutoAdvanceTimer();
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
      clearAutoAdvanceTimer();
      const w = getCurrentWord();
      renderBrowseView(w, currentLang);
      renderActionBar('front', 'browse');
    }

    const reviews = StorageManager.getChapterReviews(currentChapter.dir);
    const activeWord = getCurrentWord();
    renderSidebar(filteredWords, WORDS, activeWord?.id, currentLang, selectWordById, reviews);
    updateMasteryStats();
    updateFilterCountBadges();

    const scrollContainer = document.getElementById('main-scroll');
    if (scrollContainer && typeof scrollContainer.scrollTo === 'function') {
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
      closeWordListDrawer();
    } else {
      const idx = WORDS.findIndex(w => String(w.id) === String(id));
      if (idx !== -1) queueIndex = idx;
    }
    renderCurrentWord();
  }

  // Show Answer action (flips card to back)
  function showAnswer() {
    if (currentCardSide === 'back') return;
    playAudioFeedback('flip');
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

    if (status === 'remembered') {
      sessionGoodCount++;
      playAudioFeedback('good');
    } else {
      sessionAgainCount++;
      playAudioFeedback('again');
    }

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

  // 9-Pill Tabs Definition & Cycling
  const ALL_TABS = ['sentences', 'collocations', 'idioms', 'decomp', 'mnemonics', 'traps', 'cognates', 'contrasts', 'passages'];

  function cycleTab(direction = 1) {
    const curIdx = ALL_TABS.indexOf(currentActiveTab);
    const nextIdx = (curIdx + direction + ALL_TABS.length) % ALL_TABS.length;
    switchTab(ALL_TABS[nextIdx]);
  }

  function speakActiveTabContent(speed = 1.0) {
    const w = getCurrentWord();
    if (!w) return;

    if (currentActiveTab === 'sentences') {
      const sent = w.example_sentences?.[0];
      if (sent) speak(sent.hanzi, speed);
    } else if (currentActiveTab === 'passages') {
      const p = w.extended_reading_passages?.[0];
      if (p) speak(p.hanzi, speed);
    } else if (currentActiveTab === 'idioms') {
      const im = w.idioms?.[0];
      if (im) speak(im.hanzi, speed);
    } else if (currentActiveTab === 'collocations') {
      const c = w.collocations?.[0];
      if (c) speak(c.hanzi, speed);
    } else if (currentActiveTab === 'traps') {
      const trap = w.traps_and_cognates?.look_alikes?.[0];
      if (trap) speak(trap.character, speed);
      else speak(w.hanzi, speed);
    } else if (currentActiveTab === 'cognates') {
      const cog = w.traps_and_cognates?.etymological_cognates?.[0];
      if (cog) speak(cog.character, speed);
      else speak(w.hanzi, speed);
    } else if (currentActiveTab === 'contrasts' || currentActiveTab === 'synonyms') {
      speak(w.hanzi, speed);
    } else {
      speak(w.hanzi, speed);
    }
  }

  // Switch 9-Pill Tabs
  function switchTab(tabId) {
    if (tabId === 'synonyms') tabId = 'contrasts';
    playAudioFeedback('click');
    currentActiveTab = tabId;
    const settings = StorageManager.getSettings();
    StorageManager.saveSettings({ activeTab: tabId });

    // Update active tab buttons
    document.querySelectorAll('.pill-btn').forEach(btn => {
      const onclickAttr = btn.getAttribute('onclick') || '';
      const isTarget = onclickAttr.includes(`'${tabId}'`) || (tabId === 'contrasts' && onclickAttr.includes("'synonyms'"));
      btn.classList.toggle('active', isTarget);
    });

    // Update tab panels
    document.querySelectorAll('.tab-panel').forEach(panel => {
      const isTarget = panel.id === `panel-${tabId}` || (tabId === 'contrasts' && panel.id === 'panel-synonyms');
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
    clearAutoAdvanceTimer();
    sessionGoodCount = 0;
    sessionAgainCount = 0;
    closeWordListDrawer();

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
    currentCardSide = 'front';
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
    const autoAdvanceCheck = document.getElementById('toggle-auto-advance');
    const delayRange = document.getElementById('auto-advance-delay-range');
    const delayLabel = document.getElementById('countdown-val-label');
    const soundFxCheck = document.getElementById('toggle-sound-fx');
    const passagePinyinCheck = document.getElementById('toggle-passage-pinyin');
    const voiceSelect = document.getElementById('voice-preference-select');
    const voiceLabel = document.getElementById('voice-persona-label');

    if (autoAudioCheck) autoAudioCheck.checked = !!settings.autoAudio;
    if (toneColorsCheck) toneColorsCheck.checked = !!settings.toneColors;
    if (speechRateRange) speechRateRange.value = settings.speechRate || 0.9;
    if (autoAdvanceCheck) autoAdvanceCheck.checked = settings.autoAdvanceChapter !== false;
    if (delayRange) delayRange.value = settings.autoAdvanceDelay || 5;
    if (delayLabel) delayLabel.textContent = `${settings.autoAdvanceDelay || 5}s`;
    if (soundFxCheck) soundFxCheck.checked = settings.soundFx !== false;
    if (passagePinyinCheck) passagePinyinCheck.checked = !!settings.showPassagePinyin;
    if (voiceSelect) {
      voiceSelect.value = settings.preferredVoice || 'random';
      if (voiceLabel) {
        voiceLabel.textContent = (settings.preferredVoice === 'random' || !settings.preferredVoice)
          ? '🎲 Random'
          : (typeof AudioManager !== 'undefined' ? (AudioManager.VOICE_LABELS[settings.preferredVoice] || settings.preferredVoice) : settings.preferredVoice);
      }
    }

    drawer.classList.add('active');
    if (overlay) overlay.classList.add('active');
  }

  // Word List Off-Canvas Drawer Management
  function scrollToActiveWordInDrawer() {
    setTimeout(() => {
      const activeEl = document.querySelector('.word-item.active');
      if (activeEl) {
        activeEl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }
    }, 120);
  }

  function openWordListDrawer() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('drawer-overlay');
    if (sidebar) sidebar.classList.add('active');
    if (overlay) overlay.classList.add('active');
    scrollToActiveWordInDrawer();
  }

  function closeWordListDrawer() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar) sidebar.classList.remove('active');
    const hasOtherActive = document.querySelector('.ankineitor-drawer.active, .chapter-picker-modal-wrap.active');
    if (!hasOtherActive) {
      const overlay = document.getElementById('drawer-overlay');
      if (overlay) overlay.classList.remove('active');
    }
  }

  function toggleWordListDrawer() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar && sidebar.classList.contains('active')) {
      closeWordListDrawer();
    } else {
      openWordListDrawer();
    }
  }

  // Chapter Picker Popover Controller
  function openChapterPicker() {
    const modal = document.getElementById('chapter-picker-modal');
    const listEl = document.getElementById('chapter-picker-list');
    if (!modal || !listEl) return;

    listEl.innerHTML = '';
    chapters.forEach(c => {
      const isCurrent = currentChapter && c.dir === currentChapter.dir;
      const stats = StorageManager.getChapterStats(c.dir, c.words || []);
      const item = document.createElement('div');
      item.className = `chapter-picker-item ${isCurrent ? 'active' : ''}`;
      item.innerHTML = `
        <div class="chapter-picker-item-left">
          <span class="chapter-picker-num">CHP ${c.id}</span>
          <div class="chapter-picker-info">
            <span class="chapter-picker-name">${c.name}: ${c.title || c.dir}</span>
            <span class="chapter-picker-sub">${c.word_count || 38} words · ${c.level || 'HSK 5'}</span>
          </div>
        </div>
        <div class="chapter-picker-item-right">
          ${isCurrent ? '<span class="badge badge-pos" style="font-size: 0.72rem;">Current</span>' : ''}
          <span class="chapter-picker-progress">${stats.percent > 0 ? `${stats.percent}% Mastered` : ''}</span>
        </div>
      `;
      item.onclick = async () => {
        closeDrawers();
        await switchChapter(c.dir);
      };
      listEl.appendChild(item);
    });

    modal.classList.add('active');
    playAudioFeedback('click');
  }

  function toggleChapterPicker() {
    const modal = document.getElementById('chapter-picker-modal');
    if (modal && modal.classList.contains('active')) {
      closeDrawers();
    } else {
      openChapterPicker();
    }
  }

  // Card Step Navigation
  function prevCard() {
    playAudioFeedback('flip');
    if (studyMode === 'flashcard') {
      if (queueIndex > 0) {
        queueIndex--;
        currentCardSide = 'front';
        renderCurrentWord();
      }
    } else {
      if (queueIndex > 0) {
        queueIndex--;
        renderCurrentWord();
      }
    }
  }

  function nextCard() {
    playAudioFeedback('flip');
    if (studyMode === 'flashcard') {
      if (queueIndex < reviewQueue.length - 1) {
        queueIndex++;
        currentCardSide = 'front';
        renderCurrentWord();
      }
    } else {
      if (queueIndex < WORDS.length - 1) {
        queueIndex++;
        renderCurrentWord();
      }
    }
  }

  // Front Card Progressive Hint Toggle
  function toggleFrontHint() {
    const hintEl = document.getElementById('front-hint-content');
    if (hintEl) {
      hintEl.classList.toggle('active');
      playAudioFeedback('click');
    }
  }

  // Reading Passage Pinyin Toggle
  function togglePassagePinyin(btnEl) {
    const settings = StorageManager.getSettings();
    const nextVal = !settings.showPassagePinyin;
    StorageManager.saveSettings({ showPassagePinyin: nextVal });

    document.querySelectorAll('.passage-pinyin').forEach(el => {
      el.classList.toggle('pinyin-hidden', !nextVal);
    });
    document.querySelectorAll('.btn-toggle-pinyin').forEach(b => {
      b.classList.toggle('active', nextVal);
    });
    const check = document.getElementById('toggle-passage-pinyin');
    if (check) check.checked = nextVal;
    playAudioFeedback('click');
  }

  // Search Input Clear
  function clearSearch() {
    const input = document.getElementById('search-input');
    if (input) {
      input.value = '';
      const clearBtn = document.getElementById('search-clear-btn');
      if (clearBtn) clearBtn.classList.remove('visible');
      applyFilters();
      input.focus();
    }
  }

  function closeDrawers() {
    closeWordListDrawer();
    document.querySelectorAll('.ankineitor-drawer').forEach(d => d.classList.remove('active'));
    const overlay = document.getElementById('drawer-overlay');
    if (overlay) overlay.classList.remove('active');
    const modal = document.getElementById('shortcuts-modal');
    if (modal) modal.classList.remove('active');
    const chapterModal = document.getElementById('chapter-picker-modal');
    if (chapterModal) chapterModal.classList.remove('active');
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

      // Quick Search Focus
      if (e.key === '/') {
        e.preventDefault();
        openWordListDrawer();
        const searchInput = document.getElementById('search-input');
        if (searchInput) {
          searchInput.focus();
          searchInput.select();
        }
        return;
      }

      // Chapter Picker Popover
      if (e.key === 'c' || e.key === 'C') {
        e.preventDefault();
        toggleChapterPicker();
        return;
      }

      // Study Mode Toggle
      if (e.key === 'm' || e.key === 'M') {
        e.preventDefault();
        setStudyMode(studyMode === 'flashcard' ? 'browse' : 'flashcard');
        return;
      }

      // Language Toggle
      if (e.key === 'b' || e.key === 'B') {
        e.preventDefault();
        const nextLang = (currentLang === 'both') ? 'en' : (currentLang === 'en' ? 'es' : 'both');
        currentLang = nextLang;
        localStorage.setItem('hsk_lang', currentLang);
        document.querySelectorAll('.lang-btn').forEach(btn => {
          btn.classList.toggle('active', btn.getAttribute('data-lang') === currentLang);
        });
        showToast(`Language: ${nextLang.toUpperCase()}`);
        renderCurrentWord();
        return;
      }

      // Drawer shortcuts
      if (e.key === 'w' || e.key === 'W') {
        e.preventDefault();
        toggleWordListDrawer();
        return;
      }
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

      // Audio: Slow Pronunciation (Turtle 0.75x)
      if (e.key === 't' || e.key === 'T' || (e.shiftKey && (e.key === 'r' || e.key === 'R'))) {
        e.preventDefault();
        const w = getCurrentWord();
        if (w) speak(w.hanzi, 0.75);
        return;
      }

      // Audio: Normal Pronunciation (1.0x)
      if (e.key === 'r' || e.key === 'R') {
        e.preventDefault();
        const w = getCurrentWord();
        if (w) speak(w.hanzi, 1.0);
        return;
      }

      // Speak Active Tab Content (Sentence / Passage)
      if (e.key === 'p' || e.key === 'P') {
        // If on milestone completion screen, handle pause/resume auto-advance
        if (studyMode === 'flashcard' && (reviewQueue.length === 0 || queueIndex >= reviewQueue.length)) {
          e.preventDefault();
          if (isAutoAdvancePaused) resumeAutoAdvance();
          else pauseAutoAdvance();
          return;
        }
        e.preventDefault();
        speakActiveTabContent();
        return;
      }

      // Tab Cycling on Back card ([ and ], or Tab / Shift+Tab)
      if (currentCardSide === 'back') {
        if (e.key === '[' || e.key === ']') {
          e.preventDefault();
          cycleTab(e.key === ']' ? 1 : -1);
          return;
        }
        if (e.key === 'Tab') {
          e.preventDefault();
          cycleTab(e.shiftKey ? -1 : 1);
          return;
        }
        if (e.altKey && e.key >= '1' && e.key <= '9') {
          const tabIndex = parseInt(e.key, 10) - 1;
          if (ALL_TABS[tabIndex]) {
            e.preventDefault();
            switchTab(ALL_TABS[tabIndex]);
            return;
          }
        }
      }

      // Flip card
      if (e.key === 'f' || e.key === 'F') {
        e.preventDefault();
        toggleFlip();
        return;
      }

      // Hint toggle
      if (e.key === 'h' || e.key === 'H') {
        e.preventDefault();
        toggleFrontHint();
        return;
      }

      if (studyMode === 'flashcard') {
        // If on chapter milestone completion screen
        if (reviewQueue.length === 0 || queueIndex >= reviewQueue.length) {
          if (e.key === ' ' || e.key === 'Enter') {
            e.preventDefault();
            const currentIdx = chapters.findIndex(c => c.dir === currentChapter?.dir);
            if (currentIdx !== -1 && currentIdx + 1 < chapters.length) {
              skipToNextChapter();
            } else {
              restartFromChapter1();
            }
            return;
          }
          if (e.key === 'p' || e.key === 'P') {
            e.preventDefault();
            if (isAutoAdvancePaused) resumeAutoAdvance();
            else pauseAutoAdvance();
            return;
          }
          return;
        }

        // Space / Enter handling during active flashcard review
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
          if (e.key === 'a' || e.key === 'A' || e.key === 'ArrowLeft' || e.key === 'Backspace') {
            e.preventDefault();
            rateCard('dont_remember');
            return;
          }
          if (e.key === 'd' || e.key === 'D' || e.key === 'ArrowRight') {
            e.preventDefault();
            rateCard('remembered');
            return;
          }

          // Hotkeys 3-9 switch pill tabs on Back card
          const tabMap = {
            '3': 'idioms',
            '4': 'decomp',
            '5': 'mnemonics',
            '6': 'traps',
            '7': 'cognates',
            '8': 'contrasts',
            '9': 'passages'
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
    const searchClearBtn = document.getElementById('search-clear-btn');
    if (searchInput) {
      searchInput.addEventListener('input', () => {
        if (searchClearBtn) {
          searchClearBtn.classList.toggle('visible', !!searchInput.value);
        }
        applyFilters();
      });
    }

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
    const handleThemeToggle = () => {
      const isLight = document.body.getAttribute('data-theme') === 'light';
      const newTheme = isLight ? 'dark' : 'light';
      document.body.setAttribute('data-theme', newTheme);
      localStorage.setItem('hsk_theme', newTheme);
    };
    document.getElementById('theme-btn')?.addEventListener('click', handleThemeToggle);
    document.getElementById('main-theme-btn')?.addEventListener('click', handleThemeToggle);

    // Chapter Select
    const chapterSelect = document.getElementById('chapter-select');
    if (chapterSelect) {
      chapterSelect.addEventListener('change', (e) => {
        switchChapter(e.target.value);
      });
    }

    // Settings Drawer Controls
    const autoAdvanceCheck = document.getElementById('toggle-auto-advance');
    if (autoAdvanceCheck) {
      autoAdvanceCheck.addEventListener('change', (e) => {
        StorageManager.saveSettings({ autoAdvanceChapter: e.target.checked });
      });
    }

    const delayRange = document.getElementById('auto-advance-delay-range');
    const delayLabel = document.getElementById('countdown-val-label');
    if (delayRange) {
      delayRange.addEventListener('input', (e) => {
        const val = parseInt(e.target.value, 10);
        if (delayLabel) delayLabel.textContent = `${val}s`;
        StorageManager.saveSettings({ autoAdvanceDelay: val });
      });
    }

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

    const soundFxCheck = document.getElementById('toggle-sound-fx');
    if (soundFxCheck) {
      soundFxCheck.addEventListener('change', (e) => {
        StorageManager.saveSettings({ soundFx: e.target.checked });
      });
    }

    const passagePinyinCheck = document.getElementById('toggle-passage-pinyin');
    if (passagePinyinCheck) {
      passagePinyinCheck.addEventListener('change', (e) => {
        StorageManager.saveSettings({ showPassagePinyin: e.target.checked });
        document.querySelectorAll('.passage-pinyin').forEach(el => {
          el.classList.toggle('pinyin-hidden', !e.target.checked);
        });
        document.querySelectorAll('.btn-toggle-pinyin').forEach(b => {
          b.classList.toggle('active', e.target.checked);
        });
      });
    }

    const voiceSelect = document.getElementById('voice-preference-select');
    if (voiceSelect) {
      voiceSelect.addEventListener('change', (e) => {
        const val = e.target.value;
        StorageManager.saveSettings({ preferredVoice: val });
        const voiceLabel = document.getElementById('voice-persona-label');
        if (voiceLabel) {
          voiceLabel.textContent = val === 'random'
            ? '🎲 Random'
            : (typeof AudioManager !== 'undefined' ? (AudioManager.VOICE_LABELS[val] || val) : val);
        }
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
      if (currentActiveTab === 'synonyms') currentActiveTab = 'contrasts';
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

    getCurrentWord,
    showAnswer,
    rateCard,
    switchTab,
    cycleTab,
    speakActiveTabContent,
    toggleFlip,
    setStudyMode,
    filterByReviewStatus,
    prevCard,
    nextCard,
    toggleFrontHint,
    togglePassagePinyin,
    copyText,
    clearSearch,
    openChapterPicker,
    toggleChapterPicker,
    restartQueue() {
      clearAutoAdvanceTimer();
      sessionGoodCount = 0;
      sessionAgainCount = 0;
      buildReviewQueue();
      renderCurrentWord();
    },
    studyCurrentWord(id) {
      setStudyMode('flashcard');
      selectWordById(id);
    },
    openWordListDrawer,
    closeWordListDrawer,
    toggleWordListDrawer,
    openLookupDrawer,
    openSettingsDrawer,
    closeDrawers,
    toggleShortcutsModal,
    resetCurrentChapterProgress,
    skipToNextChapter,
    pauseAutoAdvance,
    resumeAutoAdvance,
    restartFromChapter1,
    getAutoAdvanceDelay() {
      return StorageManager.getSettings().autoAdvanceDelay || 5;
    }
  };
})();

// Attach to window for inline onclick handlers
if (typeof window !== 'undefined') {
  window.App = App;
}

// Start on DOM ready
document.addEventListener('DOMContentLoaded', () => App.init());
