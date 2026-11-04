/**
 * StorageManager - Handles local caching and spaced repetition system (SRS) persistence.
 * Stores chapter review history, lapse counters, interval schedules, and study preferences in localStorage.
 */

const StorageManager = (function() {
  const REVIEW_KEY = 'hsk_review_store_v1';
  const SETTINGS_KEY = 'hsk_study_settings_v1';

  // Spaced Repetition interval days based on Leitner/SRS levels
  const SRS_INTERVAL_DAYS = [0, 1, 3, 7, 14, 30]; // Level 0 (same day), Level 1 (1d), Level 2 (3d), etc.
  const ONE_DAY_MS = 24 * 60 * 60 * 1000;

  // Retrieve raw store
  function getRawStore() {
    try {
      const data = localStorage.getItem(REVIEW_KEY);
      return data ? JSON.parse(data) : {};
    } catch (e) {
      console.warn('Failed to parse review cache from localStorage:', e);
      return {};
    }
  }

  // Save raw store
  function saveRawStore(store) {
    try {
      localStorage.setItem(REVIEW_KEY, JSON.stringify(store));
    } catch (e) {
      console.warn('Failed to save review cache to localStorage:', e);
    }
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
        firstReviewed: Date.now(),
        lastReviewed: Date.now()
      };

      const now = Date.now();
      existing.reviews = (existing.reviews || 0) + 1;
      existing.lastReviewed = now;

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

      store[chapterDir][idStr] = existing;
      saveRawStore(store);
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
     * Reset review cache for a chapter
     */
    resetChapter(chapterDir) {
      const store = getRawStore();
      delete store[chapterDir];
      saveRawStore(store);
    },

    /**
     * Get user study preferences
     */
    getSettings() {
      const defaults = {
        studyMode: 'flashcard', // 'flashcard' or 'browse'
        autoAudio: true,       // speak headword on answer reveal
        toneColors: true,      // dynamic pinyin tone coloring
        speechRate: 0.9,       // speech rate (0.75 - 1.2)
        studyOrder: 'order',   // 'order' or 'shuffle'
        activeTab: 'sentences',// default active pill tab
        filter: 'all',         // 'all', 'due', 'lapses', 'remembered', 'new'
        lang: localStorage.getItem('hsk_lang') || 'both',
        preferredVoice: 'random', // 'random', 'mature_woman', 'soothing_host', 'office_man', 'tender_ceo'
        autoAdvanceChapter: true, // auto-start next chapter when finished
        autoAdvanceDelay: 5,      // countdown seconds before auto-advance
        soundFx: true,            // soft UI audio feedback
        showPassagePinyin: false  // reading passage pinyin visibility toggle
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

