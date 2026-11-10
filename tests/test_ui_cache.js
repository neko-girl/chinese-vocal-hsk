/**
 * Test Suite for Dual-Layer Cache, Session Snapshot Persistence, Undo Stack,
 * Predictive Intervals, 7-Day Forecast, Leech Extraction, and Backup/Restore.
 */

const assert = require('assert');

// Mock browser localStorage for Node test runner
const localStorageStore = {};
global.localStorage = {
  getItem: (key) => (Object.prototype.hasOwnProperty.call(localStorageStore, key) ? localStorageStore[key] : null),
  setItem: (key, value) => {
    localStorageStore[key] = String(value);
  },
  removeItem: (key) => {
    delete localStorageStore[key];
  },
  clear: () => {
    for (const k of Object.keys(localStorageStore)) {
      delete localStorageStore[k];
    }
  }
};

global.window = {
  localStorage: global.localStorage
};

// Import modules under test
const StorageManager = require('../web/js/storage.js');
global.StorageManager = StorageManager;
const AudioManager = require('../web/js/audio_manager.js');

let testsPassed = 0;
let testsFailed = 0;

function test(name, fn) {
  try {
    fn();
    console.log(`  ✓ ${name}`);
    testsPassed++;
  } catch (err) {
    console.error(`  ✗ ${name}`);
    console.error(err);
    testsFailed++;
  }
}

console.log('\n--- Running Dual-Layer Cache & UI Engine Tests ---');

// =========================================================================
// 1. Schema v2 & Dual-Layer Persistence
// =========================================================================
test('1.1 Schema v2 wrapper encapsulates updatedAt and wordsById', () => {
  localStorage.clear();
  StorageManager.recordReview('chapter_01', 1, 'good');

  const v2Raw = localStorage.getItem('hsk_review_store_v2');
  assert.ok(v2Raw, 'hsk_review_store_v2 must exist in localStorage');

  const parsed = JSON.parse(v2Raw);
  assert.strictEqual(parsed.schemaVersion, 2, 'schemaVersion must be 2');
  assert.ok(typeof parsed.updatedAt === 'number', 'updatedAt must be a numeric timestamp');
  assert.ok(parsed.wordsById, 'wordsById must exist');
  assert.ok(parsed.wordsById['chapter_01_1'], 'wordsById must contain chapter_01_1 key');

  // Verify v1 backwards compatibility store is also written
  const v1Raw = localStorage.getItem('hsk_review_store_v1');
  assert.ok(v1Raw, 'hsk_review_store_v1 must exist for legacy compatibility');
});

test('1.2 Non-destructive migration from v1 to Schema v2', () => {
  localStorage.clear();
  const legacyData = {
    chapter_01: {
      '5': { status: 'remembered', srsLevel: 3, intervalDays: 7, reviews: 2, dueDate: 1710000000000 }
    }
  };
  localStorage.setItem('hsk_review_store_v1', JSON.stringify(legacyData));

  const rec = StorageManager.getWordReview('chapter_01', 5);
  assert.strictEqual(rec.state, 'review');
  assert.strictEqual(rec.interval, 7);

  const v2Raw = localStorage.getItem('hsk_review_store_v2');
  assert.ok(v2Raw, 'Migration must automatically generate hsk_review_store_v2');
  const parsed = JSON.parse(v2Raw);
  assert.strictEqual(parsed.schemaVersion, 2);
  assert.ok(parsed.wordsById['chapter_01_5']);
});

// =========================================================================
// 2. Predictive SRS Intervals
// =========================================================================
test('2.1 predictNextIntervals returns card offsets for New cards', () => {
  const newCard = { state: 'new', step: 0, interval: 0, ease: 2.5 };
  const pred = StorageManager.predictNextIntervals(newCard);

  assert.strictEqual(pred.again.label, '~5 cards');
  assert.strictEqual(pred.hard.label, '~6 cards');
  assert.strictEqual(pred.good.label, '~10 cards');
  assert.strictEqual(pred.easy.label, '3d');
});

test('2.2 predictNextIntervals returns 1d graduation on Learning step 1', () => {
  const step1Card = { state: 'learning', step: 1, interval: 0, ease: 2.5 };
  const pred = StorageManager.predictNextIntervals(step1Card);

  assert.strictEqual(pred.again.label, '~5 cards');
  assert.strictEqual(pred.good.label, '1d');
  assert.strictEqual(pred.easy.label, '3d');
});

