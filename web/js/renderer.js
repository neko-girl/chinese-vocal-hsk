/**
 * Renderer module for Chinese Vocal HSK Visualizer & Anki Flashcard System.
 * Generates DOM structures for sidebar list, front/back flashcard cards, and 8-pill tabs.
 */

// Speech Synthesis Engine
function speak(text) {
  if (!('speechSynthesis' in window)) {
    console.warn('Speech synthesis not supported in this browser.');
    return;
  }

  try {
    window.speechSynthesis.cancel();
    if (!text) return;

    // Extract Chinese characters if text contains translations/notes
    const hanziOnly = (text.match(/[\u4e00-\u9fa5]+/g) || []).join('');
    const toSpeak = hanziOnly || text;

    const u = new SpeechSynthesisUtterance(toSpeak);
    u.lang = 'zh-CN';
    
    // Retrieve speed setting if available
    const settings = (typeof StorageManager !== 'undefined') ? StorageManager.getSettings() : null;
    u.rate = settings?.speechRate || 0.9;

    // Visual feedback on audio buttons
    const activeBtns = document.querySelectorAll('.hero-audio-btn, .audio-btn');
    activeBtns.forEach(b => b.classList.add('speaking'));
    u.onend = () => activeBtns.forEach(b => b.classList.remove('speaking'));
    u.onerror = () => activeBtns.forEach(b => b.classList.remove('speaking'));

    window.speechSynthesis.speak(u);
  } catch (err) {
    console.warn('SpeechSynthesis error:', err);
  }
}

// Tone Coloring Table
const TONE_MARKS = {
  'ā': 1, 'ē': 1, 'ī': 1, 'ō': 1, 'ū': 1, 'ǖ': 1,
  'Ā': 1, 'Ē': 1, 'Ī': 1, 'Ō': 1, 'Ū': 1, 'Ǖ': 1,
  'á': 2, 'é': 2, 'í': 2, 'ó': 2, 'ú': 2, 'ǘ': 2,
  'Á': 2, 'É': 2, 'Í': 2, 'Ó': 2, 'Ú': 2, 'Ǘ': 2, 'ń': 2, 'ḿ': 2,
  'ǎ': 3, 'ě': 3, 'ǐ': 3, 'ǒ': 3, 'ǔ': 3, 'ǚ': 3,
  'Ǎ': 3, 'Ě': 3, 'Ǐ': 3, 'Ǒ': 3, 'Ǔ': 3, 'Ǚ': 3, 'ň': 3,
  'à': 4, 'è': 4, 'ì': 4, 'ò': 4, 'ù': 4, 'ǜ': 4,
  'À': 4, 'È': 4, 'Ì': 4, 'Ò': 4, 'Ù': 4, 'Ǜ': 4, 'ǹ': 4
};

function getToneClass(syllable) {
  for (let i = 0; i < syllable.length; i++) {
    const t = TONE_MARKS[syllable[i]];
    if (t) return `tone-${t}`;
  }
  const numMatch = syllable.match(/[1-5]$/);
  if (numMatch) return `tone-${numMatch[0]}`;
  return 'tone-5';
}

function colorizePinyinHTML(text) {
  if (!text) return '';
  const tokenRegex = /([bcdfghjklmnpqrstwxyzBCDFGHJKLMNPQRSTWXYZ]*[aeiouvüAEIOUVÜāēīōūǖáéíóúǘǎěǐǒǔǚàèìòùǜńňḿ]+(?:ng|n|r)?[1-5]?|(?:ng|m|n)[1-5]?|[^a-zA-ZüÜāēīōūǖáéíóúǘǎěǐǒǔǚàèìòùǜńňḿ0-9]+|[0-9]+)/gi;
  const tokens = text.match(tokenRegex);
  if (!tokens) return text;
  return tokens.map(tok => {
    if (/[a-zA-ZüÜāēīōūǖáéíóúǘǎěǐǒǔǚàèìòùǜńňḿ]/.test(tok)) {
      return `<span class="${getToneClass(tok)}">${tok}</span>`;
    }
    return tok;
  }).join('');
}

// Compute Chao Tone Pitch Contour (e.g. 51-35)
function computeToneContour(pinyin) {
  if (!pinyin) return '';
  const tokenRegex = /([bcdfghjklmnpqrstwxyzBCDFGHJKLMNPQRSTWXYZ]*[aeiouvüAEIOUVÜāēīōūǖáéíóúǘǎěǐǒǔǚàèìòùǜńňḿ]+(?:ng|n|r)?[1-5]?|(?:ng|m|n)[1-5]?)/gi;
  const matches = pinyin.match(tokenRegex);
  if (!matches || matches.length === 0) return '';

  const toneContours = { 1: '55', 2: '35', 3: '214', 4: '51', 5: '·' };
  const contours = [];
  for (let i = 0; i < matches.length; i++) {
    const syl = matches[i];
    let t = 5;
    for (let k = 0; k < syl.length; k++) {
      const mark = TONE_MARKS[syl[k]];
      if (mark) { t = mark; break; }
    }
    const numMatch = syl.match(/[1-5]$/);
    if (numMatch) t = parseInt(numMatch[0], 10);
    contours.push(toneContours[t] || '55');
  }
  return `Pitch: ${contours.join('-')}`;
}

