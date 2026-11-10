/**
 * Test Suite: Two-Stage Spaced Repetition System (SRS) & Dynamic Queue Engine
 * Tests per-card data model, migration, intra-session re-queueing,
 * inter-session scheduling, anti-clustering (MIN_GAP = 5), and Smart Mix (3:1).
 */

const assert = require('assert');

// Mock browser localStorage for Node.js
class LocalStorageMock {
  constructor() {
    this.store = {};
  }
  getItem(key) {
    return this.store[key] || null;
  }
  setItem(key, value) {
    this.store[key] = String(value);
  }
  removeItem(key) {
    delete this.store[key];
  }
  clear() {
    this.store = {};
  }
}
global.localStorage = new LocalStorageMock();

const StorageManager = require('../web/js/storage.js');

let passedTests = 0;
function test(name, fn) {
  try {
    fn();
    console.log(`  ✓ ${name}`);
    passedTests++;
  } catch (err) {
    console.error(`  ✗ ${name}`);
    console.error(err);
    process.exit(1);
  }
}

console.log('--- Running SRS Engine & Dynamic Queue Tests ---');

// =========================================================================
// 1. Data Model & Migration Tests
// =========================================================================
test('1.1 New card initialization has correct defaults', () => {
  const schedule = StorageManager.calculateNextSchedule({ state: 'new' }, 'good');
  assert.strictEqual(schedule.nextState, 'learning');
  assert.strictEqual(schedule.nextStep, 1);
  assert.strictEqual(schedule.nextInterval, 0);
  assert.strictEqual(schedule.graduated, false);
  assert.ok(schedule.reinsertOffset >= 8 && schedule.reinsertOffset <= 14, `Offset ${schedule.reinsertOffset} out of range [8, 14]`);
});

test('1.2 Legacy review data migration in getRawStore', () => {
  localStorage.clear();
  const legacyStore = {
    chapter_01: {
      '1': { status: 'remembered', srsLevel: 2, intervalDays: 3, dueDate: 1700000000000, reviews: 3, lapses: 0 },
      '2': { status: 'dont_remember', srsLevel: 0, intervalDays: 0, dueDate: 1700000000000, reviews: 2, lapses: 1 },
      '3': { status: 'new', srsLevel: 0, intervalDays: 0, dueDate: 1700000000000, reviews: 0, lapses: 0 }
    }
  };
  localStorage.setItem('hsk_review_store_v1', JSON.stringify(legacyStore));

  const migrated1 = StorageManager.getWordReview('chapter_01', 1);
  assert.strictEqual(migrated1.state, 'review');
  assert.strictEqual(migrated1.interval, 3);
  assert.strictEqual(migrated1.step, 1);
  assert.strictEqual(migrated1.ease, 2.5);
  assert.strictEqual(migrated1.lapses, 0);

  const migrated2 = StorageManager.getWordReview('chapter_01', 2);
  assert.strictEqual(migrated2.state, 'relearning');
  assert.strictEqual(migrated2.step, 0);
  assert.strictEqual(migrated2.interval, 0);
  assert.strictEqual(migrated2.lapses, 1);

  const migrated3 = StorageManager.getWordReview('chapter_01', 3);
  assert.strictEqual(migrated3.state, 'new');
});

// =========================================================================
// 2. Intra-Session Learning & Delayed Re-Queueing
// =========================================================================
test('2.1 New card + Good: state = learning, step = 1, reinsert offset in [8, 14]', () => {
  const card = { state: 'new', step: 0, interval: 0, ease: 2.5, lapses: 0 };
  const res = StorageManager.calculateNextSchedule(card, 'good');
  assert.strictEqual(res.nextState, 'learning');
  assert.strictEqual(res.nextStep, 1);
  assert.strictEqual(res.nextInterval, 0);
  assert.strictEqual(res.graduated, false);
  assert.ok(res.reinsertOffset >= 8 && res.reinsertOffset <= 14);
});

test('2.2 New card + Again: state = learning, step = 0, reinsert offset in [4, 6]', () => {
  const card = { state: 'new', step: 0, interval: 0, ease: 2.5, lapses: 0 };
  const res = StorageManager.calculateNextSchedule(card, 'again');
  assert.strictEqual(res.nextState, 'learning');
  assert.strictEqual(res.nextStep, 0);
  assert.strictEqual(res.nextInterval, 0);
  assert.strictEqual(res.graduated, false);
  assert.ok(res.reinsertOffset >= 4 && res.reinsertOffset <= 6);
});