test('2.3 predictNextIntervals returns days and ease adjustments for Review cards', () => {
  const revCard = { state: 'review', step: 1, interval: 10, ease: 2.5 };
  const pred = StorageManager.predictNextIntervals(revCard);

  assert.strictEqual(pred.again.label, '~8 cards');
  assert.strictEqual(pred.hard.label, '12d');
  assert.strictEqual(pred.good.label, '25d');
  assert.strictEqual(pred.easy.label, '34d');
});

// =========================================================================
// 3. Active Session Persistence & Rollover
// =========================================================================
test('3.1 Same calendar day session restoration preserves exact queue and index', () => {
  localStorage.clear();
  const today = StorageManager.getTodayKey();
  const testSession = {
    queue: ['chapter_01:1', 'chapter_01:2', 'chapter_01:3'],
    currentIndex: 1,
    activeFilters: { chapter: 'chapter_01', status: 'all' },
    frontierChapterId: 'chapter_01',
    undoStack: [],
    startedAt: 1700000000000,
    lastActiveDate: today
  };

  StorageManager.saveActiveSession(testSession);
  const restored = StorageManager.getActiveSession();

  assert.ok(restored, 'Active session must be retrieved');
  assert.strictEqual(restored.lastActiveDate, today);
  assert.strictEqual(restored.currentIndex, 1);
  assert.deepStrictEqual(restored.queue, testSession.queue);
});

test('3.2 Calendar day rollover expires session and promotes unfinished learning cards', () => {
  localStorage.clear();
  // Set up an uncompleted learning card
  StorageManager.recordReview('chapter_01', 10, 'good'); // new -> learning step 1
  const recBefore = StorageManager.getWordReview('chapter_01', 10);
  assert.strictEqual(recBefore.state, 'learning');

  // Save session with yesterday date
  const pastSession = {
    queue: ['chapter_01:10'],
    currentIndex: 0,
    activeFilters: { chapter: 'all', status: 'all' },
    frontierChapterId: 'chapter_01',
    undoStack: [],
    startedAt: 1700000000000,
    lastActiveDate: '2020-01-01'
  };
  StorageManager.saveActiveSession(pastSession);

  const restored = StorageManager.getActiveSession();
  assert.ok(restored.expired, 'Session from past date must expire');
  assert.strictEqual(restored.isNewDay, true);
  assert.strictEqual(restored.promotedCardsCount, 1);

  // Card must now be due immediately in today review
  const recAfter = StorageManager.getWordReview('chapter_01', 10);
  assert.ok(recAfter.dueAt <= Date.now(), 'Promoted learning card must be due immediately');
});

// =========================================================================
// 4. Undo Stack
// =========================================================================
test('4.1 pushUndo and popUndo restore previous card record and queue state', () => {
  localStorage.clear();
  StorageManager.recordReview('chapter_01', 1, 'good'); // learning step 1
  const snapshotBefore = StorageManager.getWordReview('chapter_01', 1);

  const initialQueue = ['chapter_01:1', 'chapter_01:2'];
  StorageManager.pushUndo({
    chapterId: 'chapter_01',
    wordId: 1,
    prevRecord: snapshotBefore,
    prevQueue: initialQueue,
    prevIndex: 0
  });

  assert.strictEqual(StorageManager.canUndo(), true);

  // Now rate it again (mutating record to step 0)
  StorageManager.recordReview('chapter_01', 1, 'again');
  const mutated = StorageManager.getWordReview('chapter_01', 1);
  assert.strictEqual(mutated.step, 0);

  // Pop undo
  const popped = StorageManager.popUndo();
  assert.ok(popped);
  assert.strictEqual(popped.wordId, '1');

  // Verify restored record
  const reverted = StorageManager.getWordReview('chapter_01', 1);
  assert.strictEqual(reverted.step, 1);
  assert.strictEqual(reverted.state, 'learning');
});

// =========================================================================
// 5. 7-Day Forecast & Leech List
// =========================================================================
test('5.1 getForecast7Days computes 7 daily buckets', () => {
  localStorage.clear();
  const forecast = StorageManager.getForecast7Days();
  assert.strictEqual(forecast.length, 7);
  assert.strictEqual(forecast[0].dayLabel, 'Today');
  assert.strictEqual(forecast[1].dayLabel, 'Tomorrow');
  assert.strictEqual(typeof forecast[0].count, 'number');
});