// Render Sidebar List with Review Badges
function renderSidebar(filteredWords, allWords, currentWordId, currentLang, onSelect, chapterReviews = {}) {
  const listEl = document.getElementById('word-list');
  if (!listEl) return;
  listEl.innerHTML = '';

  filteredWords.forEach(w => {
    const isSelected = String(w.id) === String(currentWordId);
    const rev = chapterReviews[String(w.id)];
    const status = rev?.status || 'new';

    const item = document.createElement('div');
    item.className = `word-item ${isSelected ? 'active' : ''}`;
    item.innerHTML = `
      <div style="display: flex; align-items: center;">
        <span class="word-review-indicator status-${status}" title="Review status: ${status}"></span>
        <div class="num">${String(w.id).padStart(2, '0')}</div>
      </div>
      <div class="meta-col">
        <div style="display: flex; align-items: baseline; justify-content: space-between;">
          <span class="hanzi-sm">${w.hanzi}</span>
          <span class="pos-tag">${w.part_of_speech}</span>
        </div>
        <div class="pinyin-sm">${w.pinyin}</div>
        <div class="meaning-sm">${currentLang === 'es' ? (w.meanings_summary?.es || '') : (w.meanings_summary?.en || '')}</div>
      </div>
    `;
    item.onclick = () => onSelect(w.id);
    listEl.appendChild(item);
  });
}

// Generate Flashcard Front View
function renderFlashcardFront(w, chapterDir, reviewItem) {
  const status = reviewItem?.status || 'new';
  let statusBadge = '<span class="badge" style="background: rgba(148, 163, 184, 0.15); color: var(--text-dim);">New Card</span>';
  if (status === 'remembered') {
    statusBadge = `<span class="badge" style="background: rgba(16, 185, 129, 0.15); color: var(--accent-green);">🟢 Box ${reviewItem.srsLevel || 1}</span>`;
  } else if (status === 'dont_remember') {
    statusBadge = `<span class="badge" style="background: rgba(239, 68, 68, 0.15); color: #ef4444;">🔴 Lapsed (${reviewItem.lapses || 1}x)</span>`;
  }

  return `
    <div class="card-container front-card">
      <div class="card-top-bar">
        <div class="card-meta-left">
          <span class="badge badge-hsk">${w.level || 'HSK 5'}</span>
          <span class="badge badge-pos">${w.part_of_speech}</span>
          ${statusBadge}
        </div>
        <div class="card-action-bar">
          <button type="button" class="drawer-trigger-btn" onclick="speak('${w.hanzi}')" title="Pronounce Headword (TTS)">
            🔊
          </button>
          <button type="button" class="drawer-trigger-btn" onclick="App.openLookupDrawer()" title="External Lookups (L)">
            🔍
          </button>
          <button type="button" class="drawer-trigger-btn" onclick="App.openSettingsDrawer()" title="Study Settings (S)">
            ⚙️
          </button>
        </div>
      </div>

      <main class="front-body">
        <div class="hero-word-front" onclick="App.showAnswer()" title="Click or press Space to show answer">${w.hanzi}</div>
        <div class="front-meta-pills">
          <span class="badge badge-num">NO. ${String(w.id).padStart(2, '0')}</span>
          <span class="badge" style="background: var(--bg-card-sub); color: var(--text-muted);">${w.part_of_speech}</span>
        </div>
      </main>

      <div class="card-hint">
        <button type="button" class="hint-pill" onclick="App.showAnswer()">
          <span>💡 Show Answer</span>
          <kbd class="hint-kbd">Space</kbd>
        </button>
      </div>
    </div>
  `;
}

