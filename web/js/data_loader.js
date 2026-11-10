/**
 * DataLoader handles fetching and caching of chapter manifests and word datasets.
 * Works seamlessly across both HTTP web servers and local file:// browsing.
 */
const DataLoader = {
  async loadManifest() {
    try {
      const res = await fetch('data/chapters.json');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.json();
    } catch (err) {
      // Check for global script fallback (file:// protocol)
      if (window.__HSK_CHAPTERS_MANIFEST__) {
        return window.__HSK_CHAPTERS_MANIFEST__;
      }
      // Default to Chapter 1 if no manifest is reachable
      return [{
        id: 1,
        dir: 'chapter_01',
        name: 'Chapter 1',
        title: '细节与人际关系 (Details & Relationships)',
        word_count: 38
      }];
    }
  },

  /**
   * Normalizes word object fields so translation, meanings_summary, and chapterId
   * are uniformly available regardless of JSON / JS source schema.
   */
  normalizeWords(rawWords, chapterDir) {
    if (!Array.isArray(rawWords)) return [];
    return rawWords.map(w => {
      const en = w.meanings_summary?.en ||
        (Array.isArray(w.translations?.en) ? w.translations.en.join('; ') : w.translations?.en) ||
        (Array.isArray(w.senses) ? w.senses.map(s => s.definition_en).filter(Boolean).join('; ') : '') ||
        w.meaning_en || w.meaning || '';

      const es = w.meanings_summary?.es ||
        (Array.isArray(w.translations?.es) ? w.translations.es.join('; ') : w.translations?.es) ||
        (Array.isArray(w.senses) ? w.senses.map(s => s.definition_es).filter(Boolean).join('; ') : '') ||
        w.meaning_es || '';

      const enList = Array.isArray(w.translations?.en)
        ? w.translations.en
        : (en ? en.split(/[;,]/).map(s => s.trim()).filter(Boolean) : []);

      const esList = Array.isArray(w.translations?.es)
        ? w.translations.es
        : (es ? es.split(/[;,]/).map(s => s.trim()).filter(Boolean) : []);

      return {
        ...w,
        chapterId: w.chapterId || chapterDir,
        meaning: w.meaning || en,
        meaning_en: w.meaning_en || en,
        meaning_es: w.meaning_es || es,
        meanings_summary: {
          en: w.meanings_summary?.en || en,
          es: w.meanings_summary?.es || es
        },
        translations: {
          en: enList,
          es: esList
        }
      };
    });
  },

  async loadChapter(chapterDir) {
    let raw = null;
    try {
      const res = await fetch(`chapters/${chapterDir}/data.json`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      raw = await res.json();
    } catch (err) {
      // In local file:// mode, check if already loaded via data.js
      if (typeof window !== 'undefined' && window.__HSK_CHAPTER_DATA__ && window.__HSK_CHAPTER_DATA__[chapterDir]) {
        raw = window.__HSK_CHAPTER_DATA__[chapterDir];
      } else if (typeof document !== 'undefined') {
        // Dynamically inject data.js script tag as fallback
        raw = await new Promise((resolve, reject) => {
          const script = document.createElement('script');
          script.src = `chapters/${chapterDir}/data.js`;
          script.onload = () => {
            if (window.__HSK_CHAPTER_DATA__ && window.__HSK_CHAPTER_DATA__[chapterDir]) {
              resolve(window.__HSK_CHAPTER_DATA__[chapterDir]);
            } else {
              reject(new Error(`Failed to load dataset for ${chapterDir}`));
            }
          };
          script.onerror = () => reject(new Error(`Could not find chapters/${chapterDir}/data.js`));
          document.head.appendChild(script);
        });
      } else {
        throw new Error(`Cannot load chapter ${chapterDir} in this environment`);
      }
    }
    return this.normalizeWords(raw, chapterDir);
  },

  /**
   * Load all chapters from manifest in parallel
   */
  async loadAllChapters() {
    const manifest = await this.loadManifest();
    const map = {};
    const promises = manifest.map(async (ch) => {
      try {
        const words = await this.loadChapter(ch.dir);
        map[ch.dir] = words;
      } catch (e) {
        console.warn(`Could not load chapter ${ch.dir}:`, e);
        map[ch.dir] = [];
      }
    });
    await Promise.all(promises);
    return { manifest, chaptersMap: map };
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = DataLoader;
}