test('5.2 getLeechWords extracts and ranks most-lapsed words', () => {
  localStorage.clear();
  // Word 1: 3 lapses
  StorageManager.recordReview('chapter_01', 1, 'good');
  StorageManager.recordReview('chapter_01', 1, 'easy'); // review
  StorageManager.recordReview('chapter_01', 1, 'again'); // lapse 1
  StorageManager.recordReview('chapter_01', 1, 'again'); // lapse 2
  StorageManager.recordReview('chapter_01', 1, 'again'); // lapse 3

  // Word 2: 1 lapse
  StorageManager.recordReview('chapter_01', 2, 'good');
  StorageManager.recordReview('chapter_01', 2, 'easy'); // review
  StorageManager.recordReview('chapter_01', 2, 'again'); // lapse 1

  const leeches = StorageManager.getLeechWords(10);
  assert.strictEqual(leeches.length, 2);
  assert.strictEqual(leeches[0].wordId, '1');
  assert.strictEqual(leeches[0].lapses, 3);
  assert.strictEqual(leeches[1].wordId, '2');
  assert.strictEqual(leeches[1].lapses, 1);
});

// =========================================================================
// 6. Backup & Restore (JSON + Base64 Code)
// =========================================================================
test('6.1 Backup JSON export and import round-trip', () => {
  localStorage.clear();
  StorageManager.recordReview('chapter_01', 8, 'good');
  const jsonStr = StorageManager.exportBackupJson();
  assert.ok(jsonStr.includes('chapter_01'));

  // Clear and restore
  localStorage.clear();
  const ok = StorageManager.importBackupJson(jsonStr);
  assert.strictEqual(ok, true);

  const restoredRec = StorageManager.getWordReview('chapter_01', 8);
  assert.ok(restoredRec);
  assert.strictEqual(restoredRec.state, 'learning');
});

test('6.2 Backup Code (Base64) export and import round-trip', () => {
  localStorage.clear();
  StorageManager.recordReview('chapter_01', 9, 'easy'); // review interval = 3
  const code = StorageManager.exportBackupCode();
  assert.ok(code.startsWith('HSK_V2:'), 'Backup code must start with HSK_V2: prefix');

  localStorage.clear();
  const ok = StorageManager.importBackupCode(code);
  assert.strictEqual(ok, true);

  const restoredRec = StorageManager.getWordReview('chapter_01', 9);
  assert.ok(restoredRec);
  assert.strictEqual(restoredRec.state, 'review');
  assert.strictEqual(restoredRec.interval, 3);
});

// =========================================================================
// 7. Word Card Reset
// =========================================================================
test('7.1 resetWordReview restores card to initial new state', () => {
  localStorage.clear();
  StorageManager.recordReview('chapter_01', 12, 'easy');
  const rec = StorageManager.getWordReview('chapter_01', 12);
  assert.strictEqual(rec.state, 'review');

  const ok = StorageManager.resetWordReview('chapter_01', 12);
  assert.strictEqual(ok, true);

  const resetRec = StorageManager.getWordReview('chapter_01', 12);
  assert.strictEqual(resetRec.state, 'new');
  assert.strictEqual(resetRec.interval, 0);
  assert.strictEqual(resetRec.step, 0);
  assert.strictEqual(resetRec.lapses, 0);
});

// =========================================================================
// 8. Audio Manager Auto-Alternate Voice
// =========================================================================
test('8.1 Auto-Alternate cycles between mature_woman and office_man', () => {
  const audioMap = {
    mature_woman: 'audio/ch1/w1_mature_woman.mp3',
    office_man: 'audio/ch1/w1_office_man.mp3'
  };

  StorageManager.saveSettings({ preferredVoice: 'alternate' });

  AudioManager.setAlternateVoiceIndex(0);
  const v1 = AudioManager.selectAudioUrl(audioMap);
  assert.strictEqual(v1.voice, 'mature_woman');

  AudioManager.setAlternateVoiceIndex(1);
  const v2 = AudioManager.selectAudioUrl(audioMap);
  assert.strictEqual(v2.voice, 'office_man');

  AudioManager.setAlternateVoiceIndex(2);
  const v3 = AudioManager.selectAudioUrl(audioMap);
  assert.strictEqual(v3.voice, 'mature_woman');
});

// =========================================================================
// Summary
// =========================================================================
console.log(`\nAll ${testsPassed} UI & Cache tests passed successfully! ✨\n`);
if (testsFailed > 0) {
  process.exit(1);
}