// Generate Flashcard Back View (with Sticky Header & 8 Pill Tabs)
function renderFlashcardBack(w, chapterDir, reviewItem, currentLang, activeTab = 'sentences') {
  const showEn = currentLang === 'both' || currentLang === 'en';
  const showEs = currentLang === 'both' || currentLang === 'es';
  const contour = computeToneContour(w.pinyin);

  const status = reviewItem?.status || 'new';
  let statusBadge = '<span class="badge" style="background: rgba(148, 163, 184, 0.15); color: var(--text-dim);">New</span>';
  if (status === 'remembered') {
    statusBadge = `<span class="badge" style="background: rgba(16, 185, 129, 0.15); color: var(--accent-green);">🟢 Remembered (Box ${reviewItem.srsLevel || 1})</span>`;
  } else if (status === 'dont_remember') {
    statusBadge = `<span class="badge" style="background: rgba(239, 68, 68, 0.15); color: #ef4444;">🔴 Lapsed (${reviewItem.lapses || 1}x)</span>`;
  }

  // 1. Sentences Panel
  const sentences = w.example_sentences || [];
  const sentencesHtml = sentences.map(sent => `
    <div class="sentence-card">
      <span class="tag-ctx">${sent.id === '#1' ? 'Context: Daily / Life' : 'Context: Formal / Professional'}</span>
      <div class="sentence-hanzi">${sent.hanzi}</div>
      <div class="sentence-pinyin">${colorizePinyinHTML(sent.pinyin)}</div>
      ${showEn ? `<div class="sentence-trans"><strong>EN:</strong> ${sent.en}</div>` : ''}
      ${showEs ? `<div class="sentence-trans"><strong>ES:</strong> ${sent.es}</div>` : ''}
      <div style="margin-top: 10px;">
        <button class="btn btn-icon" style="padding: 3px 8px; font-size: 0.75rem;" onclick="speak('${sent.hanzi}')">🔊 Listen</button>
      </div>
    </div>
  `).join('');

  // 2. Collocations Panel
  const collocations = w.collocations || [];
  const collocHtml = collocations.map(c => `
    <div class="colloc-item" onclick="speak('${c.hanzi}')">
      <div class="colloc-hanzi">
        <span>${c.hanzi}</span>
        <span style="font-size: 0.8rem; color: var(--primary);">🔊</span>
      </div>
      <div class="colloc-en">${c.en}</div>
    </div>
  `).join('');

  // 3. Idioms Panel
  const idioms = w.idioms || [];
  const idiomsHtml = idioms.map(im => `
    <div class="colloc-item" onclick="speak('${im.hanzi}')">
      <div class="colloc-hanzi">
        <span>${im.hanzi}</span>
        <span style="font-size: 0.8rem; color: var(--primary);">🔊</span>
      </div>
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">${colorizePinyinHTML(im.pinyin)}</div>
      <div class="colloc-en">${im.meaning_en}</div>
    </div>
  `).join('');

  // 4. Character Decomposition Panel
  const decomp = w.character_decomposition || [];
  const decompHtml = decomp.map(ch => `
    <div class="decomp-card">
      <div class="decomp-header">
        <div class="char-big">${ch.character}</div>
        <div class="char-meta-top">
          <div style="display: flex; align-items: baseline; gap: 8px;">
            <span class="char-pinyin">${colorizePinyinHTML(ch.pinyin)}</span>
            <span class="badge badge-pos">Tone ${ch.tone_mnemonic_anchor}</span>
            <button class="btn btn-icon" style="padding: 2px 6px; font-size: 0.7rem;" onclick="speak('${ch.character}')">🔊</button>
          </div>
          <div class="char-pills">
            <span class="pill-sm">Rad: ${ch.radical} (${ch.radical_meaning_en})</span>
            <span class="pill-sm">${ch.stroke_count} strokes</span>
            <span class="pill-sm">${ch.composition_type}</span>
            ${ch.cangjie ? `<span class="pill-sm">CJ: ${ch.cangjie}</span>` : ''}
            ${ch.traditional ? `<span class="pill-sm">Trad: ${ch.traditional}</span>` : ''}
          </div>
        </div>
      </div>
      <div class="decomp-detail-row">
        <strong>Components:</strong> Meaning ${ch.meaning_component} · Sound ${ch.sound_component}
      </div>
      <div class="decomp-detail-row">
        <strong>Etymology:</strong> ${ch.etymology_and_mnemonic}
      </div>
      ${showEn && ch.visual_mnemonic_story_en ? `<div class="mnemonic-story"><strong>Visual Hook (EN):</strong> ${ch.visual_mnemonic_story_en}</div>` : ''}
      ${showEs && ch.visual_mnemonic_story_es ? `<div class="mnemonic-story" style="border-left-color: var(--accent-green);"><strong>Visual Hook (ES):</strong> ${ch.visual_mnemonic_story_es}</div>` : ''}
    </div>
  `).join('');

  // 5. Mnemonics Panel
  const mr = w.mnemonics_and_roots || {};
  const mnemonicsHtml = `
    <div style="display: flex; flex-direction: column; gap: 12px;">
      ${showEn && mr.composite_memory_hook_en ? `
        <div class="alert-box">
          <div class="alert-title">Composite Memory Hook (EN)</div>
          <div style="font-size: 0.9rem;">${mr.composite_memory_hook_en}</div>
        </div>` : ''}
      ${showEs && mr.composite_memory_hook_es ? `
        <div class="alert-box" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.3);">
          <div class="alert-title" style="color: var(--accent-green);">Gancho Mnemotécnico Compuesto (ES)</div>
          <div style="font-size: 0.9rem;">${mr.composite_memory_hook_es}</div>
        </div>` : ''}
      ${mr.cultural_and_cognitive_roots ? `
        <div class="alert-box blue">
          <div class="alert-title">Cultural & Cognitive Metaphor</div>
          <div style="font-size: 0.88rem; line-height: 1.6;">${mr.cultural_and_cognitive_roots}</div>
        </div>` : ''}
      ${mr.tone_sandhi_and_pitch_modulation ? `
        <div class="alert-box" style="background: rgba(168, 85, 247, 0.08); border-color: rgba(168, 85, 247, 0.3);">
          <div class="alert-title" style="color: var(--accent-purple);">Tone Sandhi & Pitch Contours</div>
          <div style="font-size: 0.88rem; line-height: 1.6;">${mr.tone_sandhi_and_pitch_modulation}</div>
        </div>` : ''}
    </div>
  `;

  // 6. Traps & Cognates Panel
  const traps = w.traps_and_cognates || {};
  const lookAlikes = traps.look_alikes || [];
  const lookAlikesHtml = lookAlikes.map(la => `
    <tr>
      <td class="char-cell" onclick="speak('${la.character}')">${la.character} <span style="font-size: 0.75rem; cursor: pointer;">🔊</span></td>
      <td style="font-family: 'JetBrains Mono', monospace;">${colorizePinyinHTML(la.pinyin)}</td>
      <td>${la.meaning_en}</td>
      <td style="color: var(--text-muted); font-size: 0.8rem;">${la.distinction_note}</td>
    </tr>
  `).join('');

  const cognates = traps.etymological_cognates || [];
  const cognatesHtml = cognates.map(cg => `
    <div class="cognate-chip" onclick="speak('${cg.character}')">
      <span class="ch">${cg.character}</span>
      <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem;">${colorizePinyinHTML(cg.pinyin)}</span>
      <span style="color: var(--text-dim); font-size: 0.72rem;">${cg.gloss_en}</span>
    </div>
  `).join('');

  const trapsHtml = `
    <div style="margin-bottom: 16px;">
      <div style="font-weight: 700; font-size: 0.88rem; margin-bottom: 8px;">Look-Alike Characters (字形陷阱)</div>
      <table class="data-table">
        <thead>
          <tr><th>Char</th><th>Pinyin</th><th>Meaning</th><th>Distinction</th></tr>
        </thead>
        <tbody>${lookAlikesHtml}</tbody>
      </table>
    </div>
    <div>
      <div style="font-weight: 700; font-size: 0.88rem; margin-bottom: 8px;">Etymological Cognates Family (同族字)</div>
      <div class="cognate-chips">${cognatesHtml}</div>
    </div>
  `;

  // 7. Contrasts Panel
  const sbc = w.semantic_boundary_contrasts || {};
  const contrasts = sbc.contrasts || [];
  const contrastsHtml = contrasts.map(ct => `
    <div class="contrast-item">
      <div class="contrast-header">
        <span class="contrast-pair">${ct.compared_word}</span>
        <span class="contrast-pinyin">${colorizePinyinHTML(ct.pinyin)}</span>
      </div>
      <div class="contrast-desc">${ct.analysis}</div>
    </div>
  `).join('');

  const synonymsHtml = `
    ${sbc.core_nuance ? `
      <div style="margin-bottom: 14px; font-size: 0.92rem; color: var(--text); padding: 10px 14px; background: var(--bg-card-sub); border-radius: 8px; border: 1px solid var(--border);">
        <strong>Core Semantic Nuance:</strong> ${sbc.core_nuance}
      </div>` : ''}
    <div>${contrastsHtml}</div>
  `;

  // 8. Passages Panel
  const passages = w.extended_reading_passages || [];
  const passagesHtml = passages.map((p, idx) => `
    <div class="passage-block">
      <div class="passage-header">
        <span class="passage-badge">${idx === 0 ? 'Passage #1: Reflective / Philosophical' : 'Passage #2: Socio-economic / Formal'}</span>
        <button class="btn btn-icon" onclick="speak('${p.hanzi}')">🔊 Read Passage</button>
      </div>
      <div class="passage-hanzi">${p.hanzi}</div>
      <div class="passage-pinyin">${colorizePinyinHTML(p.pinyin)}</div>
      ${showEn ? `<div class="passage-trans" style="margin-bottom: 8px;"><strong>EN:</strong> ${p.en}</div>` : ''}
      ${showEs ? `<div class="passage-trans"><strong>ES:</strong> ${p.es}</div>` : ''}
    </div>
  `).join('');

  return `
    <div class="card-container back-card">
      <!-- Persistent Header -->
      <header class="card-header-sticky">
        <div class="hero-top-row">
          <div class="hero-badges">
            <span class="badge badge-num">NO. ${String(w.id).padStart(2, '0')}</span>
            <span class="badge badge-hsk">${w.level || 'HSK 5'}</span>
            <span class="badge badge-pos">${w.part_of_speech}</span>
            ${contour ? `<span class="badge tone-contour-badge">${contour}</span>` : ''}
            ${statusBadge}
          </div>
          <div class="card-action-bar">
            <button type="button" class="drawer-trigger-btn" onclick="speak('${w.hanzi}')" title="Pronounce Headword (R)">
              🔊
            </button>
            <button type="button" class="drawer-trigger-btn" onclick="App.openLookupDrawer()" title="External Lookups (L)">
              🔍
            </button>
            <button type="button" class="drawer-trigger-btn" onclick="App.openSettingsDrawer()" title="Study Settings (S)">
              ⚙️
            </button>
          </div>
        </div>

        <div style="display: flex; align-items: baseline; gap: 12px;">
          <div class="hero-word" onclick="speak('${w.hanzi}')" title="Click to pronounce">${w.hanzi}</div>
          <div class="hero-pinyin">${colorizePinyinHTML(w.pinyin)}</div>
        </div>

        <!-- Bilingual Meanings Summary -->
        <div class="meanings-container">
          ${showEn && w.meanings_summary?.en ? `
            <div class="meaning-row"><span class="lang-tag en">EN</span> ${w.meanings_summary.en}</div>` : ''}
          ${showEs && w.meanings_summary?.es ? `
            <div class="meaning-row"><span class="lang-tag es">ES</span> ${w.meanings_summary.es}</div>` : ''}
        </div>
      </header>

      <!-- 8-Pill Segmented Navigation Bar -->
      <nav class="pill-nav-container" aria-label="Vocabulary Sections">
        <div class="pill-nav-track" role="tablist">
          <button type="button" class="pill-btn ${activeTab === 'sentences' ? 'active' : ''}" onclick="App.switchTab('sentences')">
            <span class="pill-icon">💬</span>
            <span class="pill-text">例句</span>
            <span class="pill-key">1</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'collocations' ? 'active' : ''}" onclick="App.switchTab('collocations')">
            <span class="pill-icon">⚡</span>
            <span class="pill-text">搭配</span>
            <span class="pill-key">2</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'idioms' ? 'active' : ''}" onclick="App.switchTab('idioms')">
            <span class="pill-icon">📜</span>
            <span class="pill-text">成语</span>
            <span class="pill-key">3</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'decomp' ? 'active' : ''}" onclick="App.switchTab('decomp')">
            <span class="pill-icon">🧩</span>
            <span class="pill-text">字形</span>
            <span class="pill-key">4</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'mnemonics' ? 'active' : ''}" onclick="App.switchTab('mnemonics')">
            <span class="pill-icon">🧠</span>
            <span class="pill-text">助记</span>
            <span class="pill-key">5</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'traps' ? 'active' : ''}" onclick="App.switchTab('traps')">
            <span class="pill-icon">⚠️</span>
            <span class="pill-text">形近</span>
            <span class="pill-key">6</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'synonyms' ? 'active' : ''}" onclick="App.switchTab('synonyms')">
            <span class="pill-icon">🎯</span>
            <span class="pill-text">辨析</span>
            <span class="pill-key">7</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'passages' ? 'active' : ''}" onclick="App.switchTab('passages')">
            <span class="pill-icon">📖</span>
            <span class="pill-text">篇章</span>
            <span class="pill-key">8</span>
          </button>
        </div>
      </nav>

      <!-- 8 Dynamic Tab Panels -->
      <div class="tab-viewport">
        <section class="tab-panel ${activeTab === 'sentences' ? 'active' : ''}" id="panel-sentences">
          ${sentencesHtml}
        </section>
        <section class="tab-panel ${activeTab === 'collocations' ? 'active' : ''}" id="panel-collocations">
          <div class="colloc-grid">${collocHtml}</div>
        </section>
        <section class="tab-panel ${activeTab === 'idioms' ? 'active' : ''}" id="panel-idioms">
          <div class="colloc-grid">${idiomsHtml}</div>
        </section>
        <section class="tab-panel ${activeTab === 'decomp' ? 'active' : ''}" id="panel-decomp">
          <div class="decomp-grid">${decompHtml}</div>
        </section>
        <section class="tab-panel ${activeTab === 'mnemonics' ? 'active' : ''}" id="panel-mnemonics">
          ${mnemonicsHtml}
        </section>
        <section class="tab-panel ${activeTab === 'traps' ? 'active' : ''}" id="panel-traps">
          ${trapsHtml}
        </section>
        <section class="tab-panel ${activeTab === 'synonyms' ? 'active' : ''}" id="panel-synonyms">
          ${synonymsHtml}
        </section>
        <section class="tab-panel ${activeTab === 'passages' ? 'active' : ''}" id="panel-passages">
          ${passagesHtml}
        </section>
      </div>
    </div>
  `;
}

