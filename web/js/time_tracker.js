/**
 * TimeTracker - Inactivity-aware study & reading time tracker.
 * Tracks active learning time, pauses on AFK (inactivity threshold),
 * distinguishes between Flashcard Study Time and Dictionary Reading Time,
 * and synchronizes state across windows.
 */

const TimeTracker = (function() {
  // Configurable AFK threshold in milliseconds (default: 2 minutes)
  let afkThresholdMs = 120 * 1000;
  const TENTATIVE_GRACE_MS = 60 * 1000; // 1 min buffer before tentative holding

  let currentMode = 'flashcard'; // 'flashcard' | 'dictionary' | 'stats'
  let isAfk = false;
  let lastActivityTimestamp = Date.now();
  let tentativeSeconds = 0;
  let accumulatedSinceLastSave = { study: 0, reading: 0 };
  let tickTimer = null;

  // Registered listeners
  const tickListeners = new Set();
  const statusListeners = new Set();

  function getTodayKey() {
    const d = new Date();
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  // Handle user activity event
  function onUserActivity() {
    const now = Date.now();
    const wasAfk = isAfk;
    const idleMs = now - lastActivityTimestamp;

    lastActivityTimestamp = now;

    if (wasAfk) {
      isAfk = false;
      tentativeSeconds = 0;
      notifyStatusChange();
    } else if (idleMs > TENTATIVE_GRACE_MS && idleMs < afkThresholdMs) {
      // User was tentatively idle but resumed before reaching AFK threshold: credit the buffered seconds
      if (tentativeSeconds > 0) {
        if (currentMode === 'flashcard') {
          accumulatedSinceLastSave.study += tentativeSeconds;
        } else if (currentMode === 'dictionary') {
          accumulatedSinceLastSave.reading += tentativeSeconds;
        }
        tentativeSeconds = 0;
      }
    }
  }

  // Heartbeat tick executed every 1 second
  function tick() {
    // Only accumulate time if document is visible and has focus (or is active standalone window)
    const isDocVisible = typeof document !== 'undefined' && document.visibilityState === 'visible';
    const isFocused = typeof document !== 'undefined' ? (document.hasFocus ? document.hasFocus() : true) : true;

    if (!isDocVisible || !isFocused) {
      // Tab is in background or unfocused: do not accumulate time
      return;
    }

    const now = Date.now();
    const idleMs = now - lastActivityTimestamp;

    if (idleMs >= afkThresholdMs) {
      // Idle threshold exceeded -> Enter AFK state
      if (!isAfk) {
        isAfk = true;
        // Discard any unverified tentative seconds
        tentativeSeconds = 0;
        notifyStatusChange();
      }
      return;
    }

    // Active tracking
    if (idleMs <= TENTATIVE_GRACE_MS) {
      // Definitely active
      if (currentMode === 'flashcard') {
        accumulatedSinceLastSave.study += 1;
      } else if (currentMode === 'dictionary') {
        accumulatedSinceLastSave.reading += 1;
      }
    } else {
      // Tentative idle (between grace period and AFK threshold)
      tentativeSeconds += 1;
    }

    // Periodically commit to StorageManager
    if (accumulatedSinceLastSave.study >= 5 || accumulatedSinceLastSave.reading >= 5) {
      commitAccumulated();
    }

    notifyTick();
  }

  // Save accumulated seconds into persistent store
  function commitAccumulated() {
    if (accumulatedSinceLastSave.study === 0 && accumulatedSinceLastSave.reading === 0) return;

    if (typeof StorageManager !== 'undefined' && StorageManager.recordActiveTime) {
      StorageManager.recordActiveTime(
        accumulatedSinceLastSave.study,
        accumulatedSinceLastSave.reading,
        currentMode
      );
    }

    accumulatedSinceLastSave.study = 0;
    accumulatedSinceLastSave.reading = 0;
  }

  function notifyTick() {
    const data = getStatus();
    tickListeners.forEach(cb => {
      try { cb(data); } catch (e) { console.error('TimeTracker tick listener error:', e); }
    });
  }

  function notifyStatusChange() {
    const data = getStatus();
    statusListeners.forEach(cb => {
      try { cb(data); } catch (e) { console.error('TimeTracker status listener error:', e); }
    });
  }

  function getStatus() {
    let todayData = { studySeconds: 0, readingSeconds: 0 };
    if (typeof StorageManager !== 'undefined' && StorageManager.getTimeStatsToday) {
      todayData = StorageManager.getTimeStatsToday();
    }

    const currentTotalStudy = todayData.studySeconds + accumulatedSinceLastSave.study;
    const currentTotalReading = todayData.readingSeconds + accumulatedSinceLastSave.reading;

    return {
      isAfk,
      mode: currentMode,
      afkThresholdSeconds: Math.round(afkThresholdMs / 1000),
      studySecondsToday: currentTotalStudy,
      readingSecondsToday: currentTotalReading,
      totalSecondsToday: currentTotalStudy + currentTotalReading
    };
  }

  return {
    init(options = {}) {
      if (options.afkThresholdSeconds) {
        afkThresholdMs = options.afkThresholdSeconds * 1000;
      }
      if (options.mode) {
        currentMode = options.mode;
      }

      // Load saved threshold from settings if available
      if (typeof StorageManager !== 'undefined' && StorageManager.getSettings) {
        const settings = StorageManager.getSettings();
        if (settings.afkThresholdSeconds) {
          afkThresholdMs = settings.afkThresholdSeconds * 1000;
        }
      }

      // Attach user activity listeners
      const events = ['mousemove', 'mousedown', 'keydown', 'touchstart', 'scroll', 'wheel'];
      events.forEach(evtName => {
        window.addEventListener(evtName, onUserActivity, { passive: true });
      });

      // Handle visibility changes (minimize, tab switch)
      document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'hidden') {
          commitAccumulated();
        } else {
          lastActivityTimestamp = Date.now();
        }
      });

      window.addEventListener('beforeunload', () => {
        commitAccumulated();
      });

      // Audio activity listener
      document.addEventListener('play', () => {
        onUserActivity();
      }, true);

      // Start ticker
      if (tickTimer) clearInterval(tickTimer);
      tickTimer = setInterval(tick, 1000);
    },

    setMode(mode) {
      if (mode === currentMode) return;
      commitAccumulated();
      currentMode = mode;
      onUserActivity();
    },

    getMode() {
      return currentMode;
    },

    setAfkThresholdSeconds(sec) {
      afkThresholdMs = Math.max(30, Number(sec)) * 1000;
      if (typeof StorageManager !== 'undefined' && StorageManager.saveSettings) {
        StorageManager.saveSettings({ afkThresholdSeconds: Math.round(afkThresholdMs / 1000) });
      }
      notifyStatusChange();
    },

    getAfkThresholdSeconds() {
      return Math.round(afkThresholdMs / 1000);
    },

    isAfk() {
      return isAfk;
    },

    recordImmediateActivity() {
      onUserActivity();
    },

    getStatus,

    onTick(callback) {
      if (typeof callback === 'function') {
        tickListeners.add(callback);
      }
      return () => tickListeners.delete(callback);
    },

    onStatusChange(callback) {
      if (typeof callback === 'function') {
        statusListeners.add(callback);
      }
      return () => statusListeners.delete(callback);
    },

    flush() {
      commitAccumulated();
    }
  };
})();

// Export globally for browser and Node environments
if (typeof window !== 'undefined') {
  window.TimeTracker = TimeTracker;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = TimeTracker;
}
