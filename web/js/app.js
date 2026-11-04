/**
 * Application Controller for Chinese Vocal HSK Visualizer.
 * Coordinates multi-chapter switching, filtering, search, and user preferences.
 */

let chapters = [];
let currentChapter = null;
let WORDS = [];
let filteredWords = [];
let currentIndex = 0;
let currentLang = localStorage.getItem('hsk_lang') || 'both';
let currentPosFilter = 'ALL';

// Initialize Theme
function initTheme() {
  const savedTheme = localStorage.getItem('hsk_theme') || 'dark';
  document.body.setAttribute('data-theme', savedTheme);
}

// Select and render a word by index in WORDS array
function selectWord(index) {
  if (index < 0 || index >= WORDS.length) return;
  currentIndex = index;
  renderDetail(WORDS[currentIndex], currentLang);
  renderSidebar(filteredWords, WORDS, currentIndex, currentLang, selectWordById);
  
  const counterEl = document.getElementById('word-counter');
  if (counterEl) {
    const paddedNum = String(WORDS[currentIndex].id).padStart(2, '0');
    counterEl.textContent = `${paddedNum} / ${WORDS.length}`;
  }

  const scrollContainer = document.getElementById('main-scroll');
  if (scrollContainer) {
    scrollContainer.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function selectWordById(id) {
  const idx = WORDS.findIndex(w => w.id === id);
  if (idx !== -1) {
    selectWord(idx);
  }
}

// Filter logic
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

  renderSidebar(filteredWords, WORDS, currentIndex, currentLang, selectWordById);

  if (filteredWords.length > 0 && !filteredWords.some(item => item.id === WORDS[currentIndex]?.id)) {
    const newIdx = WORDS.findIndex(item => item.id === filteredWords[0].id);
    if (newIdx !== -1) {
      selectWord(newIdx);
    }
  }
}

// Update POS filter chip counts for the active chapter
function updatePosChipCounts() {
  const chips = document.querySelectorAll('.filter-chip');
  chips.forEach(chip => {
    const pos = chip.getAttribute('data-pos');
    if (pos === 'ALL') {
      chip.textContent = `All (${WORDS.length})`;
    } else {
      const count = WORDS.filter(w => (w.part_of_speech || '').toLowerCase().includes(pos.toLowerCase())).length;
      chip.textContent = `${pos} (${count})`;
    }
  });
}

// Switch Chapter
async function switchChapter(chapterDir) {
  const found = chapters.find(c => c.dir === chapterDir) || chapters[0];
  if (!found) return;

  currentChapter = found;
  const pillEl = document.getElementById('chapter-pill');
  if (pillEl) {
    pillEl.textContent = `CHP ${found.id}`;
  }

  // Update chapter select dropdown if different
  const selectEl = document.getElementById('chapter-select');
  if (selectEl && selectEl.value !== found.dir) {
    selectEl.value = found.dir;
  }

  // Load words dataset
  try {
    WORDS = await DataLoader.loadChapter(found.dir);
  } catch (err) {
    console.error(`Failed to load chapter ${found.dir}:`, err);
    return;
  }

  currentIndex = 0;
  currentPosFilter = 'ALL';
  const searchInput = document.getElementById('search-input');
  if (searchInput) searchInput.value = '';

  document.querySelectorAll('.filter-chip').forEach(c => {
    c.classList.toggle('active', c.getAttribute('data-pos') === 'ALL');
  });

  updatePosChipCounts();
  filteredWords = [...WORDS];
  selectWord(0);
}

// Setup Event Handlers
function setupEventListeners() {
  // Search
  const searchInput = document.getElementById('search-input');
  if (searchInput) {
    searchInput.addEventListener('input', applyFilters);
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

  // Language Toggle
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentLang = btn.getAttribute('data-lang');
      localStorage.setItem('hsk_lang', currentLang);
      if (WORDS[currentIndex]) {
        renderDetail(WORDS[currentIndex], currentLang);
      }
      renderSidebar(filteredWords, WORDS, currentIndex, currentLang, selectWordById);
    });
  });

  // Previous & Next Word buttons
  const prevBtn = document.getElementById('prev-btn');
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (currentIndex > 0) selectWord(currentIndex - 1);
    });
  }

  const nextBtn = document.getElementById('next-btn');
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (currentIndex < WORDS.length - 1) selectWord(currentIndex + 1);
    });
  }

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
    if (e.key === 'ArrowLeft' && currentIndex > 0) {
      selectWord(currentIndex - 1);
    } else if (e.key === 'ArrowRight' && currentIndex < WORDS.length - 1) {
      selectWord(currentIndex + 1);
    }
  });

  // Mobile sidebar toggle
  const toggleBtn = document.getElementById('toggle-sidebar-btn');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      document.getElementById('sidebar').classList.toggle('open');
    });
  }

  // Theme toggle
  const themeBtn = document.getElementById('theme-btn');
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const isLight = document.body.getAttribute('data-theme') === 'light';
      const newTheme = isLight ? 'dark' : 'light';
      document.body.setAttribute('data-theme', newTheme);
      localStorage.setItem('hsk_theme', newTheme);
    });
  }

  // Chapter Selector dropdown
  const chapterSelect = document.getElementById('chapter-select');
  if (chapterSelect) {
    chapterSelect.addEventListener('change', (e) => {
      switchChapter(e.target.value);
    });
  }
}

// Main App Initialization
async function initApp() {
  initTheme();
  setupEventListeners();

  // Set initial language button active state
  document.querySelectorAll('.lang-btn').forEach(b => {
    b.classList.toggle('active', b.getAttribute('data-lang') === currentLang);
  });

  // Load manifest
  try {
    chapters = await DataLoader.loadManifest();
  } catch (err) {
    console.error("Failed to load manifest:", err);
    chapters = [{ id: 1, dir: 'chapter_01', name: 'Chapter 1', title: '细节与人际关系', word_count: 38 }];
  }

  // Populate Chapter dropdown
  const chapterSelect = document.getElementById('chapter-select');
  if (chapterSelect) {
    chapterSelect.innerHTML = '';
    chapters.forEach(c => {
      const opt = document.createElement('option');
      opt.value = c.dir;
      opt.textContent = `${c.name}: ${c.title || c.dir} (${c.word_count} words)`;
      chapterSelect.appendChild(opt);
    });
  }

  // Determine initial chapter
  const urlParams = new URLSearchParams(window.location.search);
  const requestedCh = urlParams.get('ch');
  let initialDir = chapters[0]?.dir || 'chapter_01';
  if (requestedCh) {
    const match = chapters.find(c => String(c.id) === requestedCh || c.dir === requestedCh);
    if (match) initialDir = match.dir;
  }

  await switchChapter(initialDir);
}

// Start on DOM ready
document.addEventListener('DOMContentLoaded', initApp);