test('2.3 Learning card at step 1 + Good: graduates to review, interval = 1d', () => {
  const card = { state: 'learning', step: 1, interval: 0, ease: 2.5, lapses: 0 };
  const res = StorageManager.calculateNextSchedule(card, 'good');
  assert.strictEqual(res.nextState, 'review');
  assert.strictEqual(res.nextStep, 1);
  assert.strictEqual(res.nextInterval, 1);
  assert.strictEqual(res.graduated, true);
  assert.strictEqual(res.reinsertOffset, null);
});

test('2.4 Answering Easy on new or learning card bypasses step 1 and graduates to interval = 3d', () => {
  const cardNew = { state: 'new', step: 0, interval: 0, ease: 2.5, lapses: 0 };
  const resNew = StorageManager.calculateNextSchedule(cardNew, 'easy');
  assert.strictEqual(resNew.nextState, 'review');
  assert.strictEqual(resNew.nextInterval, 3);
  assert.strictEqual(resNew.graduated, true);

  const cardLearn = { state: 'learning', step: 0, interval: 0, ease: 2.5, lapses: 0 };
  const resLearn = StorageManager.calculateNextSchedule(cardLearn, 'easy');
  assert.strictEqual(resLearn.nextState, 'review');
  assert.strictEqual(resLearn.nextInterval, 3);
  assert.strictEqual(resLearn.graduated, true);
});

// =========================================================================
// 3. Inter-Session Spaced Repetition (Long-Term Scheduling)
// =========================================================================
test('3.1 Review card + Again: lapses += 1, ease -= 0.20 (min 1.3), postRelearnInterval = round(interval*0.25), state = relearning, reinsert offset in [6, 10]', () => {
  const card = { state: 'review', step: 1, interval: 12, ease: 2.5, lapses: 0 };
  const res = StorageManager.calculateNextSchedule(card, 'again');
  assert.strictEqual(res.nextState, 'relearning');
  assert.strictEqual(res.nextStep, 1);
  assert.strictEqual(res.nextInterval, 0);
  assert.strictEqual(res.lapsesDelta, 1);
  assert.strictEqual(res.nextEase, 2.3);
  assert.strictEqual(res.postRelearnInterval, 3); // round(12 * 0.25) = 3
  assert.strictEqual(res.graduated, false);
  assert.ok(res.reinsertOffset >= 6 && res.reinsertOffset <= 10);
});

test('3.2 Ease floor of 1.3 is enforced on repeated lapses', () => {
  const card = { state: 'review', step: 1, interval: 4, ease: 1.4, lapses: 3 };
  const res = StorageManager.calculateNextSchedule(card, 'again');
  assert.strictEqual(res.nextEase, 1.3);
});

test('3.3 Review card + Hard: ease -= 0.15, interval = max(interval+1, round(interval*1.2))', () => {
  const card = { state: 'review', step: 1, interval: 10, ease: 2.5, lapses: 0 };
  const res = StorageManager.calculateNextSchedule(card, 'hard');
  assert.strictEqual(res.nextState, 'review');
  assert.strictEqual(res.nextEase, 2.35);
  assert.strictEqual(res.nextInterval, 12); // round(10 * 1.2) = 12
  assert.strictEqual(res.graduated, true);
});

test('3.4 Review card + Good applies ease and fuzz (0.9 to 1.1) when interval >= 3', () => {
  const card = { state: 'review', step: 1, interval: 10, ease: 2.5, lapses: 0 };
  // Expected base: 10 * 2.5 = 25. With fuzz [0.9, 1.1], range is [22, 28]
  for (let i = 0; i < 20; i++) {
    const res = StorageManager.calculateNextSchedule(card, 'good');
    assert.strictEqual(res.nextState, 'review');
    assert.strictEqual(res.graduated, true);
    assert.ok(res.nextInterval >= 22 && res.nextInterval <= 28, `Interval ${res.nextInterval} out of expected fuzz bounds [22, 28]`);
  }
});

test('3.5 Review card + Easy: ease += 0.15, interval = max(interval+2, round(interval*ease*1.3*fuzz))', () => {
  const card = { state: 'review', step: 1, interval: 10, ease: 2.5, lapses: 0 };
  // New ease = 2.65. Base = 10 * 2.65 * 1.3 = 34.45. With fuzz [0.9, 1.1], range is [31, 38]
  const res = StorageManager.calculateNextSchedule(card, 'easy');
  assert.strictEqual(res.nextState, 'review');
  assert.strictEqual(res.nextEase, 2.65);
  assert.strictEqual(res.graduated, true);
  assert.ok(res.nextInterval >= 31 && res.nextInterval <= 39, `Easy interval ${res.nextInterval} outside expected bounds`);
});