// Render Persistent Bottom Anki Review Bar
function renderActionBar(cardSide, studyMode) {
  const barEl = document.getElementById('anki-action-bar');
  if (!barEl) return;

  if (studyMode === 'browse') {
    barEl.style.display = 'none';
    return;
  }
  barEl.style.display = 'flex';

  if (cardSide === 'front') {
    barEl.innerHTML = `
      <div class="anki-action-group">
        <button type="button" class="btn-action-show" onclick="App.showAnswer()">
          <span>👁️ Show Answer</span>
          <kbd class="action-kbd">Space</kbd>
        </button>
      </div>
    `;
  } else {
    barEl.innerHTML = `
      <div class="anki-action-group">
        <button type="button" class="btn-rate-again" onclick="App.rateCard('dont_remember')" title="Mark as Don't Remember (Shortcut: 1 or A)">
          <span>🔴 Don't Remember</span>
          <kbd class="action-kbd">1</kbd>
        </button>
        <button type="button" class="btn-rate-good" onclick="App.rateCard('remembered')" title="Mark as Remembered (Shortcut: 2 or Space)">
          <span>🟢 Remember</span>
          <kbd class="action-kbd">2 / Space</kbd>
        </button>
      </div>
    `;
  }
}

// Render Session Complete & Chapter Milestone Screen with Auto-Advance Countdown
function renderCompletionScreen(stats, currentChapter, nextChapter, countdownRemaining = 5, isAutoAdvanceEnabled = true, isPaused = false, maxCountdown = 5) {
  const container = document.getElementById('detail-container');
  if (!container) return;

  const barEl = document.getElementById('anki-action-bar');
  if (barEl) barEl.style.display = 'none';

  const chName = currentChapter?.name || 'Chapter';
  const chTitle = currentChapter?.title || 'Review Completed';
  const hasNext = Boolean(nextChapter);
  const percentFill = isPaused ? 0 : Math.max(0, Math.min(100, (countdownRemaining / (maxCountdown || 5)) * 100));

  container.innerHTML = `
    <div class="chapter-milestone-card">
      <div class="milestone-icon">${hasNext ? '🎉' : '🏆'}</div>
      <div class="milestone-badge">${hasNext ? 'Chapter Milestone Complete' : 'HSK 5 Curriculum Mastered'}</div>
      <h2 class="milestone-title">${chName}: ${chTitle}</h2>
      <p class="milestone-desc">
        ${hasNext 
          ? "You've successfully cleared this study round! Every card in this chapter has been actively recalled."
          : "Magnificent achievement! You have mastered all available vocabulary chapters in this curriculum."}
      </p>

      <div class="milestone-stats-grid">
        <div class="milestone-stat-box">
          <div class="milestone-stat-val" style="color: #10b981;">${stats.remembered}</div>
          <div class="milestone-stat-lbl">Remembered (🟢)</div>
        </div>
        <div class="milestone-stat-box">
          <div class="milestone-stat-val" style="color: ${stats.dontRemember > 0 ? '#ef4444' : 'var(--text-dim)'};">${stats.dontRemember}</div>
          <div class="milestone-stat-lbl">Lapses Re-tested</div>
        </div>
        <div class="milestone-stat-box">
          <div class="milestone-stat-val" style="color: var(--primary);">${stats.percent}%</div>
          <div class="milestone-stat-lbl">Mastery Rate</div>
        </div>
      </div>

      ${hasNext && isAutoAdvanceEnabled ? `
        <div class="auto-advance-box">
          <div class="auto-advance-header">
            <span class="auto-advance-title">🚀 Next Up: Automatic Chapter Progression</span>
            <div class="countdown-pill" id="countdown-pill-el">
              ${isPaused 
                ? '<span style="color: #f59e0b;">⏸️ Paused</span>' 
                : `Next chapter in <span class="seconds-val" id="countdown-seconds-num">${countdownRemaining}</span>s`}
            </div>
          </div>
          <div class="auto-advance-target">${nextChapter.name}: ${nextChapter.title || nextChapter.dir}</div>
          <div class="auto-advance-meta">${nextChapter.word_count || 38} words · HSK 5 Level</div>

          <div class="countdown-bar-track">
            <div class="countdown-bar-fill" id="countdown-bar-fill" style="width: ${percentFill}%;"></div>
          </div>
        </div>
      ` : ''}

      <div class="milestone-actions">
        ${hasNext ? `
          <button type="button" class="btn-primary-action" onclick="App.skipToNextChapter()" title="Start immediately (Space / Enter)">
            <span>⏩ Start ${nextChapter.name} Now</span>
            <kbd class="action-kbd" style="background: rgba(0,0,0,0.25); border-color: rgba(0,0,0,0.3); color: #0b0f19;">Space</kbd>
          </button>
          ${isAutoAdvanceEnabled ? (isPaused ? `
            <button type="button" class="btn-secondary-action" onclick="App.resumeAutoAdvance()">
              ▶️ Resume Auto-Advance
            </button>
          ` : `
            <button type="button" class="btn-secondary-action" onclick="App.pauseAutoAdvance()">
              ⏸️ Pause Auto-Advance
            </button>
          `) : ''}
        ` : `
          <button type="button" class="btn-primary-action" onclick="App.restartFromChapter1()">
            ↺ Restart From Chapter 1
          </button>
        `}

        ${stats.dontRemember > 0 ? `
          <button type="button" class="btn-secondary-action" style="color: #ef4444; border-color: rgba(239,68,68,0.4);" onclick="App.filterByReviewStatus('lapses')">
            🔴 Review Lapses (${stats.dontRemember})
          </button>` : ''}

        <button type="button" class="btn-secondary-action" onclick="App.restartQueue()">
          ↺ Repeat This Chapter
        </button>
        <button type="button" class="btn-secondary-action" onclick="App.openWordListDrawer()">
          📑 Open Word List
        </button>
      </div>
    </div>
  `;
}

