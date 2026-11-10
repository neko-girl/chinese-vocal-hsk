/**
 * Application Controller for Chinese Vocal HSK Visualizer & Anki Flashcard System.
 * Coordinates two-stage SRS review loops, intra-session anti-clustering re-queueing,
 * multi-chapter global pool, automatic chapter progression, and keyboard shortcuts.
 */

const App = (function() {
  let chapters = [];
  let currentChapter = null;
  let allChaptersData = {}; // { [chapterDir]: Array<Word> }
  let WORDS = [];
  let filteredWords = [];
  
  // Flashcard review queue & state
  let reviewQueue = []; // array of composite keys: "${chapterDir}:${wordId}"
  let queueIndex = 0;
  let currentCardSide = 'front'; // 'front' | 'back'
  let currentActiveTab = 'sentences';
  let studyMode = 'flashcard'; // 'flashcard' | 'browse'
  let currentActiveView = 'study'; // 'study' | 'chapters' | 'stats' | 'settings' | 'dictionary'
  let reviewFilter = 'all'; // legacy filter support
  let activeChapterFilter = 'all'; // 'all' (All Active Chapters) | 'chapter_01' .. 'chapter_08'
  let activeStatusFilter = 'all';  // 'all' (Smart Mix 3:1) | 'due' | 'new' | 'learning' | 'leeches'
  let currentPosFilter = 'ALL';
  let currentLang = 'both';
  let sessionStartTime = Date.now();
  let frontierChapter = 'chapter_01';

  // Dedicated Browser & Catalog View State
  let browserSearchQuery = '';
  let browserStatusFilter = 'all';

  const MIN_GAP = 5;
  const AUTO_ADVANCE_THRESHOLD = 5;

  // Dedicated Dictionary View State
  let selectedDictWordId = null;
  let dictSearchQuery = '';
  let dictPosFilter = 'ALL';
  let dictStatusFilter = 'all';

  // Cross-Window Real-Time Synchronization Channel
  const syncChannel = (typeof BroadcastChannel !== 'undefined') ? new BroadcastChannel('hsk_sync_channel') : null;
  if (syncChannel) {
    syncChannel.onmessage = (event) => {
      const { type, payload } = event.data || {};
      if (type === 'review_updated') {
        if (currentActiveView === 'stats' || currentActiveView === 'dictionary') {
          renderCurrentWord();
        } else if (currentActiveView === 'flashcard') {
          updateMasteryStats();
          updateFilterCountBadges();
          updateFilterPills();
        }
      } else if (type === 'chapter_switched') {
        if (payload?.dir && payload.dir !== currentChapter?.dir) {
          switchChapter(payload.dir, false);
        }
      } else if (type === 'afk_changed') {
        if (typeof TimeTracker !== 'undefined') {
          updateTopBarTimePill(TimeTracker.getStatus());
        }
      }
    };
  }

  function broadcastSync(type, payload = {}) {
    if (syncChannel) {
      try { syncChannel.postMessage({ type, payload }); } catch (e) {}
    }
  }

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

  // Parse composite card key ("${chapterDir}:${wordId}")
  function parseCompositeKey(key) {
    if (typeof key === 'string' && key.includes(':')) {
      const [chapterDir, wordId] = key.split(':');
      return { chapterDir, wordId };
    }
    return {
      chapterDir: currentChapter ? currentChapter.dir : 'chapter_01',
      wordId: String(key || '1')
    };
  }

  // Get full word object by composite key
  function getWordByCompositeKey(key) {
    const { chapterDir, wordId } = parseCompositeKey(key);
    const chWords = allChaptersData[chapterDir] || (currentChapter?.dir === chapterDir ? WORDS : []);
    const found = chWords.find(w => String(w.id) === String(wordId));
    if (found) {
      return { ...found, chapterId: chapterDir };
    }
    const fallback = WORDS.find(w => String(w.id) === String(wordId));
    return fallback ? { ...fallback, chapterId: chapterDir } : WORDS[0] || null;
  }

  // Current active word object
  function getCurrentWord() {
    if (currentActiveView === 'dictionary' && selectedDictWordId) {
      return WORDS.find(w => String(w.id) === String(selectedDictWordId)) || WORDS[0] || null;
    }
    if (studyMode === 'flashcard') {
      const key = reviewQueue[queueIndex];
      if (!key) return null;
      return getWordByCompositeKey(key);
    } else {
      const w = WORDS[queueIndex] || WORDS[0] || null;
      return w ? { ...w, chapterId: currentChapter?.dir || 'chapter_01' } : null;
    }
  }

  // Determine active chapter directories based on filter and frontier
  function getActiveChapterDirs() {
    if (activeChapterFilter !== 'all') {
      return [activeChapterFilter];
    }
    const frontier = StorageManager.getFrontierChapter();
    const frontierIdx = Math.max(0, chapters.findIndex(c => c.dir === frontier));
    const active = chapters.slice(0, frontierIdx + 1).map(c => c.dir);
    return active.length > 0 ? active : [chapters[0]?.dir || 'chapter_01'];
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
    }, 2400);
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
    const now = Date.now();
    
    let due = 0, lapses = 0, remembered = 0, newWords = 0;
    WORDS.forEach(w => {
      const rev = reviews[String(w.id)];
      if (!rev || rev.state === 'new') {
        newWords++;
        due++;
      } else {
        if (rev.state === 'review') remembered++;
        if (rev.state === 'relearning' || rev.lapses > 0) lapses++;
        if (StorageManager.isDue(rev, now)) due++;
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

  // Update Dynamic Study Filter Bar Pills
  function updateFilterPills() {
    if (typeof renderStudyFilterPills !== 'function' || !chapters || chapters.length === 0) return;

    const chapterCounts = { all: 0 };
    const statusCounts = { all: 0, due: 0, new: 0, learning: 0 };
    const now = Date.now();

    const frontier = StorageManager.getFrontierChapter();
    const frontierIdx = Math.max(0, chapters.findIndex(c => c.dir === frontier));

    chapters.forEach((ch, idx) => {
      const chWords = allChaptersData[ch.dir] || (ch.dir === currentChapter?.dir ? WORDS : []);
      const chReviews = StorageManager.getChapterReviews(ch.dir);
      let countThisCh = 0;

      chWords.forEach(w => {
        const rev = chReviews[String(w.id)];
        const isDue = StorageManager.isDue(rev, now);
        const state = rev?.state || 'new';

        countThisCh++;

        const isWithinHorizon = (activeChapterFilter === 'all' && idx <= frontierIdx) || (activeChapterFilter === ch.dir);

        if (isWithinHorizon) {
          chapterCounts.all++;
          if (state === 'new') {
            statusCounts.new++;
          } else if (state === 'learning' || state === 'relearning') {
            statusCounts.learning++;
          } else if (state === 'review' && isDue) {
            statusCounts.due++;
          }
        }
      });
      chapterCounts[ch.dir] = countThisCh;
    });

    statusCounts.all = statusCounts.due + statusCounts.new + statusCounts.learning;

    renderStudyFilterPills({
      chapters,
      activeChapterFilter,
      activeStatusFilter,
      chapterCounts,
      statusCounts,
      onSelectChapterFilter: selectChapterFilter,
      onSelectStatusFilter: selectStatusFilter
    });
  }

  // Build the review queue with Smart Mix interleaving (3 Due : 1 New)
  function buildReviewQueue() {
    const activeDirs = getActiveChapterDirs();
    const dueList = [];
    const newList = [];
    const learningList = [];
    const now = Date.now();

    for (const dir of activeDirs) {
      const words = allChaptersData[dir] || (currentChapter?.dir === dir ? WORDS : []);
      const reviews = StorageManager.getChapterReviews(dir);

      for (const w of words) {
        if (currentPosFilter !== 'ALL') {
          const pos = (w.part_of_speech || '').toLowerCase();
          if (!pos.includes(currentPosFilter.toLowerCase())) continue;
        }

        const key = `${dir}:${w.id}`;
        const rev = reviews[String(w.id)];
        const state = rev?.state || 'new';

        if (state === 'new') {
          newList.push(key);
        } else if (state === 'learning' || state === 'relearning') {
          learningList.push(key);
        } else if (state === 'review') {
          if (StorageManager.isDue(rev, now)) {
            dueList.push(key);
          }
        }
      }
    }

    const settings = StorageManager.getSettings();

    // Enforce daily new card limit if configured
    const dailyLimit = typeof settings.dailyNewLimit === 'number' ? settings.dailyNewLimit : 20;
    if (dailyLimit > 0 && newList.length > dailyLimit) {
      newList = newList.slice(0, dailyLimit);
    }

    if (settings.studyOrder === 'shuffle') {
      dueList.sort(() => Math.random() - 0.5);
      newList.sort(() => Math.random() - 0.5);
      learningList.sort(() => Math.random() - 0.5);
    }

    let finalQueue = [];

    if (activeStatusFilter === 'due') {
      finalQueue = [...dueList, ...learningList];
    } else if (activeStatusFilter === 'new') {
      finalQueue = [...newList];
    } else if (activeStatusFilter === 'learning') {
      finalQueue = [...learningList];
    } else if (activeStatusFilter === 'leeches') {
      const leechesList = [];
      for (const dir of activeDirs) {
        const words = allChaptersData[dir] || [];
        const reviews = StorageManager.getChapterReviews(dir);
        for (const w of words) {
          const rev = reviews[String(w.id)];
          if (rev && (rev.lapses || 0) > 0) {
            leechesList.push({ key: `${dir}:${w.id}`, lapses: rev.lapses });
          }
        }
      }
      leechesList.sort((a, b) => b.lapses - a.lapses);
      finalQueue = leechesList.map(item => item.key);
    } else {
      // Smart Mix Interleaving: 3 Due Reviews : 1 New Card
      let dIdx = 0;
      let nIdx = 0;
      const interleaved = [];

      while (dIdx < dueList.length || nIdx < newList.length) {
        for (let k = 0; k < 3 && dIdx < dueList.length; k++) {
          interleaved.push(dueList[dIdx++]);
        }
        if (nIdx < newList.length) {
          interleaved.push(newList[nIdx++]);
        }
      }

      finalQueue = [...learningList, ...interleaved];
    }

    reviewQueue = finalQueue;
    queueIndex = 0;
    currentCardSide = 'front';
  }

  // Fetch backfill cards when queue length ahead is less than MIN_GAP (5)
  function fetchBackfillCards(count, excludeKeys = []) {
    const excludeSet = new Set(excludeKeys);
    const backfill = [];
    const activeDirs = getActiveChapterDirs();
    const now = Date.now();

    // 1. Try due review cards not already queued
    for (const dir of activeDirs) {
      const words = allChaptersData[dir] || [];
      const reviews = StorageManager.getChapterReviews(dir);
      for (const w of words) {
        const key = `${dir}:${w.id}`;
        if (excludeSet.has(key)) continue;
        const rev = reviews[String(w.id)];
        if (rev?.state === 'review' && StorageManager.isDue(rev, now)) {
          backfill.push(key);
          excludeSet.add(key);
          if (backfill.length >= count) return backfill;
        }
      }
    }

    // 2. Try new cards from active chapters
    for (const dir of activeDirs) {
      const words = allChaptersData[dir] || [];
      const reviews = StorageManager.getChapterReviews(dir);
      for (const w of words) {
        const key = `${dir}:${w.id}`;
        if (excludeSet.has(key)) continue;
        const rev = reviews[String(w.id)];
        if (!rev || rev.state === 'new') {
          backfill.push(key);
          excludeSet.add(key);
          if (backfill.length >= count) return backfill;
        }
      }
    }

    // 3. Try next chapter words if available
    const frontier = StorageManager.getFrontierChapter();
    const currentIdx = chapters.findIndex(c => c.dir === frontier);
    if (currentIdx !== -1 && currentIdx + 1 < chapters.length) {
      const nextDir = chapters[currentIdx + 1].dir;
      const nextWords = allChaptersData[nextDir] || [];
      for (const w of nextWords) {
        const key = `${nextDir}:${w.id}`;
        if (excludeSet.has(key)) continue;
        const rev = StorageManager.getWordReview(nextDir, w.id);
        if (!rev || rev.state === 'new') {
          backfill.push(key);
          excludeSet.add(key);
          if (backfill.length >= count) return backfill;
        }
      }
    }

    return backfill;
  }

  // Anti-Clustering Insertion Guard (MIN_GAP = 5)
  function insertWithAntiClustering(cardKey, targetOffset) {
    const remainingAhead = reviewQueue.length - (queueIndex + 1);
    const minRequired = Math.min(targetOffset, MIN_GAP);

    if (remainingAhead < minRequired) {
      const needed = minRequired - remainingAhead;
      const backfilled = fetchBackfillCards(needed, [cardKey, ...reviewQueue.slice(queueIndex + 1)]);
      if (backfilled.length > 0) {
        reviewQueue.push(...backfilled);
      }
    }

    let targetIndex = Math.min(reviewQueue.length, queueIndex + 1 + targetOffset);

    // Ensure cardKey is not placed within MIN_GAP (5) positions of another identical card
    let hasConflict = false;
    for (let i = Math.max(0, targetIndex - MIN_GAP); i <= Math.min(reviewQueue.length - 1, targetIndex + MIN_GAP); i++) {
      if (i !== queueIndex && reviewQueue[i] === cardKey) {
        hasConflict = true;
        break;
      }
    }

    if (hasConflict) {
      for (let i = queueIndex + MIN_GAP; i <= reviewQueue.length + MIN_GAP; i++) {
        let conflictAtI = false;
        for (let k = Math.max(0, i - MIN_GAP); k <= Math.min(reviewQueue.length - 1, i + MIN_GAP); k++) {
          if (k !== queueIndex && reviewQueue[k] === cardKey) {
            conflictAtI = true;
            break;
          }
        }
        if (!conflictAtI) {
          targetIndex = Math.min(reviewQueue.length, i);
          break;
        }
      }
    }

    reviewQueue.splice(targetIndex, 0, cardKey);
  }

  // Automatic Next-Chapter Progression (Low-Card Spillover)
  function checkAndTriggerSpillover() {
    const settings = StorageManager.getSettings();
    if (!settings.autoAdvanceChapter && activeChapterFilter !== 'all') {
      return;
    }

    const currentFrontier = StorageManager.getFrontierChapter();
    const frontierWords = allChaptersData[currentFrontier] || [];
    if (frontierWords.length === 0) return;

    let unlearnedCount = 0;
    for (const w of frontierWords) {
      const rev = StorageManager.getWordReview(currentFrontier, w.id);
      if (!rev || rev.state === 'new' || rev.state === 'learning' || rev.state === 'relearning') {
        unlearnedCount++;
      }
    }

    const threshold = (typeof settings.autoAdvanceThreshold === 'number') ? settings.autoAdvanceThreshold : AUTO_ADVANCE_THRESHOLD;
    if (unlearnedCount <= threshold) {
      const currentIdx = chapters.findIndex(c => c.dir === currentFrontier);
      if (currentIdx !== -1 && currentIdx + 1 < chapters.length) {
        const nextChapter = chapters[currentIdx + 1];
        StorageManager.setFrontierChapter(nextChapter.dir);

        const nextWords = allChaptersData[nextChapter.dir] || [];
        const queuedKeys = new Set(reviewQueue);
        const injected = [];

        for (const nw of nextWords) {
          const key = `${nextChapter.dir}:${nw.id}`;
          if (!queuedKeys.has(key)) {
            const rev = StorageManager.getWordReview(nextChapter.dir, nw.id);
            if (!rev || rev.state === 'new') {
              injected.push(key);
              queuedKeys.add(key);
            }
          }
        }

        if (injected.length > 0) {
          reviewQueue.push(...injected);
          const curChObj = chapters[currentIdx];
          showToast(`🎉 ${curChObj.name} nearly complete — mixing in new words from ${nextChapter.name}!`);
        }
      }
    }
  }

  // Filter Pill Select Handlers
  function selectChapterFilter(chVal) {
    activeChapterFilter = chVal;
    StorageManager.saveSettings({ activeChapterFilter: chVal });
    if (chVal !== 'all') {
      const found = chapters.find(c => c.dir === chVal);
      if (found) {
        currentChapter = found;
        WORDS = allChaptersData[found.dir] || WORDS;
        filteredWords = [...WORDS];
        const pillEl = document.getElementById('chapter-pill');
        if (pillEl) pillEl.textContent = `CHP ${found.id}`;
      }
    }
    buildReviewQueue();
    renderCurrentWord();
  }

  function selectStatusFilter(stVal) {
    activeStatusFilter = stVal;
    StorageManager.saveSettings({ activeStatusFilter: stVal });
    buildReviewQueue();
    renderCurrentWord();
  }

  // Persist exact active session snapshot
  function persistActiveSession() {
    if (typeof StorageManager === 'undefined') return;
    StorageManager.saveActiveSession({
      queue: reviewQueue,
      currentIndex: queueIndex,
      activeFilters: { chapter: activeChapterFilter, status: activeStatusFilter },
      frontierChapterId: frontierChapter,
      startedAt: sessionStartTime || Date.now()
    });
  }

  // Undo last card rating action (Ctrl+Z / Topbar button)
  function undoLastAction() {
    if (typeof StorageManager === 'undefined' || !StorageManager.canUndo()) return;
    const popped = StorageManager.popUndo();
    if (popped) {
      if (Array.isArray(popped.prevQueue)) {
        reviewQueue = popped.prevQueue;
      }
      queueIndex = typeof popped.prevIndex === 'number' ? popped.prevIndex : Math.max(0, queueIndex - 1);
      currentCardSide = 'front';
      persistActiveSession();
      renderCurrentWord();
      showToast('↶ Undid last card action');
      playAudioFeedback('click');
    }
  }

  // Rate Card action (Again, Hard, Good, Easy) with Intra-Session Re-queueing
  function rateCard(rating) {
    const card = getCurrentWord();
    if (!card) return;

    const chDir = card.chapterId || currentChapter?.dir || 'chapter_01';
    const wordKey = `${chDir}:${card.id}`;

    // Push previous card and queue state onto undo stack before mutating
    const prevRecord = StorageManager.getWordReview(chDir, card.id);
    StorageManager.pushUndo({
      chapterId: chDir,
      wordId: card.id,
      prevRecord,
      prevQueue: [...reviewQueue],
      prevIndex: queueIndex
    });

    if (rating === 'again') {
      sessionAgainCount++;
      playAudioFeedback('again');
    } else {
      sessionGoodCount++;
      playAudioFeedback('good');
    }

    const res = StorageManager.recordReview(chDir, card.id, rating);
    broadcastSync('review_updated', { chapterDir: chDir, wordId: card.id, rating });

    if (!res.graduated && typeof res.reinsertOffset === 'number') {
      insertWithAntiClustering(wordKey, res.reinsertOffset);
    }

    queueIndex++;
    currentCardSide = 'front';

    // Auto-Alternate Voice progression
    if (typeof AudioManager !== 'undefined' && typeof AudioManager.setAlternateVoiceIndex === 'function') {
      AudioManager.setAlternateVoiceIndex();
    }

    persistActiveSession();
    checkAndTriggerSpillover();
    renderCurrentWord();
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

    // Update Tri-Segment Session Progress Bar
    const segNewEl = document.getElementById('seg-fill-new');
    const segLearnEl = document.getElementById('seg-fill-learning');
    const segReviewEl = document.getElementById('seg-fill-review');
    const countNewEl = document.getElementById('val-count-new');
    const countLearnEl = document.getElementById('val-count-learning');
    const countReviewEl = document.getElementById('val-count-review');

    let qNew = 0;
    let qLearn = 0;
    let qRev = 0;

    reviewQueue.forEach(itemKey => {
      const parts = String(itemKey).split(':');
      const itemCh = parts.length === 2 ? parts[0] : (currentChapter ? currentChapter.dir : 'chapter_01');
      const itemWId = parts.length === 2 ? parts[1] : itemKey;
      const rev = StorageManager.getWordReview(itemCh, itemWId);
      if (!rev || rev.state === 'new') qNew++;
      else if (rev.state === 'learning' || rev.state === 'relearning') qLearn++;
      else if (rev.state === 'review') qRev++;
      else qNew++;
    });

    const totalQ = reviewQueue.length || 1;
    if (segNewEl) segNewEl.style.width = `${Math.round((qNew / totalQ) * 100)}%`;
    if (segLearnEl) segLearnEl.style.width = `${Math.round((qLearn / totalQ) * 100)}%`;
    if (segReviewEl) segReviewEl.style.width = `${Math.round((qRev / totalQ) * 100)}%`;

    if (countNewEl) countNewEl.textContent = qNew;
    if (countLearnEl) countLearnEl.textContent = qLearn;
    if (countReviewEl) countReviewEl.textContent = qRev;

    // Update Undo Button state
    const undoBtn = document.getElementById('btn-undo');
    if (undoBtn) {
      undoBtn.disabled = !StorageManager.canUndo();
    }
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
    const settingsBadge = document.getElementById('settings-ch-badge');
    const titleEl = document.getElementById('topbar-ch-title');
    const currentWord = getCurrentWord();
    const chNum = currentWord?.chapterId
      ? (currentWord.chapterId.match(/\d+/) ? parseInt(currentWord.chapterId.match(/\d+/)[0], 10) : currentChapter.id)
      : currentChapter.id;

    if (badgeEl) badgeEl.textContent = activeChapterFilter === 'all' ? `ALL ACTIVE` : `CHP ${chNum}`;
    if (settingsBadge) settingsBadge.textContent = `CHP ${currentChapter.id}`;
    if (titleEl) titleEl.textContent = activeChapterFilter === 'all' ? 'All Active Chapters (Smart Mix)' : (currentChapter.title || currentChapter.name);
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

    const ankiActionBar = document.getElementById('anki-action-bar');

    if (currentActiveView === 'study' || currentActiveView === 'flashcard') {
      if (ankiActionBar) ankiActionBar.style.display = '';

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
        updateFilterPills();
        return;
      }

      // We are in an active card review
      clearAutoAdvanceTimer();
      const w = getCurrentWord();
      if (!w) return;

      const chDir = w.chapterId || currentChapter.dir;
      const reviewItem = StorageManager.getWordReview(chDir, w.id);

      // Sticky pill tab memory
      const settings = StorageManager.getSettings();
      currentActiveTab = settings.lastBackTab || currentActiveTab || 'sentences';

      if (currentCardSide === 'front') {
        container.innerHTML = renderFlashcardFront(w, chDir, reviewItem);
        // Audio-First mode: automatically play headword audio on front reveal
        if (settings.audioFirstMode) {
          setTimeout(() => {
            speakCurrentHeadword(1.0);
          }, 120);
        }
      } else {
        container.innerHTML = renderFlashcardBack(w, chDir, reviewItem, currentLang, currentActiveTab);
      }

      renderActionBar(currentCardSide, 'flashcard', reviewItem);

      // Background Audio Preloading for next upcoming cards
      if (typeof AudioManager !== 'undefined' && typeof AudioManager.preloadUpcomingWords === 'function') {
        const nextCards = [];
        if (queueIndex + 1 < reviewQueue.length) {
          const w1 = getWordByKey(reviewQueue[queueIndex + 1]);
          if (w1) nextCards.push(w1);
        }
        if (queueIndex + 2 < reviewQueue.length) {
          const w2 = getWordByKey(reviewQueue[queueIndex + 2]);
          if (w2) nextCards.push(w2);
        }
        AudioManager.preloadUpcomingWords(nextCards);
      }

      const reviews = StorageManager.getChapterReviews(chDir);
      const activeWord = getCurrentWord();
      renderSidebar(filteredWords, WORDS, activeWord?.id, currentLang, selectWordById, reviews);
    } else if (currentActiveView === 'chapters') {
      if (ankiActionBar) ankiActionBar.style.display = 'none';
      clearAutoAdvanceTimer();

      if (typeof renderChaptersAndWordBrowser === 'function') {
        renderChaptersAndWordBrowser({
          chapters,
          activeChapter: currentChapter,
          allWords: getAllCurriculumWords(),
          currentLang,
          frontierChapter: StorageManager.getFrontierChapter(),
          searchQuery: browserSearchQuery,
          statusFilter: browserStatusFilter
        });
      }
    } else if (currentActiveView === 'dictionary') {
      if (ankiActionBar) ankiActionBar.style.display = 'none';
      clearAutoAdvanceTimer();

      const selectedWord = selectedDictWordId
        ? (WORDS.find(w => String(w.id) === String(selectedDictWordId)) || WORDS[0])
        : (getCurrentWord() || WORDS[0]);

      if (typeof renderDictionaryWindow === 'function') {
        renderDictionaryWindow({
          words: WORDS,
          selectedWord,
          currentLang,
          currentChapter,
          searchQuery: dictSearchQuery,
          selectedPos: dictPosFilter,
          selectedStatus: dictStatusFilter
        });
      }
    } else if (currentActiveView === 'stats') {
      if (ankiActionBar) ankiActionBar.style.display = 'none';
      clearAutoAdvanceTimer();

      if (typeof renderStatisticsDashboard === 'function') {
        renderStatisticsDashboard({
          currentChapter,
          chapters,
          words: getAllCurriculumWords()
        });
      }
    } else if (currentActiveView === 'settings') {
      if (ankiActionBar) ankiActionBar.style.display = 'none';
      clearAutoAdvanceTimer();
      openSettingsDrawer();
    }

    updateMasteryStats();
    updateFilterCountBadges();
    updateFilterPills();

    const scrollContainer = document.getElementById('main-scroll');
    if (scrollContainer && typeof scrollContainer.scrollTo === 'function') {
      scrollContainer.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  // Select word by ID
  function selectWordById(id) {
    if (studyMode === 'flashcard') {
      const idx = reviewQueue.findIndex(qid => {
        const parsed = parseCompositeKey(qid);
        return String(parsed.wordId) === String(id) || String(qid) === String(id);
      });
      if (idx !== -1) {
        queueIndex = idx;
      } else {
        const ch = currentChapter ? currentChapter.dir : 'chapter_01';
        reviewQueue.splice(queueIndex, 0, `${ch}:${id}`);
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
    StorageManager.saveSettings({ activeTab: tabId, lastBackTab: tabId });
    StorageManager.recordStudyEvent('tab_view', { tab: tabId });

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

    const settingsSelectEl = document.getElementById('settings-chapter-select');
    if (settingsSelectEl && settingsSelectEl.value !== found.dir) {
      settingsSelectEl.value = found.dir;
    }

    const settingsBadge = document.getElementById('settings-ch-badge');
    if (settingsBadge) {
      settingsBadge.textContent = `CHP ${found.id}`;
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

  // Switch Top-Level Dedicated View ('study' | 'chapters' | 'stats' | 'settings' | 'dictionary')
  function switchView(viewName) {
    if (viewName === 'flashcard') viewName = 'study';
    if (!['study', 'chapters', 'stats', 'settings', 'dictionary'].includes(viewName)) {
      viewName = 'study';
    }

    currentActiveView = viewName;
    studyMode = (viewName === 'dictionary') ? 'browse' : 'flashcard';
    StorageManager.saveSettings({ activeView: viewName, studyMode });

    if (typeof TimeTracker !== 'undefined') {
      TimeTracker.setMode(viewName);
    }

    // Update bottom nav items
    document.querySelectorAll('.mobile-nav-item').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-view') === viewName);
    });

    // Update desktop nav tabs
    document.querySelectorAll('.desktop-nav-tab').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-view') === viewName);
    });

    // Update drawer view buttons
    document.querySelectorAll('.view-btn').forEach(btn => {
      const v = btn.getAttribute('data-view');
      btn.classList.toggle('active', (v === viewName) || (v === 'flashcard' && viewName === 'study'));
    });

    // Toggle view containers
    const studyView = document.getElementById('view-study');
    const chaptersView = document.getElementById('view-chapters');
    const statsView = document.getElementById('view-stats');
    const settingsView = document.getElementById('view-settings');
    const hud = document.getElementById('topbar-study-hud');

    if (studyView) studyView.style.display = (viewName === 'study' || viewName === 'dictionary') ? 'block' : 'none';
    if (chaptersView) chaptersView.style.display = (viewName === 'chapters') ? 'block' : 'none';
    if (statsView) statsView.style.display = (viewName === 'stats') ? 'block' : 'none';
    if (settingsView) settingsView.style.display = (viewName === 'settings') ? 'block' : 'none';
    if (hud) hud.style.display = (viewName === 'study') ? 'flex' : 'none';

    renderCurrentWord();
    playAudioFeedback('click');
  }

  function speakCurrentHeadword(speed = 1.0) {
    const w = getCurrentWord();
    if (!w) return;
    if (typeof AudioManager !== 'undefined') {
      AudioManager.play(w.audio, w.hanzi, speed);
    } else {
      speak(w.hanzi, speed);
    }
  }

  function handleFrontHanziClick(boxEl) {
    const settings = StorageManager.getSettings();
    if (settings.audioFirstMode && boxEl && boxEl.classList.contains('audio-first-blur')) {
      boxEl.classList.remove('audio-first-blur');
    } else {
      showAnswer();
    }
  }

  function unblurFrontHanzi() {
    const box = document.getElementById('front-tianzige-box');
    if (box) box.classList.remove('audio-first-blur');
  }

  function getWordByKey(compositeKey) {
    if (!compositeKey) return null;
    const parts = String(compositeKey).split(':');
    if (parts.length === 2) {
      const [chDir, idStr] = parts;
      const chWords = allChaptersData[chDir] || [];
      const found = chWords.find(item => String(item.id) === idStr);
      if (found) return { ...found, chapterId: chDir };
    }
    return WORDS.find(item => String(item.id) === String(compositeKey)) || null;
  }

  function getAllCurriculumWords() {
    const list = [];
    for (const ch of chapters) {
      const chWords = allChaptersData[ch.dir] || (currentChapter?.dir === ch.dir ? WORDS : []);
      chWords.forEach(w => {
        list.push({ ...w, chapterId: ch.dir });
      });
    }
    return list;
  }

  function studySpecificChapter(chDir) {
    activeChapterFilter = chDir;
    const found = chapters.find(c => c.dir === chDir);
    if (found) currentChapter = found;
    switchView('study');
    buildReviewQueue();
    renderCurrentWord();
  }

  function setFrontierChapter(chDir) {
    frontierChapter = chDir;
    StorageManager.setFrontierChapter(chDir);
    showToast(`⭐ Set ${chDir} as active curriculum frontier`);
    renderCurrentWord();
  }

  function onBrowserSearch(val) {
    browserSearchQuery = val;
    renderCurrentWord();
    const input = document.getElementById('chapter-word-search-input');
    if (input) {
      input.focus();
      input.setSelectionRange(val.length, val.length);
    }
  }

  function filterBrowserStatus(status) {
    browserStatusFilter = status;
    renderCurrentWord();
  }

  function openWordDetail(chDir, wordId) {
    const chWords = allChaptersData[chDir] || [];
    const w = chWords.find(item => String(item.id) === String(wordId)) || WORDS.find(item => String(item.id) === String(wordId));
    if (!w) return;
    const rev = StorageManager.getWordReview(chDir, wordId);
    if (typeof renderWordDetailModal === 'function') {
      renderWordDetailModal(w, rev, chDir, currentLang);
    }
  }

  function confirmResetWord(chDir, wordId) {
    if (confirm('Reset this word back to brand new (unlearned) state?')) {
      StorageManager.resetWordReview(chDir, wordId);
      showToast('Word progress reset to new');
      closeModals();
      renderCurrentWord();
    }
  }

  function studySpecificWord(chDir, wordId) {
    closeModals();
    const chWords = allChaptersData[chDir] || [];
    const w = chWords.find(item => String(item.id) === String(wordId)) || WORDS.find(item => String(item.id) === String(wordId));
    if (!w) return;
    activeChapterFilter = chDir;
    currentChapter = chapters.find(c => c.dir === chDir) || currentChapter;
    switchView('study');
    reviewQueue = [`${chDir}:${wordId}`];
    queueIndex = 0;
    currentCardSide = 'front';
    renderCurrentWord();
  }

  function practiceLeeches() {
    activeStatusFilter = 'leeches';
    switchView('study');
    buildReviewQueue();
    renderCurrentWord();
    showToast('⚡ Practicing difficult leech vocabulary');
  }

  function openBackupCodeModal(mode = 'copy') {
    const modal = document.getElementById('backup-code-modal');
    const title = document.getElementById('backup-code-modal-title');
    const textarea = document.getElementById('backup-code-input');
    const copyBtn = document.getElementById('btn-copy-backup-code');
    const restoreBtn = document.getElementById('btn-restore-backup-code');
    if (!modal || !textarea) return;

    if (mode === 'copy') {
      if (title) title.textContent = '📋 Copy Backup Code';
      textarea.value = StorageManager.exportBackupCode();
      if (copyBtn) copyBtn.style.display = 'inline-block';
      if (restoreBtn) restoreBtn.style.display = 'none';
    } else {
      if (title) title.textContent = '📥 Paste Backup Code';
      textarea.value = '';
      if (copyBtn) copyBtn.style.display = 'none';
      if (restoreBtn) restoreBtn.style.display = 'inline-block';
    }
    modal.classList.add('active');
  }

  function copyBackupCode() {
    const textarea = document.getElementById('backup-code-input');
    if (!textarea || !textarea.value) return;
    copyText(textarea.value, '📋 Backup code copied to clipboard!');
    setTimeout(closeModals, 800);
  }

  function restoreFromBackupCode() {
    const textarea = document.getElementById('backup-code-input');
    if (!textarea || !textarea.value.trim()) {
      showToast('Please paste a backup code');
      return;
    }
    const ok = StorageManager.importBackupCode(textarea.value.trim());
    if (ok) {
      showToast('✨ Backup code restored successfully!');
      closeModals();
      setTimeout(() => {
        window.location.reload();
      }, 500);
    } else {
      showToast('⚠️ Invalid or corrupted backup code');
    }
  }

  function closeModals() {
    document.querySelectorAll('.modal-wrap').forEach(m => m.classList.remove('active'));
  }

  function changeDailyNewLimit(val) {
    const num = parseInt(val, 10);
    StorageManager.saveSettings({ dailyNewLimit: isNaN(num) ? 20 : num });
    const label = document.getElementById('daily-new-val-label');
    if (label) label.textContent = num === 0 ? 'Unlimited' : `${num} cards`;
    buildReviewQueue();
    renderCurrentWord();
  }

  function changeAutoAdvanceThreshold(val) {
    const num = parseInt(val, 10);
    StorageManager.saveSettings({ autoAdvanceThreshold: isNaN(num) ? 5 : num });
    const label = document.getElementById('advance-threshold-val-label');
    if (label) label.textContent = num === 0 ? '0 cards (100%)' : `< ${num} cards`;
  }

  // Pop out current view into an individual standalone OS/browser window
  function popoutCurrentView() {
    const url = `index.html?view=${currentActiveView}&ch=${currentChapter?.dir || 'chapter_01'}`;
    const windowFeatures = 'width=1150,height=850,resizable=yes,scrollbars=yes';
    window.open(url, `hsk_${currentActiveView}_window`, windowFeatures);
    showToast(`⧉ Opened ${currentActiveView} in separate window`);
  }

  // Legacy setStudyMode for compatibility
  function setStudyMode(mode) {
    if (mode === 'browse') {
      switchView('dictionary');
    } else {
      switchView('flashcard');
    }
  }

  // Dictionary Window Interactive Actions
  function selectDictionaryWord(id) {
    selectedDictWordId = id;
    StorageManager.recordStudyEvent('tab_view', { tab: 'dictionary_word', wordId: id });
    renderCurrentWord();
  }

  function onDictSearchInput(val) {
    dictSearchQuery = val;
    renderCurrentWord();
    const input = document.getElementById('dict-search-input');
    if (input) {
      input.focus();
      input.setSelectionRange(val.length, val.length);
    }
  }

  function clearDictSearch() {
    dictSearchQuery = '';
    renderCurrentWord();
  }

  function setDictPosFilter(pos) {
    dictPosFilter = pos;
    renderCurrentWord();
  }

  function setDictStatusFilter(status) {
    dictStatusFilter = status;
    renderCurrentWord();
  }

  function openWordInDictionary(id) {
    selectedDictWordId = id;
    switchView('dictionary');
  }

  function studyCurrentWord(id) {
    switchView('flashcard');
    selectWordById(id);
  }

  // Time Tracker & AFK Status Updates
  function updateTopBarTimePill(status) {
    if (!status) return;
    const timeDisplay = document.getElementById('topbar-time-display');
    const afkDot = document.getElementById('topbar-afk-dot');

    if (timeDisplay && typeof formatSecondsToShort === 'function') {
      timeDisplay.textContent = formatSecondsToShort(status.totalSecondsToday);
    }

    if (afkDot) {
      if (status.isAfk) {
        afkDot.textContent = '⏸️';
        afkDot.className = 'time-afk-dot afk-paused';
        afkDot.title = 'Inactivity Detected (Tracking Paused)';
      } else {
        afkDot.textContent = '🟢';
        afkDot.className = 'time-afk-dot afk-active';
        afkDot.title = 'Active Tracking';
      }
    }

    // Live update in Statistics Dashboard if currently displayed
    if (currentActiveView === 'stats') {
      const liveAfkPill = document.querySelector('.afk-indicator-pill');
      if (liveAfkPill) {
        liveAfkPill.className = `afk-indicator-pill ${status.isAfk ? 'pill-afk' : 'pill-active'}`;
        const spanText = liveAfkPill.querySelector('span:last-child');
        if (spanText) {
          spanText.textContent = status.isAfk ? '⏸️ Idle / AFK (Tracking Paused)' : '🟢 Active (Time Tracking)';
        }
      }
    }
  }

  function changeAfkThreshold(seconds) {
    const secNum = Number(seconds) || 120;
    if (typeof TimeTracker !== 'undefined') {
      TimeTracker.setAfkThresholdSeconds(secNum);
    }
    const select1 = document.getElementById('afk-timeout-setting');
    const select2 = document.getElementById('afk-timeout-select');
    if (select1) select1.value = String(secNum);
    if (select2) select2.value = String(secNum);

    const label = document.getElementById('afk-val-label');
    if (label) label.textContent = `${Math.round(secNum / 60)}m`;

    showToast(`⏱️ AFK timeout set to ${Math.round(secNum / 60)}m`);
  }

  function exportStudyAnalytics() {
    const data = StorageManager.exportAllData();
    const jsonStr = JSON.stringify(data, null, 2);
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `hsk_study_analytics_${new Date().toISOString().slice(0, 10)}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showToast('📥 Study Analytics exported successfully');
  }

  function resetTimeTrackerPrompt() {
    if (confirm('Are you sure you want to reset all active time tracking and study habit statistics? (Flashcard review progress will NOT be lost).')) {
      StorageManager.resetTimeTrackerData();
      renderCurrentWord();
      showToast('🗑️ Time tracker data reset.');
    }
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

  function populateBrowserVoices() {
    const select = document.getElementById('browser-voice-select');
    if (!select || typeof AudioManager === 'undefined' || typeof AudioManager.getAvailableChineseVoices !== 'function') return;
    const voices = AudioManager.getAvailableChineseVoices();
    const currentUri = StorageManager.getSettings().browserVoiceURI || '';

    select.innerHTML = '<option value="">✨ Auto-Select Best Neural Voice</option>';
    voices.forEach(v => {
      const opt = document.createElement('option');
      opt.value = v.voiceURI || v.name;
      const isOnline = v.localService === false || v.name.includes('Online') || v.name.includes('Natural');
      const badge = isOnline ? '⚡ ' : '';
      opt.textContent = `${badge}${v.name} (${v.lang})`;
      if (opt.value === currentUri) opt.selected = true;
      select.appendChild(opt);
    });

    const best = AudioManager.getBestChineseVoice(currentUri);
    const infoEl = document.getElementById('browser-voice-info');
    if (infoEl) {
      if (best) {
        infoEl.textContent = `Active Voice: ${best.name} (${best.lang})`;
      } else {
        infoEl.textContent = 'Auto-detecting best neural/natural voice';
      }
    }
  }

  function changeBrowserVoice(voiceURI) {
    StorageManager.saveSettings({ browserVoiceURI: voiceURI });
    if (typeof AudioManager !== 'undefined') {
      const best = AudioManager.getBestChineseVoice(voiceURI);
      const infoEl = document.getElementById('browser-voice-info');
      if (infoEl && best) {
        infoEl.textContent = `Active Voice: ${best.name} (${best.lang})`;
      }
    }
  }

  function testBrowserVoice() {
    const testPhrase = '你好，祝你汉语学习愉快！';
    const settings = StorageManager.getSettings();
    if (typeof AudioManager !== 'undefined') {
      AudioManager.speakTTS(testPhrase, settings.speechRate || 0.9, document.getElementById('btn-test-browser-voice'));
    }
  }

  let serverSyncActive = false;

  function updateSyncStatusBadge(isConnected) {
    serverSyncActive = !!isConnected;
    const badge = document.getElementById('sync-status-badge');
    if (!badge) return;
    if (isConnected) {
      badge.textContent = '🟢 Server File Synced (data/user_progress.json)';
      badge.style.background = 'rgba(16, 185, 129, 0.15)';
      badge.style.color = '#10b981';
    } else {
      badge.textContent = '⚪ Local Browser Storage';
      badge.style.background = 'rgba(156, 163, 175, 0.15)';
      badge.style.color = 'var(--text-muted)';
    }
  }

  function exportBackupFile() {
    const data = StorageManager.exportAllData();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    const d = new Date().toISOString().slice(0, 10);
    a.href = url;
    a.download = `hsk_progress_backup_${d}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function handleImportBackup(event) {
    const file = event.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = async (e) => {
      try {
        const parsed = JSON.parse(e.target.result);
        const ok = StorageManager.importAllData(parsed);
        if (ok) {
          await StorageManager.syncWithServer();
          alert('✓ Progress successfully imported and restored!');
          location.reload();
        } else {
          alert('Could not parse the backup file. Please verify it is a valid HSK backup JSON.');
        }
      } catch (err) {
        alert('Failed to read file: ' + err.message);
      }
    };
    reader.readAsText(file);
    event.target.value = '';
  }

  function openSettingsDrawer() {
    const drawer = document.getElementById('ankineitor-settings-drawer');
    const overlay = document.getElementById('drawer-overlay');
    if (!drawer) return;

    updateSyncStatusBadge(serverSyncActive);

    const settings = StorageManager.getSettings();
    const autoAudioCheck = document.getElementById('toggle-auto-audio');
    const toneColorsCheck = document.getElementById('toggle-tone-colors');
    const speechRateRange = document.getElementById('speech-rate-range');
    const speechRateLabel = document.getElementById('speech-rate-val-label');
    const autoAdvanceCheck = document.getElementById('toggle-auto-advance');
    const delayRange = document.getElementById('auto-advance-delay-range');
    const delayLabel = document.getElementById('countdown-val-label');
    const soundFxCheck = document.getElementById('toggle-sound-fx');
    const passagePinyinCheck = document.getElementById('toggle-passage-pinyin');
    const voiceSelect = document.getElementById('voice-preference-select');
    const voiceLabel = document.getElementById('voice-persona-label');

    if (autoAudioCheck) autoAudioCheck.checked = !!settings.autoAudio;
    if (toneColorsCheck) toneColorsCheck.checked = !!settings.toneColors;
    if (speechRateRange) {
      speechRateRange.value = settings.speechRate || 0.9;
      if (speechRateLabel) speechRateLabel.textContent = `${(settings.speechRate || 0.9).toFixed(2)}x`;
    }
    if (autoAdvanceCheck) autoAdvanceCheck.checked = settings.autoAdvanceChapter !== false;
    if (delayRange) delayRange.value = settings.autoAdvanceDelay || 5;
    if (delayLabel) delayLabel.textContent = `${settings.autoAdvanceDelay || 5}s`;
    if (soundFxCheck) soundFxCheck.checked = settings.soundFx !== false;
    if (passagePinyinCheck) passagePinyinCheck.checked = !!settings.showPassagePinyin;

    const audioFirstCheck = document.getElementById('toggle-audio-first');
    if (audioFirstCheck) audioFirstCheck.checked = !!settings.audioFirstMode;

    const dailyLimitSelect = document.getElementById('daily-new-limit-select');
    if (dailyLimitSelect) dailyLimitSelect.value = String(settings.dailyNewLimit ?? 20);

    const thresholdSelect = document.getElementById('auto-advance-threshold-select');
    if (thresholdSelect) thresholdSelect.value = String(settings.autoAdvanceThreshold ?? 5);

    if (voiceSelect) {
      voiceSelect.value = settings.preferredVoice || 'random';
      if (voiceLabel) {
        voiceLabel.textContent = (settings.preferredVoice === 'random' || !settings.preferredVoice)
          ? '🎲 Random'
          : (typeof AudioManager !== 'undefined' ? (AudioManager.VOICE_LABELS[settings.preferredVoice] || settings.preferredVoice) : settings.preferredVoice);
      }
    }

    populateBrowserVoices();

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
      if (hintEl.classList.contains('active')) {
        const w = getCurrentWord();
        if (w) StorageManager.recordStudyEvent('hint_peek', { wordId: w.id });
      }
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
    closeModals();
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

      // Undo Shortcut (Ctrl+Z, Cmd+Z, or Z)
      if ((e.ctrlKey || e.metaKey) && (e.key === 'z' || e.key === 'Z')) {
        e.preventDefault();
        undoLastAction();
        return;
      }
      if (e.key === 'z' || e.key === 'Z') {
        if (!e.ctrlKey && !e.metaKey && !e.altKey && (currentActiveView === 'study' || currentActiveView === 'flashcard')) {
          e.preventDefault();
          undoLastAction();
          return;
        }
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

      // Hint toggle (and unblur in Audio-First mode)
      if (e.key === 'h' || e.key === 'H') {
        e.preventDefault();
        unblurFrontHanzi();
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
            rateCard('good');
          }
          return;
        }

        // When Back is showing: 4-rating Anki responses
        if (currentCardSide === 'back') {
          if (e.key === '1' || e.key === 'a' || e.key === 'A' || e.key === 'Backspace') {
            e.preventDefault();
            rateCard('again');
            return;
          }
          if (e.key === '2') {
            e.preventDefault();
            rateCard('hard');
            return;
          }
          if (e.key === '3' || e.key === 'd' || e.key === 'D') {
            e.preventDefault();
            rateCard('good');
            return;
          }
          if (e.key === '4') {
            e.preventDefault();
            rateCard('easy');
            return;
          }

          // Hotkeys 5-9 switch pill tabs on Back card
          const tabMap = {
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
        const val = parseFloat(e.target.value);
        StorageManager.saveSettings({ speechRate: val });
        const label = document.getElementById('speech-rate-val-label');
        if (label) label.textContent = `${val.toFixed(2)}x`;
      });
    }

    // Subscribe to browser speech synthesis voices dynamically loaded
    if (typeof window !== 'undefined' && 'speechSynthesis' in window && window.speechSynthesis.onvoiceschanged !== undefined) {
      window.speechSynthesis.addEventListener('voiceschanged', () => {
        populateBrowserVoices();
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

    const audioFirstCheck = document.getElementById('toggle-audio-first');
    if (audioFirstCheck) {
      audioFirstCheck.addEventListener('change', (e) => {
        StorageManager.saveSettings({ audioFirstMode: e.target.checked });
        renderCurrentWord();
      });
    }

    const dailyLimitSelect = document.getElementById('daily-new-limit-select');
    if (dailyLimitSelect) {
      dailyLimitSelect.addEventListener('change', (e) => {
        changeDailyNewLimit(e.target.value);
      });
    }

    const thresholdSelect = document.getElementById('auto-advance-threshold-select');
    if (thresholdSelect) {
      thresholdSelect.addEventListener('change', (e) => {
        changeAutoAdvanceThreshold(e.target.value);
      });
    }
  }

  // Public App Interface
  return {
    async init() {
      initTheme();
      setupEventListeners();

      // Cross-Navigator & Server File Sync (data/user_progress.json)
      try {
        if (typeof StorageManager !== 'undefined' && typeof StorageManager.syncWithServer === 'function') {
          const syncRes = await StorageManager.syncWithServer();
          updateSyncStatusBadge(syncRes?.isConnected);
        }
      } catch (e) {
        updateSyncStatusBadge(false);
      }

      const urlParams = new URLSearchParams(window.location.search);
      const viewParam = urlParams.get('view');
      const savedSettings = StorageManager.getSettings();

      currentActiveView = viewParam || savedSettings.activeView || 'flashcard';
      studyMode = (currentActiveView === 'dictionary') ? 'browse' : 'flashcard';
      currentActiveTab = savedSettings.activeTab || 'sentences';
      if (currentActiveTab === 'synonyms') currentActiveTab = 'contrasts';
      currentLang = savedSettings.lang || 'both';

      if (viewParam) {
        document.body.classList.add(`standalone-window-${viewParam}`);
      }

      if (!savedSettings.toneColors) {
        document.body.classList.add('hide-tone-colors');
      }

      // Initialize TimeTracker
      if (typeof TimeTracker !== 'undefined') {
        TimeTracker.init({
          mode: currentActiveView,
          afkThresholdSeconds: savedSettings.afkThresholdSeconds || 120
        });
        TimeTracker.onTick((status) => updateTopBarTimePill(status));
        TimeTracker.onStatusChange((status) => {
          updateTopBarTimePill(status);
          broadcastSync('afk_changed', status);
        });
      }

      // Update view button active state
      document.querySelectorAll('.view-btn').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-view') === currentActiveView);
      });

      // Update language buttons
      document.querySelectorAll('.lang-btn').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-lang') === currentLang);
      });

      // Restore active filters
      activeChapterFilter = savedSettings.activeChapterFilter || 'all';
      activeStatusFilter = savedSettings.activeStatusFilter || 'all';

      // Load all chapters in parallel for unified global pool
      try {
        const loaded = await DataLoader.loadAllChapters();
        chapters = loaded.manifest;
        allChaptersData = loaded.chaptersMap;
      } catch (err) {
        console.error("Failed to load chapters:", err);
        chapters = [{ id: 1, dir: 'chapter_01', name: 'Chapter 1', title: '细节与人际关系', word_count: 38 }];
      }

      // Populate Chapter dropdowns
      ['chapter-select', 'settings-chapter-select'].forEach(selId => {
        const chapterSelect = document.getElementById(selId);
        if (chapterSelect) {
          chapterSelect.innerHTML = '';
          chapters.forEach(c => {
            const opt = document.createElement('option');
            opt.value = c.dir;
            opt.textContent = `${c.name}: ${c.title || c.dir} (${c.word_count} words)`;
            chapterSelect.appendChild(opt);
          });
        }
      });

      // Load initial chapter
      const requestedCh = urlParams.get('ch');
      let initialDir = chapters[0]?.dir || 'chapter_01';
      if (requestedCh) {
        const match = chapters.find(c => String(c.id) === requestedCh || c.dir === requestedCh);
        if (match) {
          initialDir = match.dir;
          activeChapterFilter = match.dir;
        }
      }

      currentChapter = chapters.find(c => c.dir === initialDir) || chapters[0];
      WORDS = allChaptersData[currentChapter.dir] || [];
      filteredWords = [...WORDS];

      const pillEl = document.getElementById('chapter-pill');
      if (pillEl) {
        pillEl.textContent = `CHP ${currentChapter.id}`;
      }

      // Check for active session snapshot
      const restored = StorageManager.getActiveSession();
      if (restored && !restored.expired && Array.isArray(restored.queue) && restored.queue.length > 0) {
        reviewQueue = restored.queue;
        queueIndex = Math.min(restored.currentIndex || 0, Math.max(0, reviewQueue.length - 1));
        if (restored.activeFilters) {
          activeChapterFilter = restored.activeFilters.chapter || 'all';
          activeStatusFilter = restored.activeFilters.status || 'all';
        }
        if (restored.frontierChapterId) {
          frontierChapter = restored.frontierChapterId;
        }
        showToast('✨ Resumed your active study session');
      } else {
        if (restored && restored.isNewDay && restored.promotedCardsCount > 0) {
          showToast(`🌅 New Day: ${restored.promotedCardsCount} unlearned card(s) promoted to today's reviews`);
        }
        buildReviewQueue();
      }

      // Add lifecycle listeners for persistent session saving
      if (typeof window !== 'undefined') {
        window.addEventListener('visibilitychange', () => {
          if (document.visibilityState === 'hidden') {
            persistActiveSession();
          }
        });
        window.addEventListener('pagehide', () => {
          persistActiveSession();
        });
        window.addEventListener('beforeunload', () => {
          persistActiveSession();
        });
      }

      renderCurrentWord();
      updateFilterPills();
    },

    getCurrentWord,
    showAnswer,
    rateCard,
    switchTab,
    cycleTab,
    speakActiveTabContent,
    toggleFlip,
    switchView,
    popoutCurrentView,
    setStudyMode,
    selectDictionaryWord,
    onDictSearchInput,
    clearDictSearch,
    setDictPosFilter,
    setDictStatusFilter,
    selectChapterFilter,
    selectStatusFilter,
    openWordInDictionary,
    changeAfkThreshold,
    exportStudyAnalytics,
    resetTimeTrackerPrompt,
    filterByReviewStatus,
    prevCard,
    nextCard,
    toggleFrontHint,
    togglePassagePinyin,
    copyText,
    clearSearch,
    openChapterPicker,
    toggleChapterPicker,
    undoLastAction,
    handleFrontHanziClick,
    unblurFrontHanzi,
    studySpecificChapter,
    setFrontierChapter,
    onBrowserSearch,
    filterBrowserStatus,
    openWordDetail,
    confirmResetWord,
    studySpecificWord,
    practiceLeeches,
    openBackupCodeModal,
    copyBackupCode,
    restoreFromBackupCode,
    closeModals,
    changeDailyNewLimit,
    changeAutoAdvanceThreshold,
    restartQueue() {
      clearAutoAdvanceTimer();
      sessionGoodCount = 0;
      sessionAgainCount = 0;
      buildReviewQueue();
      renderCurrentWord();
    },
    studyCurrentWord(id) {
      switchView('study');
      selectWordById(id);
    },
    openWordListDrawer,
    closeWordListDrawer,
    toggleWordListDrawer,
    openLookupDrawer,
    openSettingsDrawer,
    closeDrawers,
    toggleShortcutsModal,
    changeBrowserVoice,
    testBrowserVoice,
    populateBrowserVoices,
    exportBackupFile,
    handleImportBackup,
    updateSyncStatusBadge,
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