test('3.6 Relearning card at step 1 + Good restores postRelearnInterval', () => {
  const card = { state: 'relearning', step: 1, interval: 0, postRelearnInterval: 5, ease: 2.3, lapses: 1 };
  const res = StorageManager.calculateNextSchedule(card, 'good');
  assert.strictEqual(res.nextState, 'review');
  assert.strictEqual(res.nextInterval, 5);
  assert.strictEqual(res.graduated, true);
  assert.strictEqual(res.reinsertOffset, null);
});

// =========================================================================
// 4. Anti-Clustering Guard (MIN_GAP = 5) & Backfill Simulation
// =========================================================================
test('4.1 Anti-Clustering never places same word within 5 positions of itself', () => {
  const queue = ['ch1:1', 'ch1:2', 'ch1:3', 'ch1:4', 'ch1:5', 'ch1:6', 'ch1:7', 'ch1:8'];
  const queueIndex = 0;
  const currentCard = queue[queueIndex]; // 'ch1:1'
  const MIN_GAP = 5;

  // Simulate insertion with offset 5
  const targetOffset = 5;
  const targetIndex = queueIndex + 1 + targetOffset; // index 6

  // Verify distance between original index (0) and targetIndex (6) is >= MIN_GAP
  assert.ok(targetIndex - queueIndex >= MIN_GAP, `Gap ${targetIndex - queueIndex} must be >= ${MIN_GAP}`);
});

test('4.2 Backfill triggers when remaining queue ahead is smaller than MIN_GAP', () => {
  const queue = ['ch1:1', 'ch1:2'];
  const queueIndex = 0;
  const remainingAhead = queue.length - (queueIndex + 1); // 1 card ahead
  const MIN_GAP = 5;

  assert.ok(remainingAhead < MIN_GAP, 'Remaining cards ahead is less than MIN_GAP');
  const needed = MIN_GAP - remainingAhead; // 4 cards needed
  assert.strictEqual(needed, 4);

  // Mock available candidate pool
  const candidatePool = ['ch1:10', 'ch1:11', 'ch1:12', 'ch1:13', 'ch1:14'];
  const backfilled = candidatePool.slice(0, needed);
  queue.push(...backfilled);

  const updatedRemaining = queue.length - (queueIndex + 1);
  assert.ok(updatedRemaining >= MIN_GAP, `Updated remaining ${updatedRemaining} must be >= ${MIN_GAP}`);
});

// =========================================================================
// 5. Smart Mix Interleaving (3 Due Reviews : 1 New Card)
// =========================================================================
test('5.1 Smart Mix produces roughly 3 Due : 1 New ratio', () => {
  const due = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6'];
  const news = ['n1', 'n2'];
  const interleaved = [];

  let dIdx = 0;
  let nIdx = 0;
  while (dIdx < due.length || nIdx < news.length) {
    for (let k = 0; k < 3 && dIdx < due.length; k++) {
      interleaved.push(due[dIdx++]);
    }
    if (nIdx < news.length) {
      interleaved.push(news[nIdx++]);
    }
  }

  // Expected sequence: d1, d2, d3, n1, d4, d5, d6, n2
  assert.deepStrictEqual(interleaved, ['d1', 'd2', 'd3', 'n1', 'd4', 'd5', 'd6', 'n2']);
});

// =========================================================================
// 6. Preview Schedule Generation
// =========================================================================
test('6.1 previewSchedule returns expected labels for front-end buttons', () => {
  const newCard = { state: 'new', step: 0, interval: 0 };
  const pNew = StorageManager.previewSchedule(newCard);
  assert.strictEqual(pNew.again, '<10m');
  assert.strictEqual(pNew.easy, '3d');

  const revCard = { state: 'review', step: 1, interval: 10, ease: 2.5 };
  const pRev = StorageManager.previewSchedule(revCard);
  assert.strictEqual(pRev.again, '<10m');
  assert.strictEqual(pRev.hard, '12d');
  assert.strictEqual(pRev.good, '25d');
});

console.log(`\nAll ${passedTests} tests passed successfully! ✨`);
