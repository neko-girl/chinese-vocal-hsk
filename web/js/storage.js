/**
 * StorageManager - Handles local caching, two-stage spaced repetition system (SRS),
 * time tracking logs, study habits analytics, and character review timelines.
 */

const StorageManager = (function() {
  const REVIEW_KEY = 'hsk_review_store_v1';
  const REVIEW_KEY_V2 = 'hsk_review_store_v2';
  const SESSION_KEY_V2 = 'hsk_active_session_v2';
  const SETTINGS_KEY = 'hsk_study_settings_v1';
  const TIME_KEY = 'hsk_time_tracker_v1';
  const DB_NAME = 'chinese_vocal_db';
  const DB_VERSION = 1;

  // In-memory undo stack
  let undoMemoryStack = [];

  // IndexedDB asynchronous mirror & restoration helper
  let dbPromise = null;
  function getIndexedDB() {
    if (typeof window === 'undefined' || !window.indexedDB) return Promise.resolve(null);
    if (dbPromise) return dbPromise;
    dbPromise = new Promise((resolve) => {
      try {
        const req = window.indexedDB.open(DB_NAME, DB_VERSION);
        req.onupgradeneeded = (e) => {
          const db = e.target.result;
          if (!db.objectStoreNames.contains('srs_ledger')) {
            db.createObjectStore('srs_ledger', { keyPath: 'id' });
          }
          if (!db.objectStoreNames.contains('active_session')) {
            db.createObjectStore('active_session', { keyPath: 'id' });
          }
        };
        req.onsuccess = (e) => resolve(e.target.result);
        req.onerror = (e) => {
          console.warn('IndexedDB open error:', e);
          resolve(null);
        };
      } catch (err) {
        console.warn('IndexedDB unsupported:', err);
        resolve(null);
      }
    });
    return dbPromise;
  }

  async function mirrorToIndexedDB(storeName, data) {
    try {
      const db = await getIndexedDB();
      if (!db) return;
      const tx = db.transaction([storeName], 'readwrite');
      const store = tx.objectStore(storeName);
      store.put(data);
    } catch (e) {
      // Non-blocking mirror
    }
  }

  async function restoreFromIndexedDBIfEmpty() {
    if (typeof window === 'undefined') return;
    try {
      const localData = localStorage.getItem(REVIEW_KEY_V2) || localStorage.getItem(REVIEW_KEY);
      if (localData && localData !== '{}' && localData !== '{"wordsById":{}}') {
        return;
      }
      const db = await getIndexedDB();
      if (!db) return;
      const tx = db.transaction(['srs_ledger'], 'readonly');
      const store = tx.objectStore('srs_ledger');
      const req = store.get('main');
      req.onsuccess = () => {
        const result = req.result;
        if (result && result.wordsById && Object.keys(result.wordsById).length > 0) {
          const rebuilt = unflattenStore(result.wordsById);
          saveRawStore(rebuilt);
          if (typeof window !== 'undefined' && window.App && typeof window.App.renderCurrentWord === 'function') {
            window.App.renderCurrentWord();
          }
        }
      };
    } catch (e) {
      console.warn('Restore from IndexedDB failed:', e);
    }
  }

  // Trigger IndexedDB check on startup
  if (typeof window !== 'undefined') {
    setTimeout(restoreFromIndexedDBIfEmpty, 200);
  }

  function flattenWordsById(store) {
    const flat = {};
    if (!store || typeof store !== 'object') return flat;
    for (const ch of Object.keys(store)) {
      if (ch === 'schemaVersion' || ch === 'updatedAt' || ch === 'wordsById' || ch === 'chapters') continue;
      if (!store[ch] || typeof store[ch] !== 'object') continue;
      for (const wId of Object.keys(store[ch])) {
        const rec = store[ch][wId];
        if (rec) {
          flat[`${ch}_${wId}`] = rec;
        }
      }
    }
    return flat;
  }

  function unflattenStore(wordsById) {
    const store = {};
    if (!wordsById || typeof wordsById !== 'object') return store;
    for (const key of Object.keys(wordsById)) {
      const rec = wordsById[key];
      if (!rec) continue;
      const ch = rec.chapterId || (key.includes('_') ? key.substring(0, key.lastIndexOf('_')) : 'chapter_01');
      const wId = String(rec.wordId || (key.includes('_') ? key.substring(key.lastIndexOf('_') + 1) : key));
      if (!store[ch]) store[ch] = {};
      store[ch][wId] = rec;
    }
    return store;
  }

  // Spaced Repetition interval days based on Leitner/SRS levels (for legacy mapping)
  const SRS_INTERVAL_DAYS = [0, 1, 3, 7, 14, 30];
  const ONE_DAY_MS = 24 * 60 * 60 * 1000;

  function getTodayKey() {
    const d = new Date();
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  function randomFloat(min, max) {
    return Math.random() * (max - min) + min;
  }

  function intervalToSrsLevel(days) {
    if (days <= 0) return 0;
    if (days <= 1) return 1;
    if (days <= 3) return 2;
    if (days <= 7) return 3;
    if (days <= 14) return 4;
    return 5;
  }

  // Create default new card record
  function createNewCardRecord(chapterDir, wordId) {
    const now = Date.now();
    return {
      chapterId: chapterDir,
      wordId: String(wordId),
      state: 'new',
      step: 0,
      interval: 0,
      ease: 2.5,
      dueAt: now,
      lapses: 0,
      lastReviewedAt: null,
      postRelearnInterval: 1,
      reviews: 0,
      history: [],
      firstReviewed: null,
      status: 'new',
      srsLevel: 0,
      intervalDays: 0,
      dueDate: now,
      lastReviewed: null
    };
  }

  // Migrate legacy or raw record into standard 2-stage SRS model
  function migrateRecord(rec, chapterDir, wordId) {
    if (!rec || typeof rec !== 'object') {
      return createNewCardRecord(chapterDir, wordId);
    }

    const now = Date.now();

    // Already migrated to 2-stage schema
    if (rec.state && typeof rec.step === 'number' && typeof rec.interval === 'number' && typeof rec.ease === 'number') {
      rec.chapterId = rec.chapterId || chapterDir;
      rec.wordId = String(rec.wordId || wordId);
      rec.lapses = rec.lapses || 0;
      rec.ease = Math.max(1.3, rec.ease || 2.5);
      rec.dueAt = rec.dueAt || rec.dueDate || now;
      rec.lastReviewedAt = rec.lastReviewedAt ?? rec.lastReviewed ?? null;
      rec.postRelearnInterval = rec.postRelearnInterval || Math.max(1, Math.round((rec.interval || 1) * 0.25));

      // Synchronize legacy fields
      rec.status = (rec.state === 'review') ? 'remembered' : (rec.state === 'relearning' ? 'dont_remember' : (rec.state === 'learning' ? 'remembered' : 'new'));
      rec.dueDate = rec.dueAt;
      rec.intervalDays = rec.interval;
      rec.lastReviewed = rec.lastReviewedAt;
      rec.srsLevel = intervalToSrsLevel(rec.interval);
      return rec;
    }

    // Legacy migration
    const lapses = rec.lapses || (rec.status === 'dont_remember' ? 1 : 0);
    const reviews = rec.reviews || 0;
    const lastReviewedAt = rec.lastReviewed || (reviews > 0 ? now : null);
    const firstReviewed = rec.firstReviewed || lastReviewedAt;
    const history = Array.isArray(rec.history) ? rec.history : [];

    let state = 'new';
    let step = 0;
    let interval = 0;
    let ease = 2.5;
    let dueAt = now;
    let postRelearnInterval = 1;

    if (rec.status === 'remembered' && (rec.srsLevel > 0 || rec.intervalDays > 0)) {
      state = 'review';
      step = 1;
      interval = rec.intervalDays || SRS_INTERVAL_DAYS[rec.srsLevel || 1] || 1;
      dueAt = rec.dueDate || (now + interval * ONE_DAY_MS);
    } else if (rec.status === 'dont_remember' || (rec.srsLevel === 0 && reviews > 0)) {
      state = 'relearning';
      step = 0;
      interval = 0;
      dueAt = rec.dueDate || now;
      postRelearnInterval = Math.max(1, Math.round((rec.intervalDays || 1) * 0.25));
    }

    return {
      chapterId: chapterDir,
      wordId: String(wordId),
      state,
      step,
      interval,
      ease,
      dueAt,
      lapses,
      lastReviewedAt,
      postRelearnInterval,
      reviews,
      history,
      firstReviewed,
      status: (state === 'review') ? 'remembered' : (state === 'relearning' ? 'dont_remember' : 'new'),
      srsLevel: intervalToSrsLevel(interval),
      intervalDays: interval,
      dueDate: dueAt,
      lastReviewed: lastReviewedAt
    };
  }

  // Retrieve raw SRS review store and ensure migration to Schema v2
  function getRawStore() {
    try {
      let store = {};
      let needsSave = false;
      const v2Data = localStorage.getItem(REVIEW_KEY_V2);

      if (v2Data) {
        try {
          const parsed = JSON.parse(v2Data);
          if (parsed && parsed.wordsById && Object.keys(parsed.wordsById).length > 0) {
            store = unflattenStore(parsed.wordsById);
          } else if (parsed && parsed.chapters && typeof parsed.chapters === 'object') {
            store = parsed.chapters;
          }
        } catch (err) {
          console.warn('Error reading v2 store, checking v1:', err);
        }
      }

      if (Object.keys(store).length === 0) {
        const v1Data = localStorage.getItem(REVIEW_KEY);
        if (v1Data) {
          try {
            store = JSON.parse(v1Data) || {};
            needsSave = true; // Migrate to Schema v2
          } catch (err) {
            console.warn('Error reading v1 store:', err);
          }
        }
      }

      for (const chapterDir of Object.keys(store)) {
        if (chapterDir === 'schemaVersion' || chapterDir === 'updatedAt' || chapterDir === 'wordsById' || chapterDir === 'chapters') continue;
        if (!store[chapterDir] || typeof store[chapterDir] !== 'object') continue;
        for (const wordId of Object.keys(store[chapterDir])) {
          const raw = store[chapterDir][wordId];
          if (!raw.state || typeof raw.step !== 'number') {
            store[chapterDir][wordId] = migrateRecord(raw, chapterDir, wordId);
            needsSave = true;
          }
        }
      }

      if (needsSave) {
        saveRawStore(store);
      }
      return store;
    } catch (e) {
      console.warn('Failed to parse review cache from localStorage:', e);
      return {};
    }
  }

  // Save raw SRS review store to Schema v2 with dual-layer mirror
  function saveRawStore(store) {
    try {
      const flat = flattenWordsById(store);
      const envelopeV2 = {
        schemaVersion: 2,
        updatedAt: Date.now(),
        wordsById: flat,
        chapters: store
      };
      localStorage.setItem(REVIEW_KEY_V2, JSON.stringify(envelopeV2));
      localStorage.setItem(REVIEW_KEY, JSON.stringify(store));
      mirrorToIndexedDB('srs_ledger', { id: 'main', ...envelopeV2 });
    } catch (e) {
      console.warn('Failed to save review cache to localStorage:', e);
    }
  }

  // Retrieve raw time tracker store
  function getRawTimeStore() {
    try {
      const data = localStorage.getItem(TIME_KEY);
      if (data) {
        return JSON.parse(data);
      }
    } catch (e) {
      console.warn('Failed to parse time tracker cache:', e);
    }

    return {
      daily: {},          // { [dateKey]: { studySeconds, readingSeconds, reviewsCount, goodCount, againCount, hintPeeks, audioPlays, tabClicks: {} } }
      totalStudySeconds: 0,
      totalReadingSeconds: 0,
      totalReviews: 0,
      totalGood: 0,
      totalAgain: 0,
      chapters: {},       // { [chapterDir]: { studySeconds, readingSeconds, reviewsCount } }
      sessions: [],       // past session objects
      streak: {
        currentStreak: 0,
        longestStreak: 0,
        lastActiveDate: null
      }
    };
  }

  // Save raw time tracker store
  function saveRawTimeStore(store) {
    try {
      localStorage.setItem(TIME_KEY, JSON.stringify(store));
    } catch (e) {
      console.warn('Failed to save time tracker cache:', e);
    }
  }

  let syncTimer = null;
  function scheduleServerSync(delayMs = 2500) {
    if (typeof window === 'undefined' || !window.fetch) return;
    clearTimeout(syncTimer);
    syncTimer = setTimeout(() => {
      if (typeof StorageManager !== 'undefined' && typeof StorageManager.syncWithServer === 'function') {
        StorageManager.syncWithServer().catch(() => {});
      }
    }, delayMs);
  }

  // Update streak counter based on activity date
  function updateStreak(store, todayKey) {
    const streak = store.streak || { currentStreak: 0, longestStreak: 0, lastActiveDate: null };
    if (!streak.lastActiveDate) {
      streak.currentStreak = 1;
      streak.longestStreak = 1;
      streak.lastActiveDate = todayKey;
    } else if (streak.lastActiveDate !== todayKey) {
      const last = new Date(streak.lastActiveDate);
      const curr = new Date(todayKey);
      const diffDays = Math.round((curr - last) / (1000 * 60 * 60 * 24));

      if (diffDays === 1) {
        streak.currentStreak += 1;
      } else if (diffDays > 1) {
        streak.currentStreak = 1;
      }
      if (streak.currentStreak > streak.longestStreak) {
        streak.longestStreak = streak.currentStreak;
      }
      streak.lastActiveDate = todayKey;
    }
    store.streak = streak;
  }

  return {
    SRS_INTERVAL_DAYS,

    /**
     * Calculate next schedule according to 2-stage Spaced Repetition rules
     */
    calculateNextSchedule(cardRecord, rating, now = Date.now()) {
      const state = cardRecord.state || 'new';
      const step = typeof cardRecord.step === 'number' ? cardRecord.step : 0;
      let ease = typeof cardRecord.ease === 'number' ? cardRecord.ease : 2.5;
      const curInterval = cardRecord.interval || 0;
      let postRelearnInterval = cardRecord.postRelearnInterval || Math.max(1, Math.round(curInterval * 0.25));

      let nextState = state;
      let nextStep = step;
      let nextInterval = 0;
      let nextEase = ease;
      let nextDueAt = now;
      let reinsertOffset = null;
      let graduated = false;
      let lapsesDelta = 0;

      if (state === 'new') {
        if (rating === 'easy') {
          nextState = 'review';
          nextStep = 1;
          nextInterval = 3;
          nextDueAt = now + (3 * ONE_DAY_MS);
          reinsertOffset = null;
          graduated = true;
        } else if (rating === 'good') {
          nextState = 'learning';
          nextStep = 1;
          nextInterval = 0;
          nextDueAt = now;
          reinsertOffset = randomInt(8, 14);
          graduated = false;
        } else {
          // 'again' or 'hard'
          nextState = 'learning';
          nextStep = 0;
          nextInterval = 0;
          nextDueAt = now;
          reinsertOffset = randomInt(4, 6);
          graduated = false;
        }
      } else if (state === 'learning') {
        if (rating === 'easy') {
          nextState = 'review';
          nextStep = 1;
          nextInterval = 3;
          nextDueAt = now + (3 * ONE_DAY_MS);
          reinsertOffset = null;
          graduated = true;
        } else if (step === 0) {
          if (rating === 'good') {
            nextState = 'learning';
            nextStep = 1;
            nextInterval = 0;
            nextDueAt = now;
            reinsertOffset = randomInt(8, 14);
            graduated = false;
          } else {
            // 'again' or 'hard'
            nextState = 'learning';
            nextStep = 0;
            nextInterval = 0;
            nextDueAt = now;
            reinsertOffset = randomInt(4, 6);
            graduated = false;
          }
        } else {
          // step === 1
          if (rating === 'good') {
            nextState = 'review';
            nextStep = 1;
            nextInterval = 1;
            nextDueAt = now + ONE_DAY_MS;
            reinsertOffset = null;
            graduated = true;
          } else if (rating === 'hard') {
            nextState = 'learning';
            nextStep = 1;
            nextInterval = 0;
            nextDueAt = now;
            reinsertOffset = randomInt(5, 8);
            graduated = false;
          } else {
            // 'again' -> resets to step 0
            nextState = 'learning';
            nextStep = 0;
            nextInterval = 0;
            nextDueAt = now;
            reinsertOffset = randomInt(4, 6);
            graduated = false;
          }
        }
      } else if (state === 'review') {
        if (rating === 'again') {
          lapsesDelta = 1;
          nextEase = Math.max(1.3, ease - 0.20);
          postRelearnInterval = Math.max(1, Math.round(curInterval * 0.25));
          nextState = 'relearning';
          nextStep = 1;
          nextInterval = 0;
          nextDueAt = now;
          reinsertOffset = randomInt(6, 10);
          graduated = false;
        } else if (rating === 'hard') {
          nextEase = Math.max(1.3, ease - 0.15);
          nextInterval = Math.max(curInterval + 1, Math.round(curInterval * 1.2));
          nextState = 'review';
          nextStep = 1;
          nextDueAt = now + (nextInterval * ONE_DAY_MS);
          reinsertOffset = null;
          graduated = true;
        } else if (rating === 'good') {
          const fuzz = curInterval >= 3 ? randomFloat(0.9, 1.1) : 1.0;
          nextInterval = Math.max(curInterval + 1, Math.round(curInterval * ease * fuzz));
          nextState = 'review';
          nextStep = 1;
          nextDueAt = now + (nextInterval * ONE_DAY_MS);
          reinsertOffset = null;
          graduated = true;
        } else {
          // 'easy'
          nextEase = ease + 0.15;
          const fuzz = curInterval >= 3 ? randomFloat(0.9, 1.1) : 1.0;
          nextInterval = Math.max(curInterval + 2, Math.round(curInterval * nextEase * 1.3 * fuzz));
          nextState = 'review';
          nextStep = 1;
          nextDueAt = now + (nextInterval * ONE_DAY_MS);
          reinsertOffset = null;
          graduated = true;
        }
      } else if (state === 'relearning') {
        if (rating === 'again') {
          lapsesDelta = 1;
          nextEase = Math.max(1.3, ease - 0.20);
          nextState = 'relearning';
          nextStep = 0;
          nextInterval = 0;
          nextDueAt = now;
          reinsertOffset = randomInt(4, 6);
          graduated = false;
        } else if (rating === 'hard') {
          nextState = 'relearning';
          nextStep = 1;
          nextInterval = 0;
          nextDueAt = now;
          reinsertOffset = randomInt(5, 8);
          graduated = false;
        } else if (rating === 'good') {
          nextInterval = postRelearnInterval || 1;
          nextState = 'review';
          nextStep = 1;
          nextDueAt = now + (nextInterval * ONE_DAY_MS);
          reinsertOffset = null;
          graduated = true;
        } else {
          // 'easy'
          nextInterval = Math.max(2, Math.round((postRelearnInterval || 1) * 1.5));
          nextState = 'review';
          nextStep = 1;
          nextDueAt = now + (nextInterval * ONE_DAY_MS);
          reinsertOffset = null;
          graduated = true;
        }
      }

      return {
        nextState,
        nextStep,
        nextInterval,
        nextEase: Math.round(nextEase * 100) / 100,
        nextDueAt,
        reinsertOffset,
        graduated,
        lapsesDelta,
        postRelearnInterval
      };
    },

    /**
     * Generate predictive intervals and intra-session offsets for the 4 grading buttons
     */
    predictNextIntervals(cardRecord) {
      const state = cardRecord?.state || 'new';
      const step = cardRecord?.step || 0;
      const interval = cardRecord?.interval || 1;
      const ease = cardRecord?.ease || 2.5;
      const postRelearn = cardRecord?.postRelearnInterval || Math.max(1, Math.round(interval * 0.25));

      if (state === 'new') {
        return {
          again: { label: '~5 cards', desc: 'Repeat intra-session' },
          hard: { label: '~6 cards', desc: 'Repeat intra-session' },
          good: { label: '~10 cards', desc: 'Step 1 delayed check' },
          easy: { label: '3d', desc: 'Graduate immediately' }
        };
      }
      if (state === 'learning') {
        if (step === 0) {
          return {
            again: { label: '~5 cards', desc: 'Repeat intra-session' },
            hard: { label: '~6 cards', desc: 'Repeat intra-session' },
            good: { label: '~10 cards', desc: 'Advance to step 1' },
            easy: { label: '3d', desc: 'Graduate immediately' }
          };
        } else {
          return {
            again: { label: '~5 cards', desc: 'Reset to step 0' },
            hard: { label: '~6 cards', desc: 'Reset to step 0' },
            good: { label: '1d', desc: 'Graduate to Review' },
            easy: { label: '3d', desc: 'Graduate with boost' }
          };
        }
      }
      if (state === 'relearning') {
        return {
          again: { label: '~5 cards', desc: 'Repeat intra-session' },
          hard: { label: '~6 cards', desc: 'Repeat intra-session' },
          good: { label: `${postRelearn}d`, desc: 'Re-graduate to Review' },
          easy: { label: `${Math.max(2, Math.round(postRelearn * 1.5))}d`, desc: 'Bonus re-graduate' }
        };
      }
      // 'review' state
      const hardInt = Math.max(interval + 1, Math.round(interval * 1.2));
      const goodInt = Math.max(interval + 1, Math.round(interval * ease));
      const easyInt = Math.max(interval + 2, Math.round(interval * (ease + 0.15) * 1.3));

      return {
        again: { label: '~8 cards', desc: `Lapses +1, relearn ${Math.max(1, Math.round(interval * 0.25))}d` },
        hard: { label: `${hardInt}d`, desc: 'Ease reduced' },
        good: { label: `${goodInt}d`, desc: 'Normal interval' },
        easy: { label: `${easyInt}d`, desc: 'Ease bonus' }
      };
    },

    /**
     * Generate human-readable interval preview labels for UI buttons (legacy compatibility)
     */
    previewSchedule(cardRecord) {
      const state = cardRecord?.state || 'new';
      const step = cardRecord?.step || 0;
      const interval = cardRecord?.interval || 1;
      const ease = cardRecord?.ease || 2.5;
      const postRelearn = cardRecord?.postRelearnInterval || Math.max(1, Math.round(interval * 0.25));

      if (state === 'new') {
        return {
          again: '<10m',
          hard: '<15m',
          good: '<25m',
          easy: '3d'
        };
      }
      if (state === 'learning') {
        if (step === 0) {
          return {
            again: '<10m',
            hard: '<15m',
            good: '<25m',
            easy: '3d'
          };
        } else {
          return {
            again: '<10m',
            hard: '<15m',
            good: '1d',
            easy: '3d'
          };
        }
      }
      if (state === 'relearning') {
        return {
          again: '<10m',
          hard: '<15m',
          good: `${postRelearn}d`,
          easy: `${Math.max(2, Math.round(postRelearn * 1.5))}d`
        };
      }
      // 'review' state
      const hardInt = Math.max(interval + 1, Math.round(interval * 1.2));
      const goodInt = Math.max(interval + 1, Math.round(interval * ease));
      const easyInt = Math.max(interval + 2, Math.round(interval * (ease + 0.15) * 1.3));

      return {
        again: '<10m',
        hard: `${hardInt}d`,
        good: `${goodInt}d`,
        easy: `${easyInt}d`
      };
    },

    getTodayKey() {
      return getTodayKey();
    },

    /**
     * Get all review records for a specific chapter
     */
    getChapterReviews(chapterDir) {
      const store = getRawStore();
      return store[chapterDir] || {};
    },

    /**
     * Get review record for a specific word
     */
    getWordReview(chapterDir, wordId) {
      const chapterData = this.getChapterReviews(chapterDir);
      return chapterData[String(wordId)] || null;
    },

    /**
     * Record a review rating ('again', 'hard', 'good', 'easy')
     */
    recordReview(chapterDir, wordId, ratingOrStatus) {
      let rating = ratingOrStatus;
      if (rating === 'remembered') rating = 'good';
      if (rating === 'dont_remember') rating = 'again';
      if (!['again', 'hard', 'good', 'easy'].includes(rating)) {
        rating = 'good';
      }

      const store = getRawStore();
      if (!store[chapterDir]) {
        store[chapterDir] = {};
      }

      const idStr = String(wordId);
      const existing = store[chapterDir][idStr]
        ? migrateRecord(store[chapterDir][idStr], chapterDir, idStr)
        : createNewCardRecord(chapterDir, idStr);

      const now = Date.now();
      const schedule = this.calculateNextSchedule(existing, rating, now);

      existing.reviews = (existing.reviews || 0) + 1;
      existing.lastReviewedAt = now;
      existing.lastReviewed = now;
      if (!existing.firstReviewed) existing.firstReviewed = now;

      existing.state = schedule.nextState;
      existing.step = schedule.nextStep;
      existing.interval = schedule.nextInterval;
      existing.ease = schedule.nextEase;
      existing.dueAt = schedule.nextDueAt;
      existing.dueDate = schedule.nextDueAt;
      existing.intervalDays = schedule.nextInterval;
      existing.srsLevel = intervalToSrsLevel(schedule.nextInterval);

      if (schedule.lapsesDelta) {
        existing.lapses = (existing.lapses || 0) + schedule.lapsesDelta;
      }
      if (schedule.postRelearnInterval) {
        existing.postRelearnInterval = schedule.postRelearnInterval;
      }

      // Synchronize legacy status
      existing.status = (existing.state === 'review')
        ? 'remembered'
        : (existing.state === 'relearning' ? 'dont_remember' : (existing.state === 'learning' ? 'learning' : 'new'));

      if (!Array.isArray(existing.history)) {
        existing.history = [];
      }
      existing.history.push({
        t: now,
        result: rating,
        state: existing.state,
        step: existing.step,
        interval: existing.interval,
        ease: existing.ease
      });
      if (existing.history.length > 30) {
        existing.history.shift();
      }

      store[chapterDir][idStr] = existing;
      saveRawStore(store);
      scheduleServerSync();

      // Log study event to time tracker / analytics
      this.recordStudyEvent('card_grade', {
        status: rating === 'again' ? 'dont_remember' : 'remembered',
        rating,
        wordId,
        chapterDir,
        srsLevel: existing.srsLevel
      });

      return {
        record: existing,
        reinsertOffset: schedule.reinsertOffset,
        graduated: schedule.graduated
      };
    },

    /**
     * Check if a word is due for review
     */
    isDue(reviewItem, now = Date.now()) {
      if (!reviewItem) return true; // New words are due
      if (reviewItem.state === 'new') return true;
      if (reviewItem.state === 'learning' || reviewItem.state === 'relearning') return true;
      if (!reviewItem.dueAt && !reviewItem.dueDate) return true;
      const dueTimestamp = reviewItem.dueAt || reviewItem.dueDate;
      return dueTimestamp <= now;
    },

    /**
     * Get aggregated chapter statistics
     */
    getChapterStats(chapterDir, words = []) {
      const reviews = this.getChapterReviews(chapterDir);
      const total = words.length;
      let remembered = 0;
      let dontRemember = 0;
      let learningCount = 0;
      let unreviewed = 0;
      let dueCount = 0;
      let mastered = 0;

      const now = Date.now();

      words.forEach(w => {
        const rev = reviews[String(w.id)];
        if (!rev || rev.state === 'new') {
          unreviewed++;
          dueCount++;
        } else {
          if (rev.state === 'review') remembered++;
          if (rev.state === 'learning' || rev.state === 'relearning') learningCount++;
          if (rev.lapses > 0 || rev.state === 'relearning') dontRemember++;
          if (this.isDue(rev, now)) dueCount++;
          if (rev.interval >= 14 || rev.srsLevel >= 4) mastered++;
        }
      });

      const percent = total > 0 ? Math.round((remembered / total) * 100) : 0;
      return {
        total,
        remembered,
        dontRemember,
        learningCount,
        unreviewed,
        dueCount,
        mastered,
        percent
      };
    },

    /**
     * Get user's current frontier chapter (starting at chapter_01)
     */
    getFrontierChapter() {
      const settings = this.getSettings();
      return settings.frontierChapter || 'chapter_01';
    },

    /**
     * Set user's current frontier chapter
     */
    setFrontierChapter(chapterDir) {
      return this.saveSettings({ frontierChapter: chapterDir });
    },

    /**
     * Get dictionary of all records across all chapters keyed by "chapterDir:wordId"
     */
    getAllCardsRecordMap() {
      const store = getRawStore();
      const map = {};
      for (const [chDir, words] of Object.entries(store)) {
        if (words && typeof words === 'object') {
          for (const [wId, rec] of Object.entries(words)) {
            map[`${chDir}:${wId}`] = rec;
          }
        }
      }
      return map;
    },

    /**
     * Character Review & Lapse Timeline Data Extraction
     * Separates words into:
     * 1. High-lapse characters (repeated due to lapses, with individual event history)
     * 2. Smooth-progress characters (no lapses, grouped into consolidated milestones)
     * 3. Unreviewed characters
     */
    getCharacterTimelineData(chapterDir, words = []) {
      const reviews = this.getChapterReviews(chapterDir);

      const highLapseWords = [];
      const smoothWords = [];
      let unreviewedCount = 0;

      words.forEach(w => {
        const rev = reviews[String(w.id)];
        if (!rev || rev.reviews === 0) {
          unreviewedCount++;
          return;
        }

        const lapses = rev.lapses || 0;
        const history = Array.isArray(rev.history) ? rev.history : [];

        if (lapses > 0 || rev.status === 'dont_remember') {
          // Problem character: repeatedly reviewed due to lapses
          highLapseWords.push({
            word: w,
            reviewItem: rev,
            lapses,
            reviews: rev.reviews || 0,
            srsLevel: rev.srsLevel || 0,
            status: rev.status,
            lastReviewed: rev.lastReviewed || rev.dueDate || 0,
            history
          });
        } else {
          // Smooth progression without lapses
          smoothWords.push({
            word: w,
            reviewItem: rev,
            reviews: rev.reviews || 0,
            srsLevel: rev.srsLevel || 0,
            status: rev.status,
            history
          });
        }
      });

      // Sort high lapse words: highest lapses first, then highest reviews
      highLapseWords.sort((a, b) => {
        if (b.lapses !== a.lapses) return b.lapses - a.lapses;
        return b.reviews - a.reviews;
      });

      // Group smooth progress words by SRS Level
      const smoothGroups = {};
      smoothWords.forEach(item => {
        const lvl = item.srsLevel;
        if (!smoothGroups[lvl]) {
          smoothGroups[lvl] = { level: lvl, count: 0, words: [] };
        }
        smoothGroups[lvl].count++;
        smoothGroups[lvl].words.push(item);
      });

      return {
        highLapseWords,
        smoothWords,
        smoothGroups,
        unreviewedCount,
        totalReviewed: highLapseWords.length + smoothWords.length,
        totalWords: words.length
      };
    },

    /**
     * Reset review cache for a chapter
     */
    resetChapter(chapterDir) {
      const store = getRawStore();
      delete store[chapterDir];
      saveRawStore(store);
    },

    // -------------------------------------------------------------
    // Time Tracker & Study Behavior Analytics Persistence
    // -------------------------------------------------------------

    /**
     * Accumulate active seconds (study vs reading)
     */
    recordActiveTime(studySeconds = 0, readingSeconds = 0, mode = 'flashcard', chapterDir = null) {
      if (studySeconds <= 0 && readingSeconds <= 0) return;

      const store = getRawTimeStore();
      const todayKey = getTodayKey();

      if (!store.daily[todayKey]) {
        store.daily[todayKey] = {
          studySeconds: 0,
          readingSeconds: 0,
          reviewsCount: 0,
          goodCount: 0,
          againCount: 0,
          hintPeeks: 0,
          audioPlays: 0,
          tabClicks: {}
        };
      }

      store.daily[todayKey].studySeconds += studySeconds;
      store.daily[todayKey].readingSeconds += readingSeconds;

      store.totalStudySeconds = (store.totalStudySeconds || 0) + studySeconds;
      store.totalReadingSeconds = (store.totalReadingSeconds || 0) + readingSeconds;

      if (chapterDir) {
        if (!store.chapters[chapterDir]) {
          store.chapters[chapterDir] = { studySeconds: 0, readingSeconds: 0, reviewsCount: 0 };
        }
        store.chapters[chapterDir].studySeconds += studySeconds;
        store.chapters[chapterDir].readingSeconds += readingSeconds;
      }

      updateStreak(store, todayKey);
      saveRawTimeStore(store);
      scheduleServerSync();
    },

    /**
     * Record a specific study interaction event
     */
    recordStudyEvent(eventType, payload = {}) {
      const store = getRawTimeStore();
      const todayKey = getTodayKey();

      if (!store.daily[todayKey]) {
        store.daily[todayKey] = {
          studySeconds: 0,
          readingSeconds: 0,
          reviewsCount: 0,
          goodCount: 0,
          againCount: 0,
          hintPeeks: 0,
          audioPlays: 0,
          tabClicks: {}
        };
      }

      const today = store.daily[todayKey];

      if (eventType === 'card_grade') {
        today.reviewsCount = (today.reviewsCount || 0) + 1;
        store.totalReviews = (store.totalReviews || 0) + 1;

        if (payload.status === 'remembered') {
          today.goodCount = (today.goodCount || 0) + 1;
          store.totalGood = (store.totalGood || 0) + 1;
        } else {
          today.againCount = (today.againCount || 0) + 1;
          store.totalAgain = (store.totalAgain || 0) + 1;
        }

        if (payload.chapterDir) {
          if (!store.chapters[payload.chapterDir]) {
            store.chapters[payload.chapterDir] = { studySeconds: 0, readingSeconds: 0, reviewsCount: 0 };
          }
          store.chapters[payload.chapterDir].reviewsCount = (store.chapters[payload.chapterDir].reviewsCount || 0) + 1;
        }
      } else if (eventType === 'hint_peek') {
        today.hintPeeks = (today.hintPeeks || 0) + 1;
      } else if (eventType === 'audio_play') {
        today.audioPlays = (today.audioPlays || 0) + 1;
      } else if (eventType === 'tab_view') {
        const tab = payload.tab || 'sentences';
        today.tabClicks[tab] = (today.tabClicks[tab] || 0) + 1;
      }

      updateStreak(store, todayKey);
      saveRawTimeStore(store);
      scheduleServerSync();
    },

    /**
     * Get active time for today
     */
    getTimeStatsToday() {
      const store = getRawTimeStore();
      const todayKey = getTodayKey();
      const today = store.daily[todayKey] || { studySeconds: 0, readingSeconds: 0, reviewsCount: 0 };
      return {
        date: todayKey,
        studySeconds: today.studySeconds || 0,
        readingSeconds: today.readingSeconds || 0,
        reviewsCount: today.reviewsCount || 0,
        goodCount: today.goodCount || 0,
        againCount: today.againCount || 0,
        hintPeeks: today.hintPeeks || 0,
        audioPlays: today.audioPlays || 0
      };
    },

    /**
     * Get all-time time totals
     */
    getTimeStatsAllTime() {
      const store = getRawTimeStore();
      return {
        totalStudySeconds: store.totalStudySeconds || 0,
        totalReadingSeconds: store.totalReadingSeconds || 0,
        totalSeconds: (store.totalStudySeconds || 0) + (store.totalReadingSeconds || 0),
        totalReviews: store.totalReviews || 0,
        totalGood: store.totalGood || 0,
        totalAgain: store.totalAgain || 0,
        streak: store.streak || { currentStreak: 0, longestStreak: 0 }
      };
    },

    /**
     * Get daily activity breakdown for the last N days
     */
    getDailyActivityHistory(days = 14) {
      const store = getRawTimeStore();
      const result = [];
      const today = new Date();

      for (let i = days - 1; i >= 0; i--) {
        const d = new Date(today);
        d.setDate(d.getDate() - i);
        const y = d.getFullYear();
        const m = String(d.getMonth() + 1).padStart(2, '0');
        const dayStr = String(d.getDate()).padStart(2, '0');
        const key = `${y}-${m}-${dayStr}`;

        const entry = store.daily[key] || {
          studySeconds: 0,
          readingSeconds: 0,
          reviewsCount: 0,
          goodCount: 0,
          againCount: 0
        };

        result.push({
          date: key,
          label: `${m}/${dayStr}`,
          dayOfWeek: d.toLocaleDateString('en-US', { weekday: 'short' }),
          studySeconds: entry.studySeconds || 0,
          readingSeconds: entry.readingSeconds || 0,
          totalSeconds: (entry.studySeconds || 0) + (entry.readingSeconds || 0),
          reviewsCount: entry.reviewsCount || 0,
          goodCount: entry.goodCount || 0,
          againCount: entry.againCount || 0
        });
      }

      return result;
    },

    /**
     * Calculate comprehensive study behavior & habits summary
     */
    getStudyHabitsSummary() {
      const store = getRawTimeStore();
      const totals = this.getTimeStatsAllTime();

      let totalReviews = totals.totalReviews;
      let totalGood = totals.totalGood;
      let totalAgain = totals.totalAgain;
      let totalHintPeeks = 0;
      let totalAudioPlays = 0;
      const aggregatedTabs = {
        sentences: 0,
        collocations: 0,
        idioms: 0,
        decomposition: 0,
        mnemonics: 0,
        contrasts: 0,
        traps: 0,
        passages: 0
      };

      Object.values(store.daily || {}).forEach(day => {
        totalHintPeeks += day.hintPeeks || 0;
        totalAudioPlays += day.audioPlays || 0;
        if (day.tabClicks) {
          Object.entries(day.tabClicks).forEach(([tab, count]) => {
            aggregatedTabs[tab] = (aggregatedTabs[tab] || 0) + count;
          });
        }
      });

      const retentionRate = totalReviews > 0 ? Math.round((totalGood / totalReviews) * 100) : 0;
      const hintRate = totalReviews > 0 ? Math.round((totalHintPeeks / totalReviews) * 100) : 0;
      const avgCardSeconds = totalReviews > 0 ? Math.round(totals.totalStudySeconds / totalReviews) : 0;

      return {
        totalReviews,
        totalGood,
        totalAgain,
        retentionRate,
        hintRate,
        totalHintPeeks,
        totalAudioPlays,
        avgCardSeconds,
        tabClicks: aggregatedTabs,
        streak: store.streak || { currentStreak: 0, longestStreak: 0 },
        chapters: store.chapters || {}
      };
    },

    /**
     * Log completed session
     */
    logSession(session) {
      const store = getRawTimeStore();
      if (!Array.isArray(store.sessions)) {
        store.sessions = [];
      }
      store.sessions.unshift({
        id: Date.now(),
        timestamp: Date.now(),
        date: getTodayKey(),
        mode: session.mode || 'flashcard',
        durationSeconds: session.durationSeconds || 0,
        chapterDir: session.chapterDir || '',
        reviewsCount: session.reviewsCount || 0,
        accuracy: session.accuracy || 0
      });

      // Keep last 30 sessions
      if (store.sessions.length > 30) {
        store.sessions.pop();
      }

      saveRawTimeStore(store);
    },

    /**
     * Get recent sessions
     */
    getRecentSessions(limit = 10) {
      const store = getRawTimeStore();
      return (store.sessions || []).slice(0, limit);
    },

    /**
     * Reset time tracker data
     */
    resetTimeTrackerData() {
      localStorage.removeItem(TIME_KEY);
    },

    /**
     * Export all user progress and analytics as a JSON object
     */
    exportAllData() {
      return {
        version: '1.2.0',
        exportedAt: new Date().toISOString(),
        reviews: getRawStore(),
        timeTracking: getRawTimeStore(),
        settings: this.getSettings()
      };
    },

    /**
     * Get user study preferences
     */
    getSettings() {
      const defaults = {
        activeView: 'flashcard', // 'flashcard' | 'dictionary' | 'stats'
        studyMode: 'flashcard',  // 'flashcard' or 'browse'
        autoAudio: true,         // speak headword on answer reveal
        toneColors: true,        // dynamic pinyin tone coloring
        speechRate: 0.9,         // speech rate (0.75 - 1.2)
        studyOrder: 'order',     // 'order' or 'shuffle'
        activeTab: 'sentences',  // default active pill tab
        filter: 'all',           // 'all', 'due', 'lapses', 'remembered', 'new'
        lang: localStorage.getItem('hsk_lang') || 'both',
        preferredVoice: 'random',// 'random', 'mature_woman', 'soothing_host', 'office_man', 'tender_ceo', 'alternate'
        autoAdvanceChapter: true,// auto-start next chapter when finished
        autoAdvanceDelay: 5,     // countdown seconds before auto-advance
        soundFx: true,           // soft UI audio feedback
        showPassagePinyin: false,// reading passage pinyin visibility toggle
        afkThresholdSeconds: 120,// AFK inactivity threshold in seconds (default 2 min)
        browserVoiceURI: '',     // Browser TTS Voice (empty string = auto-detect best neural)
        activeChapterFilter: 'all', // 'all' (All Active Chapters) | 'chapter_01' .. 'chapter_08'
        activeStatusFilter: 'all',  // 'all' (Smart Mix 3:1) | 'due' | 'new' | 'learning'
        frontierChapter: 'chapter_01', // Current active frontier chapter
        audioFirstMode: false,   // Listening mode: blur front Hanzi and autoplay audio
        dailyNewLimit: 20,       // Daily new card limit (0 = unlimited)
        autoAdvanceThreshold: 5, // Auto-advance chapter when < 5 unlearned cards remain
        lastBackTab: 'sentences' // Sticky pill-tab memory across cards
      };

      try {
        const saved = localStorage.getItem(SETTINGS_KEY);
        return saved ? { ...defaults, ...JSON.parse(saved) } : defaults;
      } catch (e) {
        return defaults;
      }
    },

    /**
     * Update user study preferences
     */
    saveSettings(patch) {
      const current = this.getSettings();
      const updated = { ...current, ...patch };
      try {
        localStorage.setItem(SETTINGS_KEY, JSON.stringify(updated));
        scheduleServerSync();
      } catch (e) {
        console.warn('Failed to save study settings:', e);
      }
      return updated;
    },

    /**
     * Import and intelligently merge external user progress
     */
    importAllData(payload) {
      if (!payload || typeof payload !== 'object') return false;
      try {
        if (payload.reviews && typeof payload.reviews === 'object') {
          const currentStore = getRawStore();
          for (const [chDir, wordsMap] of Object.entries(payload.reviews)) {
            if (!currentStore[chDir]) {
              currentStore[chDir] = { ...wordsMap };
            } else {
              for (const [wId, revData] of Object.entries(wordsMap)) {
                const migratedIncoming = migrateRecord(revData, chDir, wId);
                const existing = currentStore[chDir][wId];
                if (!existing) {
                  currentStore[chDir][wId] = migratedIncoming;
                } else {
                  const incomingCount = migratedIncoming.reviews || 0;
                  const existingCount = existing.reviews || 0;
                  const incomingDate = migratedIncoming.lastReviewedAt || migratedIncoming.dueAt || 0;
                  const existingDate = existing.lastReviewedAt || existing.dueAt || 0;

                  if (incomingCount > existingCount || (incomingCount === existingCount && incomingDate > existingDate)) {
                    currentStore[chDir][wId] = migratedIncoming;
                  }
                }
              }
            }
          }
          saveRawStore(currentStore);
        }

        if (payload.timeTracking && typeof payload.timeTracking === 'object') {
          const currentT = getRawTimeStore();
          const incoming = payload.timeTracking;

          currentT.daily = { ...(incoming.daily || {}), ...(currentT.daily || {}) };
          currentT.totalStudySeconds = Math.max(currentT.totalStudySeconds || 0, incoming.totalStudySeconds || 0);
          currentT.totalReadingSeconds = Math.max(currentT.totalReadingSeconds || 0, incoming.totalReadingSeconds || 0);
          currentT.totalReviews = Math.max(currentT.totalReviews || 0, incoming.totalReviews || 0);
          currentT.totalGood = Math.max(currentT.totalGood || 0, incoming.totalGood || 0);
          currentT.totalAgain = Math.max(currentT.totalAgain || 0, incoming.totalAgain || 0);

          if (incoming.chapters) {
            currentT.chapters = { ...(incoming.chapters || {}), ...(currentT.chapters || {}) };
          }
          if (incoming.streak) {
            currentT.streak = {
              currentStreak: Math.max(currentT.streak?.currentStreak || 0, incoming.streak.currentStreak || 0),
              longestStreak: Math.max(currentT.streak?.longestStreak || 0, incoming.streak.longestStreak || 0),
              lastActiveDate: currentT.streak?.lastActiveDate || incoming.streak.lastActiveDate
            };
          }
          if (Array.isArray(incoming.sessions) && incoming.sessions.length) {
            const seen = new Set((currentT.sessions || []).map(s => s.startTime));
            const merged = [...(currentT.sessions || [])];
            incoming.sessions.forEach(s => {
              if (s && s.startTime && !seen.has(s.startTime)) {
                merged.push(s);
                seen.add(s.startTime);
              }
            });
            merged.sort((a, b) => (b.startTime || 0) - (a.startTime || 0));
            currentT.sessions = merged.slice(0, 50);
          }

          saveRawTimeStore(currentT);
        }

        if (payload.settings && typeof payload.settings === 'object') {
          this.saveSettings(payload.settings);
        }

        if (payload.activeSession && typeof payload.activeSession === 'object') {
          this.saveActiveSession(payload.activeSession);
        }

        return true;
      } catch (err) {
        console.warn('Failed to import user progress:', err);
        return false;
      }
    },

    /**
     * Reset review record for a specific word back to new state
     */
    resetWordReview(chapterDir, wordId) {
      const store = getRawStore();
      if (!store[chapterDir]) store[chapterDir] = {};
      store[chapterDir][String(wordId)] = createNewCardRecord(chapterDir, String(wordId));
      saveRawStore(store);
      return true;
    },

    /**
     * Save active study session snapshot to localStorage and mirror to IndexedDB
     */
    saveActiveSession(sessionData) {
      if (!sessionData || typeof sessionData !== 'object') return;
      const snapshot = {
        queue: Array.isArray(sessionData.queue) ? sessionData.queue : [],
        currentIndex: typeof sessionData.currentIndex === 'number' ? sessionData.currentIndex : 0,
        activeFilters: sessionData.activeFilters || { chapter: 'all', status: 'all' },
        frontierChapterId: sessionData.frontierChapterId || 'chapter_01',
        undoStack: Array.isArray(sessionData.undoStack) ? sessionData.undoStack.slice(-20) : [],
        startedAt: sessionData.startedAt || Date.now(),
        lastActiveDate: sessionData.lastActiveDate || getTodayKey(),
        updatedAt: Date.now()
      };
      try {
        localStorage.setItem(SESSION_KEY_V2, JSON.stringify(snapshot));
      } catch (e) {
        console.warn('Failed to save session snapshot to localStorage:', e);
      }
      mirrorToIndexedDB('active_session', { id: 'current', ...snapshot });
    },

    /**
     * Retrieve active session snapshot. If from a previous calendar day, expires snapshot
     * and promotes unfinished intra-session learning cards to the top of today's queue.
     */
    getActiveSession() {
      try {
        const raw = localStorage.getItem(SESSION_KEY_V2);
        if (!raw) return null;
        const session = JSON.parse(raw);
        if (!session || typeof session !== 'object') return null;

        const today = getTodayKey();
        if (session.lastActiveDate && session.lastActiveDate !== today) {
          // Calendar day rollover: promote unfinished learning cards & clear snapshot
          const promoted = this.promoteUnfinishedLearningCards();
          this.clearActiveSession();
          return {
            expired: true,
            isNewDay: true,
            previousDate: session.lastActiveDate,
            promotedCardsCount: promoted
          };
        }
        return session;
      } catch (e) {
        console.warn('Failed to retrieve active session:', e);
        return null;
      }
    },

    /**
     * Clear active session snapshot
     */
    clearActiveSession() {
      try {
        localStorage.removeItem(SESSION_KEY_V2);
      } catch (e) {}
      mirrorToIndexedDB('active_session', { id: 'current', cleared: true, updatedAt: Date.now() });
    },

    /**
     * Promote any unfinished learning/relearning cards to due immediately
     */
    promoteUnfinishedLearningCards() {
      const store = getRawStore();
      let count = 0;
      const now = Date.now();
      for (const ch of Object.keys(store)) {
        if (ch === 'schemaVersion' || ch === 'updatedAt' || ch === 'wordsById' || ch === 'chapters') continue;
        if (!store[ch] || typeof store[ch] !== 'object') continue;
        for (const wId of Object.keys(store[ch])) {
          const rec = store[ch][wId];
          if (rec && (rec.state === 'learning' || rec.state === 'relearning')) {
            rec.dueAt = now - 60000;
            rec.dueDate = rec.dueAt;
            count++;
          }
        }
      }
      if (count > 0) {
        saveRawStore(store);
      }
      return count;
    },

    /**
     * Push action onto the undo stack (max 20 entries)
     */
    pushUndo(entry) {
      if (!entry || !entry.chapterId || !entry.wordId) return;
      const currentStack = undoMemoryStack;
      currentStack.push({
        wordId: String(entry.wordId),
        chapterId: entry.chapterId,
        prevRecord: entry.prevRecord ? JSON.parse(JSON.stringify(entry.prevRecord)) : null,
        prevQueue: Array.isArray(entry.prevQueue) ? JSON.parse(JSON.stringify(entry.prevQueue)) : [],
        prevIndex: typeof entry.prevIndex === 'number' ? entry.prevIndex : 0,
        timestamp: Date.now()
      });
      if (currentStack.length > 20) currentStack.shift();
      undoMemoryStack = currentStack;

      const session = this.getActiveSession();
      if (session && !session.expired) {
        session.undoStack = currentStack;
        this.saveActiveSession(session);
      }
    },

    /**
     * Pop the last action from the undo stack and restore state
     */
    popUndo() {
      if (!undoMemoryStack.length) {
        const session = this.getActiveSession();
        if (session && Array.isArray(session.undoStack) && session.undoStack.length) {
          undoMemoryStack = session.undoStack;
        }
      }
      if (!undoMemoryStack.length) return null;

      const entry = undoMemoryStack.pop();

      // Restore word record in review store
      if (entry && entry.chapterId && entry.wordId && entry.prevRecord) {
        const store = getRawStore();
        if (!store[entry.chapterId]) store[entry.chapterId] = {};
        store[entry.chapterId][String(entry.wordId)] = entry.prevRecord;
        saveRawStore(store);
      }

      // Update active session snapshot
      const session = this.getActiveSession();
      if (session && !session.expired) {
        session.undoStack = undoMemoryStack;
        if (Array.isArray(entry.prevQueue) && entry.prevQueue.length) {
          session.queue = entry.prevQueue;
          session.currentIndex = entry.prevIndex;
        }
        this.saveActiveSession(session);
      }

      return entry;
    },

    canUndo() {
      if (undoMemoryStack.length > 0) return true;
      const session = this.getActiveSession();
      return !!(session && Array.isArray(session.undoStack) && session.undoStack.length > 0);
    },

    clearUndo() {
      undoMemoryStack = [];
      const session = this.getActiveSession();
      if (session && !session.expired) {
        session.undoStack = [];
        this.saveActiveSession(session);
      }
    },

    /**
     * Get review distribution forecast for the next 7 days (Today .. +6 days)
     */
    getForecast7Days() {
      const store = getRawStore();
      const days = [];
      const now = new Date();
      const startOfToday = new Date(now.getFullYear(), now.getMonth(), now.getDate()).getTime();
      const ONE_DAY = 24 * 60 * 60 * 1000;

      for (let i = 0; i < 7; i++) {
        const dayStart = startOfToday + i * ONE_DAY;
        const dateObj = new Date(dayStart);
        const dayLabel = i === 0 ? 'Today' : i === 1 ? 'Tomorrow' : dateObj.toLocaleDateString(undefined, { weekday: 'short' });
        const dateStr = `${dateObj.getMonth() + 1}/${dateObj.getDate()}`;
        days.push({
          dayOffset: i,
          dayLabel,
          dateStr,
          count: 0
        });
      }

      for (const ch of Object.keys(store)) {
        if (ch === 'schemaVersion' || ch === 'updatedAt' || ch === 'wordsById' || ch === 'chapters') continue;
        if (!store[ch] || typeof store[ch] !== 'object') continue;
        for (const wId of Object.keys(store[ch])) {
          const rec = store[ch][wId];
          if (!rec || rec.state === 'new') continue;
          const due = rec.dueAt || rec.dueDate || 0;
          if (due <= startOfToday + ONE_DAY - 1) {
            days[0].count++;
          } else {
            const offset = Math.floor((due - startOfToday) / ONE_DAY);
            if (offset >= 1 && offset < 7) {
              days[offset].count++;
            }
          }
        }
      }

      return days;
    },

    /**
     * Get words with the highest lapses (Leech List)
     */
    getLeechWords(limit = 10) {
      const store = getRawStore();
      const leeches = [];
      for (const ch of Object.keys(store)) {
        if (ch === 'schemaVersion' || ch === 'updatedAt' || ch === 'wordsById' || ch === 'chapters') continue;
        if (!store[ch] || typeof store[ch] !== 'object') continue;
        for (const wId of Object.keys(store[ch])) {
          const rec = store[ch][wId];
          if (rec && (rec.lapses || 0) > 0) {
            leeches.push(rec);
          }
        }
      }
      leeches.sort((a, b) => (b.lapses || 0) - (a.lapses || 0));
      return leeches.slice(0, limit);
    },

    /**
     * Export complete user data as formatted JSON
     */
    exportBackupJson() {
      const full = this.exportAllData();
      const session = this.getActiveSession();
      return JSON.stringify({
        schemaVersion: 2,
        exportedAt: new Date().toISOString(),
        ...full,
        activeSession: session
      }, null, 2);
    },

    /**
     * Import user data from JSON string or object
     */
    importBackupJson(payload) {
      try {
        const obj = (typeof payload === 'string') ? JSON.parse(payload) : payload;
        return this.importAllData(obj);
      } catch (e) {
        console.warn('Invalid backup JSON:', e);
        return false;
      }
    },

    /**
     * Export backup as compact Base64 code for cross-device copy-paste
     */
    exportBackupCode() {
      const jsonStr = this.exportBackupJson();
      if (typeof btoa !== 'undefined') {
        const encoded = btoa(unescape(encodeURIComponent(jsonStr)));
        return `HSK_V2:${encoded}`;
      } else if (typeof Buffer !== 'undefined') {
        return `HSK_V2:${Buffer.from(jsonStr, 'utf-8').toString('base64')}`;
      }
      return jsonStr;
    },

    /**
     * Import backup from Base64 code
     */
    importBackupCode(code) {
      try {
        if (!code || typeof code !== 'string') return false;
        let base64 = code.trim();
        if (base64.startsWith('HSK_V2:')) {
          base64 = base64.slice('HSK_V2:'.length);
        }
        let jsonStr = '';
        if (typeof atob !== 'undefined') {
          jsonStr = decodeURIComponent(escape(atob(base64)));
        } else if (typeof Buffer !== 'undefined') {
          jsonStr = Buffer.from(base64, 'base64').toString('utf-8');
        }
        return this.importBackupJson(jsonStr);
      } catch (e) {
        console.warn('Import backup code failed:', e);
        return false;
      }
    },

    /**
     * Cross-Navigator Server Sync
     * Synchronizes progress with the local server (/api/sync) backed by data/user_progress.json
     */
    async syncWithServer() {
      if (typeof window === 'undefined' || !window.fetch) return { success: false, reason: 'no-fetch' };
      try {
        const resp = await fetch('/api/sync', { method: 'GET', cache: 'no-store' });
        if (!resp.ok) return { success: false, status: resp.status };

        const serverData = await resp.json();
        if (serverData && (serverData.reviews || serverData.timeTracking)) {
          this.importAllData(serverData);
        }

        const fullPayload = this.exportAllData();
        const postResp = await fetch('/api/sync', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(fullPayload)
        });

        return { success: postResp.ok, isConnected: true, lastSynced: new Date().toISOString() };
      } catch (e) {
        return { success: false, isConnected: false, error: e.message };
      }
    },

    triggerServerSync() {
      scheduleServerSync(500);
    }
  };
})();

// Export globally for browser and module systems
if (typeof window !== 'undefined') {
  window.StorageManager = StorageManager;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = StorageManager;
}
