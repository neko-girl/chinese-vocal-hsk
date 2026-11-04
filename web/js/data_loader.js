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

  async loadChapter(chapterDir) {
    try {
      const res = await fetch(`chapters/${chapterDir}/data.json`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.json();
    } catch (err) {
      // In local file:// mode, check if already loaded via data.js
      if (window.__HSK_CHAPTER_DATA__ && window.__HSK_CHAPTER_DATA__[chapterDir]) {
        return window.__HSK_CHAPTER_DATA__[chapterDir];
      }
      // Dynamically inject data.js script tag as fallback
      return new Promise((resolve, reject) => {
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
    }
  }
};