// Full Browse Mode Renderer
function renderBrowseView(w, currentLang) {
  const container = document.getElementById('detail-container');
  if (!container || !w) return;

  const showEn = currentLang === 'both' || currentLang === 'en';
  const showEs = currentLang === 'both' || currentLang === 'es';
  const contour = computeToneContour(w.pinyin);

  const senses = w.senses || [];
  const sentences = w.example_sentences || [];
  const collocations = w.collocations || [];
  const idioms = w.idioms || [];
  const decomp = w.character_decomposition || [];
  const mr = w.mnemonics_and_roots || {};
  const traps = w.traps_and_cognates || {};
  const sbc = w.semantic_boundary_contrasts || {};
  const passages = w.extended_reading_passages || [];

  container.innerHTML = `
    <!-- Hero Card -->
    <div class="hero-card">
      <div class="hero-top">
        <div class="hero-main">
          <span class="hanzi-hero" onclick="speak('${w.hanzi}')" title="Click to pronounce">${w.hanzi}</span>
          <span class="pinyin-hero">${colorizePinyinHTML(w.pinyin)}</span>
          <button class="audio-btn" title="Pronounce Word" onclick="speak('${w.hanzi}')">🔊</button>
        </div>
        <div class="hero-badges">
          <span class="badge badge-num">NO. ${String(w.id).padStart(2, '0')}</span>
          <span class="badge badge-hsk">${w.level || 'HSK 5'}</span>
          <span class="badge badge-pos">${w.part_of_speech}</span>
          ${contour ? `<span class="badge tone-contour-badge">${contour}</span>` : ''}
          <button type="button" class="btn" style="padding: 2px 10px; font-size: 0.76rem; border-color: var(--primary); color: var(--primary);" onclick="App.studyCurrentWord(${w.id})">
            🗂️ Study This Card
          </button>
        </div>
      </div>
      <div class="hero-summary">
        ${showEn ? `
          <div class="summary-box">
            <div class="label">English Definition</div>
            <div class="text">${w.meanings_summary?.en || ''}</div>
          </div>` : ''}
        ${showEs ? `
          <div class="summary-box">
            <div class="label">Definición en Español</div>
            <div class="text">${w.meanings_summary?.es || ''}</div>
          </div>` : ''}
      </div>
    </div>

    <!-- Senses -->
    <div class="section-card">
      <div class="section-title">Core Lexical Senses (${senses.length})</div>
      ${senses.map(s => `
        <div class="sense-row">
          <div class="sense-meta">
            <span class="badge badge-pos">${s.part_of_speech}</span>
            <span class="badge badge-num">${s.register}</span>
          </div>
          ${showEn ? `<div class="sense-def"><strong>EN:</strong> ${s.definition_en}</div>` : ''}
          ${showEs ? `<div class="sense-def" style="color: var(--text-muted);"><strong>ES:</strong> ${s.definition_es}</div>` : ''}
          <div class="sense-eg" onclick="speak('${s.example_phrase.split(' ')[0]}')">
            <span>🔊 ${s.example_phrase}</span>
          </div>
        </div>
      `).join('')}
    </div>

    <!-- Example Sentences -->
    <div class="section-card">
      <div class="section-title">Contextual Example Sentences (${sentences.length})</div>
      ${sentences.map(sent => `
        <div class="sentence-card">
          <span class="tag-ctx">${sent.id === '#1' ? 'Context: Daily / Life' : 'Context: Formal / Professional'}</span>
          <div class="sentence-hanzi">${sent.hanzi}</div>
          <div class="sentence-pinyin">${colorizePinyinHTML(sent.pinyin)}</div>
          ${showEn ? `<div class="sentence-trans"><strong>EN:</strong> ${sent.en}</div>` : ''}
          ${showEs ? `<div class="sentence-trans"><strong>ES:</strong> ${sent.es}</div>` : ''}
          <div style="margin-top: 10px;">
            <button class="btn btn-icon" style="padding: 3px 8px; font-size: 0.75rem;" onclick="speak('${sent.hanzi}')">🔊 Listen</button>
          </div>
        </div>
      `).join('')}
    </div>

    <!-- Collocations & Idioms -->
    <div class="grid-2">
      <div class="section-card" style="margin-bottom: 0;">
        <div class="section-title">High-Frequency Collocations (${collocations.length})</div>
        <div class="colloc-grid">
          ${collocations.map(c => `
            <div class="colloc-item" onclick="speak('${c.hanzi}')">
              <div class="colloc-hanzi"><span>${c.hanzi}</span> <span style="font-size: 0.8rem; color: var(--primary);">🔊</span></div>
              <div class="colloc-en">${c.en}</div>
            </div>
          `).join('')}
        </div>
      </div>
      <div class="section-card" style="margin-bottom: 0;">
        <div class="section-title">Classical Idioms (成语 ${idioms.length})</div>
        <div class="colloc-grid">
          ${idioms.map(im => `
            <div class="colloc-item" onclick="speak('${im.hanzi}')">
              <div class="colloc-hanzi"><span>${im.hanzi}</span> <span style="font-size: 0.8rem; color: var(--primary);">🔊</span></div>
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem;">${colorizePinyinHTML(im.pinyin)}</div>
              <div class="colloc-en">${im.meaning_en}</div>
            </div>
          `).join('')}
        </div>
      </div>
    </div>
    <div style="height: 20px;"></div>

    <!-- Character Decomposition -->
    <div class="section-card">
      <div class="section-title">Character Decomposition & Etymology (K=${decomp.length})</div>
      <div class="decomp-grid">
        ${decomp.map(ch => `
          <div class="decomp-card">
            <div class="decomp-header">
              <div class="char-big">${ch.character}</div>
              <div class="char-meta-top">
                <div style="display: flex; align-items: baseline; gap: 8px;">
                  <span class="char-pinyin">${colorizePinyinHTML(ch.pinyin)}</span>
                  <span class="badge badge-pos">Tone ${ch.tone_mnemonic_anchor}</span>
                  <button class="btn btn-icon" style="padding: 2px 6px; font-size: 0.7rem;" onclick="speak('${ch.character}')">🔊</button>
                </div>
                <div class="char-pills">
                  <span class="pill-sm">Rad: ${ch.radical} (${ch.radical_meaning_en})</span>
                  <span class="pill-sm">${ch.stroke_count} strokes</span>
                  <span class="pill-sm">${ch.composition_type}</span>
                </div>
              </div>
            </div>
            <div class="decomp-detail-row"><strong>Components:</strong> Meaning ${ch.meaning_component} · Sound ${ch.sound_component}</div>
            <div class="decomp-detail-row"><strong>Etymology:</strong> ${ch.etymology_and_mnemonic}</div>
            ${showEn && ch.visual_mnemonic_story_en ? `<div class="mnemonic-story"><strong>Visual Hook (EN):</strong> ${ch.visual_mnemonic_story_en}</div>` : ''}
            ${showEs && ch.visual_mnemonic_story_es ? `<div class="mnemonic-story" style="border-left-color: var(--accent-green);"><strong>Visual Hook (ES):</strong> ${ch.visual_mnemonic_story_es}</div>` : ''}
          </div>
        `).join('')}
      </div>
    </div>

    <!-- Memory Hooks & Cultural Roots -->
    <div class="section-card">
      <div class="section-title">Memory Hooks & Cultural Foundations</div>
      ${showEn && mr.composite_memory_hook_en ? `
        <div class="alert-box">
          <div class="alert-title">Composite Memory Hook (EN)</div>
          <div style="font-size: 0.9rem;">${mr.composite_memory_hook_en}</div>
        </div>` : ''}
      ${showEs && mr.composite_memory_hook_es ? `
        <div class="alert-box" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.3);">
          <div class="alert-title" style="color: var(--accent-green);">Gancho Mnemotécnico Compuesto (ES)</div>
          <div style="font-size: 0.9rem;">${mr.composite_memory_hook_es}</div>
        </div>` : ''}
      ${mr.cultural_and_cognitive_roots ? `
        <div class="alert-box blue">
          <div class="alert-title">Cultural & Cognitive Metaphor</div>
          <div style="font-size: 0.88rem; line-height: 1.6;">${mr.cultural_and_cognitive_roots}</div>
        </div>` : ''}
      ${mr.tone_sandhi_and_pitch_modulation ? `
        <div class="alert-box" style="background: rgba(168, 85, 247, 0.08); border-color: rgba(168, 85, 247, 0.3);">
          <div class="alert-title" style="color: var(--accent-purple);">Tone Sandhi & Pitch Contours</div>
          <div style="font-size: 0.88rem; line-height: 1.6;">${mr.tone_sandhi_and_pitch_modulation}</div>
        </div>` : ''}
    </div>

    <!-- Look-alikes & Cognates -->
    <div class="grid-2">
      <div class="section-card" style="margin-bottom: 0;">
        <div class="section-title">Look-Alike Characters (字形陷阱)</div>
        <table class="data-table">
          <thead><tr><th>Char</th><th>Pinyin</th><th>Meaning</th><th>Distinction</th></tr></thead>
          <tbody>${(traps.look_alikes || []).map(la => `
            <tr>
              <td class="char-cell" onclick="speak('${la.character}')">${la.character} 🔊</td>
              <td style="font-family: 'JetBrains Mono';">${colorizePinyinHTML(la.pinyin)}</td>
              <td>${la.meaning_en}</td>
              <td style="color: var(--text-muted); font-size: 0.8rem;">${la.distinction_note}</td>
            </tr>
          `).join('')}</tbody>
        </table>
      </div>
      <div class="section-card" style="margin-bottom: 0;">
        <div class="section-title">Etymological Cognates Family (同族字)</div>
        <div class="cognate-chips">
          ${(traps.etymological_cognates || []).map(cg => `
            <div class="cognate-chip" onclick="speak('${cg.character}')">
              <span class="ch">${cg.character}</span>
              <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem;">${colorizePinyinHTML(cg.pinyin)}</span>
              <span style="color: var(--text-dim); font-size: 0.72rem;">${cg.gloss_en}</span>
            </div>
          `).join('')}
        </div>
      </div>
    </div>
    <div style="height: 20px;"></div>

    <!-- Semantic Contrasts -->
    <div class="section-card">
      <div class="section-title">Semantic Boundary Contrasts</div>
      ${sbc.core_nuance ? `<div style="margin-bottom: 14px; font-size: 0.92rem; color: var(--text);"><strong>Core Semantic Nuance:</strong> ${sbc.core_nuance}</div>` : ''}
      ${(sbc.contrasts || []).map(ct => `
        <div class="contrast-item">
          <div class="contrast-header">
            <span class="contrast-pair">${ct.compared_word}</span>
            <span class="contrast-pinyin">${colorizePinyinHTML(ct.pinyin)}</span>
          </div>
          <div class="contrast-desc">${ct.analysis}</div>
        </div>
      `).join('')}
    </div>

    <!-- Extended Reading Passages -->
    <div class="section-card">
      <div class="section-title">Extended Reading Passages (${passages.length})</div>
      ${passages.map((p, idx) => `
        <div class="passage-block">
          <div class="passage-header">
            <span class="passage-badge">${idx === 0 ? 'Passage #1: Reflective' : 'Passage #2: Formal'}</span>
            <button class="btn btn-icon" onclick="speak('${p.hanzi}')">🔊 Read Passage</button>
          </div>
          <div class="passage-hanzi">${p.hanzi}</div>
          <div class="passage-pinyin">${colorizePinyinHTML(p.pinyin)}</div>
          ${showEn ? `<div class="passage-trans" style="margin-bottom: 8px;"><strong>EN:</strong> ${p.en}</div>` : ''}
          ${showEs ? `<div class="passage-trans"><strong>ES:</strong> ${p.es}</div>` : ''}
        </div>
      `).join('')}
    </div>
  `;
}

if (typeof window !== 'undefined') {
  window.speak = speak;
  window.colorizePinyinHTML = colorizePinyinHTML;
  window.computeToneContour = computeToneContour;
  window.renderSidebar = renderSidebar;
  window.renderFlashcardFront = renderFlashcardFront;
  window.renderFlashcardBack = renderFlashcardBack;
  window.renderActionBar = renderActionBar;
  window.renderCompletionScreen = renderCompletionScreen;
  window.renderBrowseView = renderBrowseView;
}

