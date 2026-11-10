/**
 * Headless boot test simulating browser loading index.html and executing App.init()
 */

const fs = require('fs');
const path = require('path');
const assert = require('assert');

// 1. Setup minimal browser globals
const localStorageStore = {};
global.localStorage = {
  getItem: (k) => (Object.prototype.hasOwnProperty.call(localStorageStore, k) ? localStorageStore[k] : null),
  setItem: (k, v) => { localStorageStore[k] = String(v); },
  removeItem: (k) => { delete localStorageStore[k]; },
  clear: () => { for (const k of Object.keys(localStorageStore)) delete localStorageStore[k]; }
};

const elements = new Map();

function createElement(tag = 'div', id = '', classes = []) {
  const classListSet = new Set(classes);
  const el = {
    tagName: tag.toUpperCase(),
    id: id || '',
    className: classes.join(' '),
    classList: {
      add: (...cls) => cls.forEach(c => classListSet.add(c)),
      remove: (...cls) => cls.forEach(c => classListSet.delete(c)),
      toggle: (c, force) => {
        if (force === undefined) {
          if (classListSet.has(c)) classListSet.delete(c);
          else classListSet.add(c);
        } else if (force) classListSet.add(c);
        else classListSet.delete(c);
      },
      contains: (c) => classListSet.has(c)
    },
    style: {},
    attributes: {},
    getAttribute: (name) => el.attributes[name] || null,
    setAttribute: (name, val) => { el.attributes[name] = String(val); },
    hasAttribute: (name) => name in el.attributes,
    removeAttribute: (name) => { delete el.attributes[name]; },
    addEventListener: () => {},
    removeEventListener: () => {},
    appendChild: (child) => child,
    removeChild: () => {},
    querySelector: (sel) => null,
    querySelectorAll: () => [],
    innerHTML: '',
    textContent: '',
    value: '',
    disabled: false
  };
  return el;
}

// Parse IDs from index.html
const html = fs.readFileSync(path.join(__dirname, '../index.html'), 'utf-8');
const idMatches = html.match(/id="([^"]+)"/g) || [];
idMatches.forEach(m => {
  const id = m.replace('id="', '').replace('"', '');
  if (!elements.has(id)) {
    elements.set(id, createElement('div', id));
  }
});

global.Audio = class MockAudio {
  constructor(src) { this.src = src; }
  play() { return Promise.resolve(); }
  pause() {}
};

global.SpeechSynthesisUtterance = class MockSpeechSynthesisUtterance {
  constructor(text) { this.text = text; }
};

global.window = {
  localStorage: global.localStorage,
  location: { search: '', href: 'https://neko-girl.github.io/chinese-vocal-hsk/' },
  addEventListener: () => {},
  removeEventListener: () => {},
  speechSynthesis: {
    getVoices: () => [],
    onvoiceschanged: null,
    speak: () => {},
    cancel: () => {}
  },
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  setInterval: setInterval,
  clearInterval: clearInterval,
  fetch: async (url) => {
    // Return mock responses for local fetch
    if (url.includes('chapters.json')) {
      const manifestPath = path.join(__dirname, '../data/chapters.json');
      return { ok: true, json: async () => JSON.parse(fs.readFileSync(manifestPath, 'utf-8')) };
    }
    if (url.includes('data.json')) {
      const p = path.join(__dirname, '..', url.split('?')[0]);
      if (fs.existsSync(p)) {
        return { ok: true, json: async () => JSON.parse(fs.readFileSync(p, 'utf-8')) };
      }
    }
    return { ok: false, status: 404 };
  }
};

global.document = {
  readyState: 'complete',
  body: createElement('body', 'body'),
  getElementById: (id) => elements.get(id) || null,
  querySelector: (sel) => {
    if (sel.startsWith('#')) return elements.get(sel.slice(1)) || null;
    return null;
  },
  querySelectorAll: (sel) => {
    if (sel.startsWith('.')) {
      const cls = sel.slice(1);
      return Array.from(elements.values()).filter(el => el.classList.contains(cls));
    }
    return [];
  },
  createElement: (tag) => createElement(tag),
  addEventListener: () => {},
  removeEventListener: () => {}
};

// 2. Load manifest and chapter data scripts (file:// mode fallbacks)
require('../data/chapters.js');
for (let i = 1; i <= 8; i++) {
  const chDir = `chapter_0${i}`;
  require(`../chapters/${chDir}/data.js`);
}

// 3. Load core modules
const StorageManager = require('../web/js/storage.js');
global.StorageManager = StorageManager;

const TimeTracker = require('../web/js/time_tracker.js');
global.TimeTracker = TimeTracker;

const DataLoader = require('../web/js/data_loader.js');
global.DataLoader = DataLoader;

const AudioManager = require('../web/js/audio_manager.js');
global.AudioManager = AudioManager;

require('../web/js/renderer.js');
Object.assign(global, global.window);
require('../web/js/app.js');
Object.assign(global, global.window);
require('../web/js/mobile.js');

async function runBootTest() {
  console.log('--- Testing Browser Boot & App Initialization ---');

  assert.ok(global.window.App, 'window.App must be attached globally');
  assert.strictEqual(typeof global.window.App.init, 'function', 'App.init must be a function');

  console.log('  Executing App.init()...');
  await global.window.App.init();
  console.log('  ✓ App.init() completed without exceptions');

  // Verify basic app state
  const curWord = global.window.App.getCurrentWord();
  assert.ok(curWord, 'Current word must be loaded');
  console.log(`  ✓ Current word loaded: ${curWord.hanzi} (${curWord.pinyin})`);

  // Verify translation accessibility
  const enTrans = global.window.getWordTranslation(curWord, 'en');
  const esTrans = global.window.getWordTranslation(curWord, 'es');
  assert.ok(enTrans && enTrans.length > 0, 'English translation must be populated');
  assert.ok(esTrans && esTrans.length > 0, 'Spanish translation must be populated');
  assert.ok(Array.isArray(curWord.translations?.en) && curWord.translations.en.length > 0, 'translations.en array must be populated');
  console.log(`  ✓ Translations verified: EN="${enTrans}" | ES="${esTrans}"`);

  // Test switching views
  console.log('  Testing view transitions...');
  global.window.App.switchView('chapters');
  global.window.App.switchView('stats');
  global.window.App.switchView('settings');
  global.window.App.switchView('study');
  console.log('  ✓ All 4 views navigated successfully');

  // Test study interactions
  console.log('  Testing study interactions (flip, rate, undo)...');
  global.window.App.showAnswer();
  console.log('  ✓ Card show answer successful');

  global.window.App.rateCard('good');
  console.log('  ✓ Card rated Good');

  assert.strictEqual(StorageManager.canUndo(), true, 'Undo must be available after rating');
  global.window.App.undoLastAction();
  console.log('  ✓ Undo last action successful');

  // Test filter pills
  console.log('  Testing filter selections...');
  global.window.App.selectStatusFilter('new');
  global.window.App.selectStatusFilter('all');
  console.log('  ✓ Filter selection successful');

  console.log('\nBoot test & user workflow passed! 🚀\n');
  process.exit(0);
}

runBootTest().catch(err => {
  console.error('\nBoot test FAILED:');
  console.error(err);
  process.exit(1);
});
