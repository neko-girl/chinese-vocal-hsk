/**
 * StorageManager - Handles local caching, spaced repetition system (SRS) persistence,
 * time tracking logs, study habits analytics, and character review timelines.
 */

const StorageManager = (function() {
  const REVIEW_KEY = 'hsk_review_store_v1';
  const SETTINGS_KEY = 'hsk_study_settings_v1';
  const TIME_KEY = 'hsk_time_tracker_v1';

  // Spaced Repetition interval days based on Leitner/SRS levels
  const SRS_INTERVAL_DAYS = [0, 1, 3, 7, 14, 30]; // Level 0 (same day), Level 1 (1d), Level 2 (3d), etc.
  const ONE_DAY_MS = 24 * 60 * 60 * 1000;

  function getTodayKey() {
    const d = new Date();
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  // Retrieve raw SRS review store
  function getRawStore() {
    try {
      const data = localStorage.getItem(REVIEW_KEY);
      return data ? JSON.parse(data) : {};
    } catch (e) {
      console.warn('Failed to parse review cache from localStorage:', e);
      return {};
    }
  }

  // Save raw SRS review store
  function saveRawStore(store) {
    try {
      localStorage.setItem(REVIEW_KEY, JSON.stringify(store));
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
     * Record a review outcome ("remembered" or "dont_remember")
     * Maintains chronological history events and lapse counters
     */
    recordReview(chapterDir, wordId, status) {
      const store = getRawStore();
      if (!store[chapterDir]) {
        store[chapterDir] = {};
      }

      const idStr = String(wordId);
      const existing = store[chapterDir][idStr] || {
        status: 'new',
        srsLevel: 0,
        intervalDays: 0,
        dueDate: Date.now(),
        reviews: 0,
        lapses: 0,
        history: [],
        firstReviewed: Date.now(),
        lastReviewed: Date.now()
      };

      const now = Date.now();
      existing.reviews = (existing.reviews || 0) + 1;
      existing.lastReviewed = now;
      if (!Array.isArray(existing.history)) {
        existing.history = [];
      }

      if (status === 'remembered') {
        const nextLevel = Math.min(SRS_INTERVAL_DAYS.length - 1, (existing.srsLevel || 0) + 1);
        const interval = SRS_INTERVAL_DAYS[nextLevel];
        existing.status = 'remembered';
        existing.srsLevel = nextLevel;
        existing.intervalDays = interval;
        existing.dueDate = now + (interval * ONE_DAY_MS);
      } else {
        // "dont_remember" -> reset SRS level to 0, log lapse, due immediately
        existing.status = 'dont_remember';
        existing.srsLevel = 0;
        existing.intervalDays = 0;
        existing.dueDate = now;
        existing.lapses = (existing.lapses || 0) + 1;
      }

      // Append to chronological history (capped to last 25 steps)
      existing.history.push({
        t: now,
        result: status,
        level: existing.srsLevel
      });
      if (existing.history.length > 25) {
        existing.history.shift();
      }

      store[chapterDir][idStr] = existing;
      saveRawStore(store);

      // Log to time tracker / study analytics
      this.recordStudyEvent('card_grade', {
        status,
        wordId,
        chapterDir,
        srsLevel: existing.srsLevel
      });

      return existing;
    },

    /**
     * Check if a word is due for review
     */
    isDue(reviewItem) {
      if (!reviewItem) return true; // New words are due
      if (reviewItem.status === 'dont_remember') return true;
      if (!reviewItem.dueDate) return true;
      return reviewItem.dueDate <= Date.now();
    },

    /**
     * Get aggregated chapter statistics
     */
    getChapterStats(chapterDir, words = []) {
      const reviews = this.getChapterReviews(chapterDir);
      const total = words.length;
      let remembered = 0;
      let dontRemember = 0;
      let unreviewed = 0;
      let dueCount = 0;
      let mastered = 0;

      words.forEach(w => {
        const rev = reviews[String(w.id)];
        if (!rev) {
          unreviewed++;
          dueCount++;
        } else {
          if (rev.status === 'remembered') remembered++;
          if (rev.status === 'dont_remember') dontRemember++;
          if (this.isDue(rev)) dueCount++;
          if (rev.srsLevel >= 4) mastered++;
        }
      });

      const percent = total > 0 ? Math.round((remembered / total) * 100) : 0;
      return {
        total,
        remembered,
        dontRemember,
        unreviewed,
        dueCount,
        mastered,
        percent
      };
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
        preferredVoice: 'random',// 'random', 'mature_woman', 'soothing_host', 'office_man', 'tender_ceo'
        autoAdvanceChapter: true,// auto-start next chapter when finished
        autoAdvanceDelay: 5,     // countdown seconds before auto-advance
        soundFx: true,           // soft UI audio feedback
        showPassagePinyin: false,// reading passage pinyin visibility toggle
        afkThresholdSeconds: 120,// AFK inactivity threshold in seconds (default 2 min)
        browserVoiceURI: ''      // Browser TTS Voice (empty string = auto-detect best neural)
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
      } catch (e) {
        console.warn('Failed to save study settings:', e);
      }
      return updated;
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
