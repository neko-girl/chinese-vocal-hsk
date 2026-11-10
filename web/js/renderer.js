/**
 * Renderer module for Chinese Vocal HSK Visualizer & Anki Flashcard System.
 * Generates DOM structures for sidebar list, front/back flashcard cards, and 8-pill tabs.
 */

// Speech & Native Audio Engine with Multi-Voice Randomization
function speak(textOrAudio, speed, triggerEl) {
  if (typeof AudioManager !== 'undefined') {
    // If an audio object was passed directly
    if (typeof textOrAudio === 'object' && textOrAudio !== null) {
      AudioManager.play(textOrAudio, '', speed, triggerEl);
      return;
    }

    const textStr = String(textOrAudio || '').trim();
    if (!textStr) return;

    // Check if the current word has audio for this text item
    const currentWord = (typeof App !== 'undefined' && App.getCurrentWord) ? App.getCurrentWord() : null;
    let matchingAudio = null;

    if (currentWord) {
      if (textStr === currentWord.hanzi) {
        matchingAudio = currentWord.audio;
      } else {
        // Example sentences
        const sent = (currentWord.example_sentences || []).find(s => s.hanzi === textStr);
        if (sent?.audio) matchingAudio = sent.audio;

        // Collocations
        if (!matchingAudio) {
          const col = (currentWord.collocations || []).find(c => c.hanzi === textStr);
          if (col?.audio) matchingAudio = col.audio;
        }

        // Idioms
        if (!matchingAudio) {
          const im = (currentWord.idioms || []).find(i => i.hanzi === textStr);
          if (im?.audio) matchingAudio = im.audio;
        }

        // Reading passages
        if (!matchingAudio) {
          const p = (currentWord.extended_reading_passages || []).find(p => p.hanzi === textStr);
          if (p?.audio) matchingAudio = p.audio;
        }

        // Character decomposition
        if (!matchingAudio) {
          const ch = (currentWord.character_decomposition || []).find(c => c.character === textStr);
          if (ch?.audio) matchingAudio = ch.audio;
        }

        // Look-alikes
        if (!matchingAudio) {
          const la = (currentWord.traps_and_cognates?.look_alikes || []).find(l => l.character === textStr);
          if (la?.audio) matchingAudio = la.audio;
        }

        // Cognates
        if (!matchingAudio) {
          const cg = (currentWord.traps_and_cognates?.etymological_cognates || []).find(c => c.character === textStr);
          if (cg?.audio) matchingAudio = cg.audio;
        }
      }
    }

    AudioManager.play(matchingAudio, textStr, speed, triggerEl);
    return;
  }

  // Fallback if AudioManager is not loaded
  if (!('speechSynthesis' in window)) {
    console.warn('Speech synthesis not supported in this browser.');
    return;
  }

  try {
    window.speechSynthesis.cancel();
    if (!textOrAudio) return;

    const hanziOnly = (String(textOrAudio).match(/[\u4e00-\u9fa5]+/g) || []).join('');
    const toSpeak = hanziOnly || textOrAudio;

    const u = new SpeechSynthesisUtterance(toSpeak);
    u.lang = 'zh-CN';
    
    const settings = (typeof StorageManager !== 'undefined') ? StorageManager.getSettings() : null;
    u.rate = (typeof speed === 'number') ? speed : (settings?.speechRate || 0.9);

    const activeBtns = document.querySelectorAll('.hero-audio-btn, .audio-btn, .audio-speed-btn');
    activeBtns.forEach(b => b.classList.add('speaking'));
    u.onend = () => activeBtns.forEach(b => b.classList.remove('speaking'));
    u.onerror = () => activeBtns.forEach(b => b.classList.remove('speaking'));

    window.speechSynthesis.speak(u);
  } catch (err) {
    console.warn('SpeechSynthesis error:', err);
  }
}

// Highlight Target Headword in Sentences and Passages
function highlightHeadword(text, headword) {
  if (!text || !headword) return text || '';
  const escaped = headword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const regex = new RegExp(`(${escaped})`, 'g');
  return text.replace(regex, '<mark class="target-headword">$1</mark>');
}

// Universal Translation & Definition Extraction Helper
function getWordTranslation(w, lang = 'both') {
  if (!w) return '';
  const en = w.meanings_summary?.en ||
    (Array.isArray(w.translations?.en) ? w.translations.en.join('; ') : w.translations?.en) ||
    (Array.isArray(w.senses) ? w.senses.map(s => s.definition_en).filter(Boolean).join('; ') : '') ||
    w.meaning_en || w.meaning || '';

  const es = w.meanings_summary?.es ||
    (Array.isArray(w.translations?.es) ? w.translations.es.join('; ') : w.translations?.es) ||
    (Array.isArray(w.senses) ? w.senses.map(s => s.definition_es).filter(Boolean).join('; ') : '') ||
    w.meaning_es || '';

  if (lang === 'en') return en;
  if (lang === 'es') return es;
  if (en && es) return `${en} / ${es}`;
  return en || es || '';
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

function renderSRSStatusBadge(reviewItem) {
  if (!reviewItem || reviewItem.state === 'new') {
    return '<span class="card-srs-badge badge-new" title="New unlearned word">🔵 New</span>';
  }
  if (reviewItem.state === 'learning') {
    const stepLabel = (reviewItem.step === 1) ? 'Step 2/2' : 'Step 1/2';
    return `<span class="card-srs-badge badge-learning" title="Intra-session learning step">🟠 Learning: ${stepLabel}</span>`;
  }
  if (reviewItem.state === 'relearning') {
    return `<span class="card-srs-badge badge-relearning" title="Lapsed card in re-learning">🔴 Relearning • Lapse ${reviewItem.lapses || 1}</span>`;
  }
  // review
  const intDays = reviewItem.interval || 1;
  return `<span class="card-srs-badge badge-review" title="Graduated spaced repetition review">🟢 Review • ${intDays}d</span>`;
}

function renderChapterOriginBadge(chapterDir) {
  if (!chapterDir) return '';
  const num = chapterDir.match(/\d+/) ? parseInt(chapterDir.match(/\d+/)[0], 10) : '';
  return num ? `<span class="card-origin-badge">📖 CHP ${num}</span>` : '';
}

// Generate Flashcard Front View
function renderFlashcardFront(w, chapterDir, reviewItem) {
  const statusBadge = renderSRSStatusBadge(reviewItem);
  const originBadge = renderChapterOriginBadge(w.chapterId || chapterDir);

  const decomp = w.character_decomposition || [];
  const radicalHint = decomp.map(d => `${d.character}: ${d.radical} (${d.radical_meaning_en || ''})`).join(' · ');

  const settings = (typeof StorageManager !== 'undefined') ? StorageManager.getSettings() : {};
  const isAudioFirst = !!settings.audioFirstMode;
  const blurClass = isAudioFirst ? 'audio-first-blur' : '';

  return `
    <div class="card-container front-card">
      <div class="card-top-bar">
        <div class="card-meta-left">
          ${originBadge}
          <span class="badge badge-hsk">${w.level || 'HSK 5'}</span>
          <span class="badge badge-pos">${w.part_of_speech}</span>
          ${statusBadge}
        </div>
        <div class="card-action-bar">
          <div class="audio-control-cluster">
            <button type="button" class="audio-speed-btn" onclick="speak('${w.hanzi}', 0.75)" title="Slow Pronunciation (0.75x)">
              🐢 0.75x
            </button>
            <button type="button" class="audio-speed-btn" onclick="speak('${w.hanzi}', 1.0)" title="Normal Pronunciation (1.0x)">
              🔊 1.0x
            </button>
          </div>
          <button type="button" class="drawer-trigger-btn" onclick="App.openLookupDrawer()" title="External Lookups">
            🔍
          </button>
          <button type="button" class="drawer-trigger-btn" onclick="App.openSettingsDrawer()" title="Configuration & Settings">
            ⚙️
          </button>
        </div>
      </div>

      <main class="front-body">
        <div class="tianzige-container">
          <div class="tianzige-box ${w.hanzi.length > 2 ? 'tianzige-box-multi' : ''} ${blurClass}" id="front-tianzige-box" onclick="App.handleFrontHanziClick(this)" title="${isAudioFirst ? 'Listening Mode: Click or press H to reveal Hanzi' : 'Click or press Space to reveal answer'}">
            <div class="tianzige-char">${w.hanzi}</div>
          </div>
        </div>
        ${isAudioFirst ? `
          <div class="audio-first-indicator" onclick="App.unblurFrontHanzi()" title="Click to reveal Hanzi (or press H)">
            🎧 Listening Mode (Tap or press H to reveal)
          </div>
        ` : ''}

        <div class="front-meta-pills">
          <span class="badge badge-num">NO. ${String(w.id).padStart(2, '0')}</span>
          <span class="badge" style="background: var(--bg-card-sub); color: var(--text-muted);">${w.part_of_speech}</span>
          ${w.level ? `<span class="badge badge-hsk">${w.level}</span>` : ''}
        </div>

        <!-- Progressive Hints -->
        <div class="front-hint-section">
          <button type="button" class="btn-peek-hint" onclick="App.toggleFrontHint()">
            <span>💡 Peek Hint</span>
          </button>
          <div id="front-hint-content" class="hint-content-box">
            <div style="font-size: 0.85rem; margin-bottom: 4px;"><strong>Pinyin:</strong> ${colorizePinyinHTML(w.pinyin)}</div>
            ${getWordTranslation(w, 'both') ? `<div style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 4px;"><strong>Meaning:</strong> ${getWordTranslation(w, 'both')}</div>` : ''}
            ${radicalHint ? `<div style="font-size: 0.76rem; color: var(--text-dim);"><strong>Radicals:</strong> ${radicalHint}</div>` : ''}
          </div>
        </div>
      </main>

      <div class="card-hint">
        <button type="button" class="hint-pill" onclick="App.showAnswer()">
          <span>👁️ Show Answer</span>
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

  const statusBadge = renderSRSStatusBadge(reviewItem);
  const originBadge = renderChapterOriginBadge(w.chapterId || chapterDir);

  // 1. Sentences Panel (with target word highlighting and dual-speed audio)
  const sentences = w.example_sentences || [];
  const sentencesHtml = sentences.map(sent => `
    <div class="sentence-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span class="tag-ctx">${sent.id === '#1' ? 'Context: Daily / Life' : 'Context: Formal / Professional'}</span>
        <button type="button" class="btn-copy-sent" onclick="App.copyText('${sent.hanzi.replace(/'/g, "\\'")}', 'Sentence copied!')" title="Copy Sentence">
          📋 Copy
        </button>
      </div>
      <div class="sentence-hanzi">${highlightHeadword(sent.hanzi, w.hanzi)}</div>
      <div class="sentence-pinyin">${colorizePinyinHTML(sent.pinyin)}</div>
      ${showEn ? `<div class="sentence-trans"><strong>EN:</strong> ${sent.en}</div>` : ''}
      ${showEs ? `<div class="sentence-trans"><strong>ES:</strong> ${sent.es}</div>` : ''}
      <div style="margin-top: 10px; display: flex; gap: 8px;">
        <button class="audio-speed-btn" onclick="speak('${sent.hanzi.replace(/'/g, "\\'")}', 1.0)">🔊 Listen</button>
        <button class="audio-speed-btn" onclick="speak('${sent.hanzi.replace(/'/g, "\\'")}', 0.75)">🐢 0.75x</button>
      </div>
    </div>
  `).join('');

  // 2. Collocations Panel
  const collocations = w.collocations || [];
  const collocHtml = collocations.map(c => `
    <div class="colloc-item" onclick="speak('${c.hanzi.replace(/'/g, "\\'")}', 1.0)">
      <div class="colloc-hanzi">
        <span>${highlightHeadword(c.hanzi, w.hanzi)}</span>
        <span style="font-size: 0.8rem; color: var(--primary);">🔊</span>
      </div>
      <div class="colloc-en">${c.en}</div>
    </div>
  `).join('');

  // 3. Idioms Panel
  const idioms = w.idioms || [];
  const idiomsHtml = idioms.map(im => `
    <div class="colloc-item" onclick="speak('${im.hanzi.replace(/'/g, "\\'")}', 1.0)">
      <div class="colloc-hanzi">
        <span>${highlightHeadword(im.hanzi, w.hanzi)}</span>
        <span style="font-size: 0.8rem; color: var(--primary);">🔊</span>
      </div>
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">${colorizePinyinHTML(im.pinyin)}</div>
      <div class="colloc-en">${im.meaning_en}</div>
    </div>
  `).join('');

  // 4. Character Decomposition Panel (with Tianzige Box)
  const decomp = w.character_decomposition || [];
  const decompHtml = decomp.map(ch => `
    <div class="decomp-card">
      <div class="decomp-header">
        <div class="tianzige-box" style="width: 64px; height: 64px; min-width: 64px; border-radius: 12px; cursor: pointer;" onclick="speak('${ch.character}', 1.0)" title="Pronounce character">
          <div class="tianzige-char" style="font-size: 2.2rem;">${ch.character}</div>
        </div>
        <div class="char-meta-top" style="flex: 1;">
          <div style="display: flex; align-items: baseline; gap: 8px;">
            <span class="char-pinyin">${colorizePinyinHTML(ch.pinyin)}</span>
            <span class="badge badge-pos">Tone ${ch.tone_mnemonic_anchor}</span>
            <button class="btn btn-icon" style="padding: 2px 6px; font-size: 0.7rem;" onclick="speak('${ch.character}', 1.0)">🔊</button>
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
        <strong>Components:</strong> Meaning <span class="badge badge-pos" style="font-size: 0.7rem;">${ch.meaning_component}</span> · Sound <span class="badge badge-hsk" style="font-size: 0.7rem;">${ch.sound_component}</span>
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
          <div class="alert-title">🧠 Composite Memory Hook (EN)</div>
          <div style="font-size: 0.92rem; line-height: 1.5; font-style: italic;">"${mr.composite_memory_hook_en}"</div>
        </div>` : ''}
      ${showEs && mr.composite_memory_hook_es ? `
        <div class="alert-box" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.3);">
          <div class="alert-title" style="color: var(--accent-green);">🧠 Gancho Mnemotécnico Compuesto (ES)</div>
          <div style="font-size: 0.92rem; line-height: 1.5; font-style: italic;">"${mr.composite_memory_hook_es}"</div>
        </div>` : ''}
      ${mr.cultural_and_cognitive_roots ? `
        <div class="alert-box blue">
          <div class="alert-title">💡 Cultural & Cognitive Metaphor</div>
          <div style="font-size: 0.88rem; line-height: 1.6;">${mr.cultural_and_cognitive_roots}</div>
        </div>` : ''}
      ${mr.tone_sandhi_and_pitch_modulation ? `
        <div class="alert-box" style="background: rgba(168, 85, 247, 0.08); border-color: rgba(168, 85, 247, 0.3);">
          <div class="alert-title" style="color: var(--accent-purple);">🎵 Tone Sandhi & Pitch Contours</div>
          <div style="font-size: 0.88rem; line-height: 1.6;">${mr.tone_sandhi_and_pitch_modulation}</div>
        </div>` : ''}
    </div>
  `;

  // 6. Look-Alike Traps Panel (字形陷阱)
  const traps = w.traps_and_cognates || {};
  const lookAlikes = traps.look_alikes || [];
  const lookAlikesHtml = lookAlikes.map(la => `
    <div class="lookalike-card">
      <div class="lookalike-char-box" onclick="speak('${la.character}', 1.0)" title="Click to pronounce">
        ${la.character}
      </div>
      <div class="lookalike-meta">
        <div class="lookalike-pinyin">${colorizePinyinHTML(la.pinyin)}</div>
        <div class="lookalike-meaning">${la.meaning_en}</div>
        <div class="lookalike-distinction">⚠️ ${la.distinction_note}</div>
      </div>
    </div>
  `).join('');

  const trapsHtml = lookAlikes.length > 0 ? `
    <div style="margin-bottom: 12px;">
      <div style="font-weight: 700; font-size: 0.92rem; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
        <span>⚠️ Look-Alike Confusion Traps (字形陷阱)</span>
        <span class="badge badge-pos" style="background: rgba(245, 158, 11, 0.15); color: var(--accent);">${lookAlikes.length} pairs</span>
      </div>
      <div class="comparison-grid">${lookAlikesHtml}</div>
    </div>
  ` : `
    <div class="alert-box" style="text-align: center; color: var(--text-muted); padding: 18px;">
      No specific look-alike confusion traps recorded for this word.
    </div>
  `;

  // 7. Etymological Cognates Family Panel (同族字)
  const cognates = traps.etymological_cognates || [];
  const cognatesHtml = cognates.map(cg => `
    <div class="cognate-chip" onclick="speak('${cg.character}', 1.0)" title="Click to pronounce ${cg.character}">
      <span class="ch">${cg.character}</span>
      <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem;">${colorizePinyinHTML(cg.pinyin)}</span>
      <span style="color: var(--text-dim); font-size: 0.72rem;">${cg.gloss_en}</span>
    </div>
  `).join('');

  const cognatesPanelHtml = cognates.length > 0 ? `
    <div>
      <div style="font-weight: 700; font-size: 0.92rem; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
        <span>🧬 Etymological Cognates Family (同族字)</span>
        <span class="badge badge-pos" style="background: rgba(59, 130, 246, 0.15); color: var(--primary);">${cognates.length} cognates</span>
      </div>
      <div class="cognate-chips">${cognatesHtml}</div>
    </div>
  ` : `
    <div class="alert-box" style="text-align: center; color: var(--text-muted); padding: 18px;">
      No etymological cognate family members recorded for this word.
    </div>
  `;

  // 8. Semantic Boundary Contrasts Panel (语义辨析)
  const sbc = w.semantic_boundary_contrasts || {};
  const contrasts = sbc.contrasts || [];
  const contrastsHtml = contrasts.map(ct => `
    <div class="contrast-card">
      <div class="contrast-head">
        <span class="contrast-title">${ct.compared_word}</span>
        <span class="contrast-pinyin-tag">${colorizePinyinHTML(ct.pinyin)}</span>
      </div>
      <div class="contrast-desc" style="font-size: 0.88rem; line-height: 1.6; color: var(--text);">${ct.analysis}</div>
    </div>
  `).join('');

  const contrastsPanelHtml = `
    ${sbc.core_nuance ? `
      <div style="margin-bottom: 16px; font-size: 0.94rem; color: var(--text); padding: 12px 16px; background: var(--bg-card-sub); border-radius: 10px; border: 1px solid var(--border); border-left: 4px solid var(--accent);">
        <strong>🎯 Core Semantic Nuance:</strong> ${sbc.core_nuance}
      </div>` : ''}
    <div>${contrastsHtml || '<div class="alert-box" style="text-align: center; color: var(--text-muted); padding: 18px;">No semantic boundary contrasts recorded for this word.</div>'}</div>
  `;

  // 8. Passages Panel (with Pinyin toggle and dual-speed audio)
  const passages = w.extended_reading_passages || [];
  const isPinyinVisible = (typeof StorageManager !== 'undefined') ? StorageManager.getSettings().showPassagePinyin : false;
  const passagesHtml = passages.map((p, idx) => `
    <div class="passage-block">
      <div class="passage-ctrl-row">
        <span class="passage-badge">${idx === 0 ? 'Passage #1: Reflective / Philosophical' : 'Passage #2: Socio-economic / Formal'}</span>
        <div style="display: flex; gap: 6px; align-items: center;">
          <button type="button" class="btn-toggle-pinyin ${isPinyinVisible ? 'active' : ''}" onclick="App.togglePassagePinyin(this)" title="Toggle Pinyin visibility">
            🔤 Pinyin
          </button>
          <button type="button" class="btn-copy-sent" onclick="App.copyText('${p.hanzi.replace(/'/g, "\\'")}', 'Passage copied!')" title="Copy Passage">
            📋 Copy
          </button>
          <button class="audio-speed-btn" onclick="speak('${p.hanzi.replace(/'/g, "\\'")}', 1.0)">🔊 1.0x</button>
          <button class="audio-speed-btn" onclick="speak('${p.hanzi.replace(/'/g, "\\'")}', 0.75)">🐢 0.75x</button>
        </div>
      </div>
      <div class="passage-hanzi" style="font-size: 1.15rem; line-height: 1.7; letter-spacing: 0.02em;">${highlightHeadword(p.hanzi, w.hanzi)}</div>
      <div class="passage-pinyin ${isPinyinVisible ? '' : 'pinyin-hidden'}" style="margin: 8px 0;">${colorizePinyinHTML(p.pinyin)}</div>
      ${showEn ? `<div class="passage-trans" style="margin-bottom: 8px; font-size: 0.9rem; line-height: 1.5;"><strong>EN:</strong> ${p.en}</div>` : ''}
      ${showEs ? `<div class="passage-trans" style="font-size: 0.9rem; line-height: 1.5;"><strong>ES:</strong> ${p.es}</div>` : ''}
    </div>
  `).join('');

  return `
    <div class="card-container back-card">
      <!-- Persistent Header -->
      <header class="card-header-sticky">
        <div class="hero-top-row">
          <div class="hero-badges">
            ${originBadge}
            <span class="badge badge-num">NO. ${String(w.id).padStart(2, '0')}</span>
            <span class="badge badge-hsk">${w.level || 'HSK 5'}</span>
            <span class="badge badge-pos">${w.part_of_speech}</span>
            ${contour ? `<span class="badge tone-contour-badge">${contour}</span>` : ''}
            ${statusBadge}
          </div>
          <div class="card-action-bar">
            <div class="audio-control-cluster">
              <button type="button" class="audio-speed-btn" onclick="speak('${w.hanzi}', 0.75)" title="Slow Pronunciation (Shortcut: T or Shift+R)">
                🐢 0.75x <kbd class="hint-kbd" style="font-size: 0.65rem; padding: 1px 4px; margin-left: 2px;">T</kbd>
              </button>
              <button type="button" class="audio-speed-btn" onclick="speak('${w.hanzi}', 1.0)" title="Normal Pronunciation (Shortcut: R)">
                🔊 1.0x <kbd class="hint-kbd" style="font-size: 0.65rem; padding: 1px 4px; margin-left: 2px;">R</kbd>
              </button>
            </div>
            <button type="button" class="drawer-trigger-btn" onclick="App.openLookupDrawer()" title="External Lookups (L)">
              🔍
            </button>
            <button type="button" class="drawer-trigger-btn" onclick="App.openSettingsDrawer()" title="Study Settings (S)">
              ⚙️
            </button>
          </div>
        </div>

        <div style="display: flex; align-items: baseline; gap: 14px; margin-top: 6px;">
          <div class="hero-word" onclick="speak('${w.hanzi}', 1.0)" title="Click to pronounce">${w.hanzi}</div>
          <div class="hero-pinyin" style="font-size: 1.3rem;">${colorizePinyinHTML(w.pinyin)}</div>
        </div>

        <!-- Bilingual Meanings Summary -->
        <div class="meanings-container">
          ${showEn && w.meanings_summary?.en ? `
            <div class="meaning-row"><span class="lang-tag en">EN</span> ${w.meanings_summary.en}</div>` : ''}
          ${showEs && w.meanings_summary?.es ? `
            <div class="meaning-row"><span class="lang-tag es">ES</span> ${w.meanings_summary.es}</div>` : ''}
        </div>
      </header>

      <!-- Minimalist Segmented Navigation Bar -->
      <nav class="pill-nav-container" aria-label="Vocabulary Sections">
        <div class="pill-nav-track" role="tablist">
          <button type="button" class="pill-btn ${activeTab === 'sentences' ? 'active' : ''}" onclick="App.switchTab('sentences')">
            <span class="pill-text">例句</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'collocations' ? 'active' : ''}" onclick="App.switchTab('collocations')">
            <span class="pill-text">搭配</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'idioms' ? 'active' : ''}" onclick="App.switchTab('idioms')">
            <span class="pill-text">成语</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'decomp' ? 'active' : ''}" onclick="App.switchTab('decomp')">
            <span class="pill-text">字形</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'mnemonics' ? 'active' : ''}" onclick="App.switchTab('mnemonics')">
            <span class="pill-text">助记</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'traps' ? 'active' : ''}" onclick="App.switchTab('traps')" title="Look-Alike Character Traps">
            <span class="pill-text">字形陷阱</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'cognates' ? 'active' : ''}" onclick="App.switchTab('cognates')" title="Etymological Cognates Family">
            <span class="pill-text">同族字</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'contrasts' || activeTab === 'synonyms' ? 'active' : ''}" onclick="App.switchTab('contrasts')" title="Semantic Boundary Contrasts">
            <span class="pill-text">语义辨析</span>
          </button>
          <button type="button" class="pill-btn ${activeTab === 'passages' ? 'active' : ''}" onclick="App.switchTab('passages')" title="Extended Reading Passages">
            <span class="pill-text">篇章</span>
          </button>
        </div>
      </nav>

      <!-- 9 Dynamic Tab Panels -->
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
        <section class="tab-panel ${activeTab === 'cognates' ? 'active' : ''}" id="panel-cognates">
          ${cognatesPanelHtml}
        </section>
        <section class="tab-panel ${activeTab === 'contrasts' || activeTab === 'synonyms' ? 'active' : ''}" id="panel-contrasts">
          ${contrastsPanelHtml}
        </section>
        <section class="tab-panel ${activeTab === 'passages' ? 'active' : ''}" id="panel-passages">
          ${passagesHtml}
        </section>
      </div>
    </div>
  `;
}

// Render Persistent Bottom Anki Review Bar
function renderActionBar(cardSide, studyMode, reviewItem) {
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
          <span>👁️ Show Answer <span class="action-kbd">Space</span></span>
        </button>
      </div>
    `;
  } else {
    const pred = (typeof StorageManager !== 'undefined' && StorageManager.predictNextIntervals)
      ? StorageManager.predictNextIntervals(reviewItem)
      : {
          again: { label: '~5 cards' },
          hard: { label: '~6 cards' },
          good: { label: '1d' },
          easy: { label: '3d' }
        };

    barEl.innerHTML = `
      <div class="anki-action-group">
        <button type="button" class="btn-rate-again" onclick="App.rateCard('again')" title="Mark as Again: Intra-session repeat (1 / A / Bksp)">
          <span class="rate-interval-preview">${pred.again.label}</span>
          <span class="rate-btn-label">🔴 Again <span class="action-kbd">1</span></span>
        </button>
        <button type="button" class="btn-rate-hard" onclick="App.rateCard('hard')" title="Mark as Hard: Shorter interval (2)">
          <span class="rate-interval-preview">${pred.hard.label}</span>
          <span class="rate-btn-label">🟠 Hard <span class="action-kbd">2</span></span>
        </button>
        <button type="button" class="btn-rate-good" onclick="App.rateCard('good')" title="Mark as Good: Spaced repetition progression (3 / D / Space)">
          <span class="rate-interval-preview">${pred.good.label}</span>
          <span class="rate-btn-label">🟢 Good <span class="action-kbd">3</span></span>
        </button>
        <button type="button" class="btn-rate-easy" onclick="App.rateCard('easy')" title="Mark as Easy: Accelerated bonus (4)">
          <span class="rate-interval-preview">${pred.easy.label}</span>
          <span class="rate-btn-label">🔵 Easy <span class="action-kbd">4</span></span>
        </button>
      </div>
    `;
  }
}

// Render Dynamic Study Filter Bar (Chapter Horizon & SRS Status Interleaving)
function renderStudyFilterPills({
  chapters = [],
  activeChapterFilter = 'all',
  activeStatusFilter = 'all',
  chapterCounts = {},
  statusCounts = {},
  onSelectChapterFilter,
  onSelectStatusFilter
}) {
  const chContainer = document.getElementById('chapter-filter-pills');
  const stContainer = document.getElementById('status-filter-pills');
  if (!chContainer || !stContainer) return;

  // Row 1: Chapter Filter Pills
  let chHtml = `
    <button type="button" class="study-filter-pill ${activeChapterFilter === 'all' ? 'active' : ''}" data-ch="all">
      <span>🌐 All Active Chapters</span>
      <span class="pill-count-badge">${chapterCounts['all'] || 0}</span>
    </button>
  `;

  chapters.forEach(ch => {
    const isAct = activeChapterFilter === ch.dir;
    const cnt = chapterCounts[ch.dir] ?? ch.word_count ?? 0;
    chHtml += `
      <button type="button" class="study-filter-pill ${isAct ? 'active' : ''}" data-ch="${ch.dir}" title="${ch.title || ch.name}">
        <span>CHP ${ch.id}</span>
        <span class="pill-count-badge">${cnt}</span>
      </button>
    `;
  });
  chContainer.innerHTML = chHtml;
  chContainer.querySelectorAll('.study-filter-pill').forEach(btn => {
    btn.onclick = () => {
      const chVal = btn.getAttribute('data-ch');
      if (onSelectChapterFilter) onSelectChapterFilter(chVal);
    };
  });

  // Row 2: Status Filter Pills
  const statuses = [
    { id: 'all', label: '⚡ All (Smart Mix)', count: statusCounts['all'] || 0, title: 'Interleaves 3 Due Reviews : 1 New Card' },
    { id: 'due', label: '⏰ Due Reviews Only', count: statusCounts['due'] || 0, title: 'SRS due cards needing review' },
    { id: 'new', label: '⚪ New Words Only', count: statusCounts['new'] || 0, title: 'Unstudied vocabulary' },
    { id: 'learning', label: '🔥 Learning / Difficult', count: statusCounts['learning'] || 0, title: 'Cards currently in intra-session learning or lapses' },
    { id: 'leeches', label: '🔴 Hard / Leeches', count: statusCounts['leeches'] || 0, title: 'Cards with frequent lapses' }
  ];

  let stHtml = statuses.map(st => `
    <button type="button" class="study-filter-pill ${activeStatusFilter === st.id ? 'active' : ''}" data-status="${st.id}" title="${st.title}">
      <span>${st.label}</span>
      <span class="pill-count-badge">${st.count}</span>
    </button>
  `).join('');
  stContainer.innerHTML = stHtml;
  stContainer.querySelectorAll('.study-filter-pill').forEach(btn => {
    btn.onclick = () => {
      const stVal = btn.getAttribute('data-status');
      if (onSelectStatusFilter) onSelectStatusFilter(stVal);
    };
  });
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
      <div class="section-title">Semantic Boundary Contrasts (语义辨析)</div>
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

// -------------------------------------------------------------
// Time & Date Formatting Utilities
// -------------------------------------------------------------
function formatSecondsToHMS(totalSeconds) {
  const s = Math.max(0, Math.floor(totalSeconds || 0));
  const hours = Math.floor(s / 3600);
  const minutes = Math.floor((s % 3600) / 60);
  const seconds = s % 60;
  if (hours > 0) {
    return `${hours}h ${String(minutes).padStart(2, '0')}m ${String(seconds).padStart(2, '0')}s`;
  }
  return `${String(minutes).padStart(2, '0')}m ${String(seconds).padStart(2, '0')}s`;
}

function formatSecondsToShort(totalSeconds) {
  const s = Math.max(0, Math.floor(totalSeconds || 0));
  const hours = Math.floor(s / 3600);
  const minutes = Math.floor((s % 3600) / 60);
  if (hours > 0) return `${hours}h ${minutes}m`;
  if (minutes > 0) return `${minutes}m`;
  return `${s}s`;
}

// -------------------------------------------------------------
// Mini Review Timeline for Individual Word
// -------------------------------------------------------------
function renderWordMiniTimeline(reviewItem) {
  if (!reviewItem || !reviewItem.reviews) {
    return `
      <div class="word-timeline-card empty-state">
        <div style="font-size: 0.82rem; color: var(--text-dim);">⚪ <strong>Unreviewed Word:</strong> This word has not been practiced in flashcards yet.</div>
      </div>
    `;
  }

  const lapses = reviewItem.lapses || 0;
  const history = reviewItem.history || [];
  const srsLevel = reviewItem.srsLevel || 0;
  const lastRevDate = reviewItem.lastReviewed ? new Date(reviewItem.lastReviewed).toLocaleDateString() : 'Today';

  return `
    <div class="word-timeline-card">
      <div class="word-timeline-header">
        <div class="word-timeline-title">
          <span>📈 Memorization Journey</span>
          <span class="badge ${lapses > 0 ? 'badge-again' : 'badge-green'}">
            ${lapses > 0 ? `🔴 ${lapses} Lapse${lapses > 1 ? 's' : ''}` : '🟢 Mastered Smoothly'}
          </span>
          <span class="badge badge-num">SRS Level ${srsLevel} (${reviewItem.reviews} Reviews)</span>
        </div>
        <span style="font-size: 0.78rem; color: var(--text-dim);">Last Review: ${lastRevDate}</span>
      </div>
      <div class="word-timeline-track">
        <div class="tl-node tl-node-start" title="First Encounter">⚪ First Seen</div>
        ${history.slice(-10).map((h) => {
          const isLapse = h.result === 'dont_remember';
          const timeStr = new Date(h.t).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
          const dateStr = new Date(h.t).toLocaleDateString([], { month: 'short', day: 'numeric' });
          return `
            <div class="tl-connector ${isLapse ? 'tl-conn-lapse' : 'tl-conn-good'}"></div>
            <div class="tl-node ${isLapse ? 'tl-node-lapse' : 'tl-node-good'}" title="${isLapse ? 'Forgot (Lapse)' : 'Remembered (Good)'} on ${dateStr} ${timeStr}">
              <span>${isLapse ? '🔴 Lapse' : `🟢 Lvl ${h.level}`}</span>
              <span class="tl-date">${dateStr}</span>
            </div>
          `;
        }).join('')}
      </div>
    </div>
  `;
}

// -------------------------------------------------------------
// Full Dedicated Dictionary Window View
// -------------------------------------------------------------
function renderDictionaryWindow({
  words = [],
  selectedWord = null,
  currentLang = 'both',
  currentChapter = null,
  searchQuery = '',
  selectedPos = 'ALL',
  selectedStatus = 'all'
}) {
  const container = document.getElementById('detail-container');
  if (!container) return;

  const showEn = currentLang === 'both' || currentLang === 'en';
  const showEs = currentLang === 'both' || currentLang === 'es';
  const chapterDir = currentChapter ? currentChapter.dir : 'chapter_01';
  const reviews = (typeof StorageManager !== 'undefined') ? StorageManager.getChapterReviews(chapterDir) : {};

  // Filter words for dictionary index pane
  let filtered = [...words];
  const queryLower = (searchQuery || '').trim().toLowerCase();
  if (queryLower) {
    filtered = filtered.filter(w =>
      (w.hanzi && w.hanzi.toLowerCase().includes(queryLower)) ||
      (w.pinyin && w.pinyin.toLowerCase().includes(queryLower)) ||
      (w.meanings_summary?.en && w.meanings_summary.en.toLowerCase().includes(queryLower)) ||
      (w.meanings_summary?.es && w.meanings_summary.es.toLowerCase().includes(queryLower))
    );
  }

  if (selectedPos !== 'ALL') {
    const posLower = selectedPos.toLowerCase();
    filtered = filtered.filter(w => (w.part_of_speech || '').toLowerCase().includes(posLower));
  }

  if (selectedStatus === 'due') {
    filtered = filtered.filter(w => StorageManager.isDue(reviews[String(w.id)]));
  } else if (selectedStatus === 'lapses') {
    filtered = filtered.filter(w => reviews[String(w.id)]?.status === 'dont_remember' || (reviews[String(w.id)]?.lapses > 0));
  } else if (selectedStatus === 'remembered') {
    filtered = filtered.filter(w => reviews[String(w.id)]?.status === 'remembered');
  } else if (selectedStatus === 'new') {
    filtered = filtered.filter(w => !reviews[String(w.id)]);
  }

  const activeWord = selectedWord || filtered[0] || words[0] || null;
  const activeReview = activeWord ? reviews[String(activeWord.id)] : null;

  container.innerHTML = `
    <div class="dictionary-view-container">
      <!-- Left Index & Navigation Pane -->
      <aside class="dict-index-pane">
        <div class="dict-index-header">
          <div class="dict-search-row">
            <svg class="dict-search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            <input type="text" id="dict-search-input" class="dict-search-input" placeholder="Search Hanzi, Pinyin, EN, ES..." value="${searchQuery || ''}" oninput="App.onDictSearchInput(this.value)">
            ${searchQuery ? `<button class="dict-clear-btn" onclick="App.clearDictSearch()">&times;</button>` : ''}
          </div>

          <!-- POS Quick Filter Chips -->
          <div class="dict-filter-chips">
            ${['ALL', 'Noun', 'Verb', 'Adjective', 'Adverb', 'Idiom'].map(p => `
              <button class="dict-pos-chip ${selectedPos === p ? 'active' : ''}" onclick="App.setDictPosFilter('${p}')">${p}</button>
            `).join('')}
          </div>

          <!-- Review Status Filter -->
          <div class="dict-status-row">
            <button class="dict-status-chip ${selectedStatus === 'all' ? 'active' : ''}" onclick="App.setDictStatusFilter('all')">All (${words.length})</button>
            <button class="dict-status-chip ${selectedStatus === 'lapses' ? 'active' : ''}" onclick="App.setDictStatusFilter('lapses')">🔴 Lapses</button>
            <button class="dict-status-chip ${selectedStatus === 'remembered' ? 'active' : ''}" onclick="App.setDictStatusFilter('remembered')">🟢 Mastered</button>
            <button class="dict-status-chip ${selectedStatus === 'new' ? 'active' : ''}" onclick="App.setDictStatusFilter('new')">⚪ New</button>
          </div>

          <div class="dict-meta-summary">
            <span>Showing <strong>${filtered.length}</strong> of ${words.length} terms</span>
            <span class="dict-ch-tag">CHP ${currentChapter ? currentChapter.id : 1}</span>
          </div>
        </div>

        <!-- Dictionary Word List -->
        <div class="dict-word-list" id="dict-word-list">
          ${filtered.length === 0 ? `
            <div class="dict-empty-list">No vocabulary terms match current filter.</div>
          ` : filtered.map(w => {
            const rev = reviews[String(w.id)];
            const isSelected = activeWord && activeWord.id === w.id;
            let statusBadge = '<span class="dict-chip-status status-new">⚪</span>';
            if (rev) {
              if (rev.status === 'dont_remember' || rev.lapses > 0) {
                statusBadge = `<span class="dict-chip-status status-lapse">🔴 ${rev.lapses || 1}</span>`;
              } else if (rev.status === 'remembered') {
                statusBadge = `<span class="dict-chip-status status-good">🟢 L${rev.srsLevel || 1}</span>`;
              }
            }

            return `
              <div class="dict-word-item ${isSelected ? 'active' : ''}" onclick="App.selectDictionaryWord(${w.id})">
                <div class="dict-item-top">
                  <span class="dict-item-hanzi">${w.hanzi}</span>
                  <span class="dict-item-pinyin">${colorizePinyinHTML(w.pinyin)}</span>
                  ${statusBadge}
                </div>
                <div class="dict-item-def">${showEn ? (w.meanings_summary?.en || '') : (w.meanings_summary?.es || '')}</div>
                <div class="dict-item-meta">
                  <span class="dict-item-badge">#${String(w.id).padStart(2, '0')}</span>
                  <span class="dict-item-badge">${w.part_of_speech}</span>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </aside>

      <!-- Right Lexicographical Article Pane -->
      <section class="dict-article-pane">
        ${!activeWord ? `
          <div class="dict-no-selection">
            <div style="font-size: 2.5rem; margin-bottom: 12px;">📖</div>
            <h3>Select a word from the dictionary list</h3>
            <p>Select any vocabulary item on the left to read full definitions, radicals, decompositions, and reading passages.</p>
          </div>
        ` : renderDictionaryArticle(activeWord, currentLang, activeReview)}
      </section>
    </div>
  `;
}

// Render full single-entry dictionary article
function renderDictionaryArticle(w, currentLang, reviewItem) {
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

  return `
    <div class="dict-article-inner">
      <!-- Article Top Toolbar -->
      <div class="dict-article-toolbar">
        <div class="dict-toolbar-left">
          <span class="badge badge-hsk">${w.level || 'HSK 5'}</span>
          <span class="badge badge-pos">${w.part_of_speech}</span>
          <span class="badge badge-num">NO. ${String(w.id).padStart(2, '0')}</span>
          ${contour ? `<span class="badge tone-contour-badge">${contour}</span>` : ''}
        </div>
        <div class="dict-toolbar-right">
          <button type="button" class="btn btn-primary" onclick="App.studyCurrentWord(${w.id})" title="Jump to Flashcard Stage for this word">
            🗂️ Study in Flashcards
          </button>
          <button type="button" class="btn btn-icon" onclick="App.openExternalLookups('${w.hanzi}')" title="External Lookups (Pleco, MDBG, Wiktionary)">
            🔍 Lookups
          </button>
        </div>
      </div>

      <!-- Hero Header -->
      <div class="dict-hero-card">
        <div class="dict-hero-main">
          <span class="dict-hanzi-hero" onclick="speak('${w.hanzi}')" title="Click to pronounce">${w.hanzi}</span>
          <div class="dict-hero-pinyin-group">
            <span class="dict-pinyin-hero">${colorizePinyinHTML(w.pinyin)}</span>
            <button class="audio-btn hero-audio-btn" title="Pronounce Word" onclick="speak('${w.hanzi}')">🔊</button>
          </div>
        </div>
        <div class="dict-hero-summary">
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

      <!-- Word Memorization History Timeline -->
      ${renderWordMiniTimeline(reviewItem)}

      <!-- Core Lexical Senses -->
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

      <!-- Contextual Example Sentences -->
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

      <!-- Collocations & Classical Idioms -->
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

      <!-- Character Decomposition & Etymology -->
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

      <!-- Memory Hooks & Roots -->
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
      </div>

      <!-- Look-Alikes & Cognates -->
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
        <div class="section-title">Semantic Boundary Contrasts (语义辨析)</div>
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
    </div>
  `;
}

// -------------------------------------------------------------
// Character Review & Lapse Timeline Section Renderer
// -------------------------------------------------------------
function renderCharacterTimeline(chapterDir, words = []) {
  if (typeof StorageManager === 'undefined') return '';
  const data = StorageManager.getCharacterTimelineData(chapterDir, words);

  const highLapse = data.highLapseWords || [];
  const smoothGroups = data.smoothGroups || {};
  const smoothTotal = data.smoothWords?.length || 0;

  return `
    <div class="char-timeline-section">
      <div class="char-timeline-header">
        <div>
          <h3 class="char-timeline-title">🎯 Character Retention Radar & Lapse Timeline</h3>
          <p class="char-timeline-desc">
            Spotlights vocabulary terms that had to be repeated most often due to memory lapses.
            Smoothly mastered terms are grouped together into progression milestones.
          </p>
        </div>
      </div>

      <!-- High-Lapse Problem Characters Spotlight -->
      <div class="high-lapse-block">
        <div class="lapse-block-title">
          <span>⚠️ High-Lapse Focus Area (${highLapse.length} Characters)</span>
          <span style="font-size: 0.8rem; font-weight: 500; color: var(--text-dim);">Repeated multiple times due to lapses</span>
        </div>

        ${highLapse.length === 0 ? `
          <div class="lapse-empty-banner">
            🎉 <strong>Zero Problem Words!</strong> No memory lapses recorded yet in this chapter.
          </div>
        ` : `
          <div class="lapse-cards-grid">
            ${highLapse.map(item => {
              const w = item.word;
              const lapses = item.lapses;
              const revs = item.reviews;
              const history = item.history || [];
              const severityClass = lapses >= 3 ? 'severity-critical' : 'severity-moderate';

              return `
                <div class="lapse-card ${severityClass}">
                  <div class="lapse-card-top">
                    <div class="lapse-card-hanzi" onclick="speak('${w.hanzi}')">
                      <span>${w.hanzi}</span>
                      <span class="audio-mini-btn">🔊</span>
                    </div>
                    <div class="lapse-card-meta">
                      <span class="badge ${lapses >= 3 ? 'badge-again' : 'badge-amber'}">
                        🔴 ${lapses} Lapse${lapses > 1 ? 's' : ''} / ${revs} Reviews
                      </span>
                      <span class="badge badge-pos">${w.part_of_speech}</span>
                    </div>
                  </div>

                  <div class="lapse-card-pinyin">${colorizePinyinHTML(w.pinyin)}</div>
                  <div class="lapse-card-def">${w.meanings_summary?.en || w.meanings_summary?.es || ''}</div>

                  <!-- Step-by-Step History Event Track -->
                  <div class="lapse-track-wrap">
                    <div class="lapse-track-label">Review Progression:</div>
                    <div class="word-timeline-track">
                      <div class="tl-node tl-node-start" title="Started">⚪ Start</div>
                      ${history.slice(-8).map(h => {
                        const isLapse = h.result === 'dont_remember';
                        const timeStr = new Date(h.t).toLocaleDateString([], { month: 'numeric', day: 'numeric' });
                        return `
                          <div class="tl-connector ${isLapse ? 'tl-conn-lapse' : 'tl-conn-good'}"></div>
                          <div class="tl-node ${isLapse ? 'tl-node-lapse' : 'tl-node-good'}" title="${isLapse ? 'Forgot (Lapse)' : 'Remembered (Good)'}">
                            ${isLapse ? '🔴 Forgot' : `🟢 Lvl ${h.level}`}
                          </div>
                        `;
                      }).join('')}
                    </div>
                  </div>

                  <!-- Quick Action Buttons -->
                  <div class="lapse-card-actions">
                    <button type="button" class="btn btn-sm btn-primary" onclick="App.studyCurrentWord(${w.id})" title="Practice this card immediately in Flashcards">
                      🗂️ Study Now
                    </button>
                    <button type="button" class="btn btn-sm" onclick="App.openWordInDictionary(${w.id})" title="Inspect radicals & decomposition in Dictionary">
                      📖 View Details
                    </button>
                  </div>
                </div>
              `;
            }).join('')}
          </div>
        `}
      </div>

      <!-- Grouped Smooth Progress Milestones -->
      <div class="smooth-progress-block">
        <div class="smooth-block-header">
          <div>
            <span style="font-weight: 700; color: var(--accent-green); font-size: 1rem;">
              🟢 Standard Progression (${smoothTotal} Characters Advancing Without Lapses)
            </span>
            <div style="font-size: 0.8rem; color: var(--text-dim); margin-top: 2px;">
              Words remembered steadily on schedule, grouped by current spaced repetition level
            </div>
          </div>
        </div>

        ${smoothTotal === 0 ? `
          <div style="font-size: 0.84rem; color: var(--text-dim); padding: 12px;">No smooth review records yet. Complete flashcard reviews to see progress tiers.</div>
        ` : `
          <div class="smooth-tiers-container">
            ${Object.keys(smoothGroups).sort((a, b) => b - a).map(lvl => {
              const grp = smoothGroups[lvl];
              const lvlNames = ['Level 0 (Same-Day Queue)', 'Level 1 (1-Day Interval)', 'Level 2 (3-Day Interval)', 'Level 3 (7-Day Interval)', 'Level 4 (14-Day Interval)', 'Level 5 (30-Day Mastered)'];
              const label = lvlNames[lvl] || `Level ${lvl}`;

              return `
                <div class="smooth-tier-row">
                  <div class="smooth-tier-label">
                    <span class="badge ${lvl >= 4 ? 'badge-green' : 'badge-num'}">${label}</span>
                    <span style="font-size: 0.8rem; font-weight: 600; color: var(--text);">${grp.count} terms</span>
                  </div>
                  <div class="smooth-chips-wrap">
                    ${grp.words.map(item => `
                      <span class="smooth-char-chip" onclick="App.openWordInDictionary(${item.word.id})" title="${item.word.hanzi} (${item.word.pinyin}) - ${item.word.meanings_summary?.en || ''}">
                        ${item.word.hanzi}
                        <span class="smooth-chip-revs">${item.reviews}x</span>
                      </span>
                    `).join('')}
                  </div>
                </div>
              `;
            }).join('')}
          </div>
        `}
      </div>
    </div>
  `;
}

// -------------------------------------------------------------
// Dedicated Statistics & Study Analytics Window View
// -------------------------------------------------------------
function renderStatisticsDashboard({
  currentChapter = null,
  chapters = [],
  words = []
}) {
  const container = document.getElementById('stats-view-container') || document.getElementById('detail-container');
  if (!container || typeof StorageManager === 'undefined') return;

  const todayStats = StorageManager.getTimeStatsToday();
  const allTimeStats = StorageManager.getTimeStatsAllTime();
  const habits = StorageManager.getStudyHabitsSummary();
  const recentDays = StorageManager.getDailyActivityHistory(14);
  const recentSessions = StorageManager.getRecentSessions(8);
  const forecast = (typeof StorageManager.getForecast7Days === 'function') ? StorageManager.getForecast7Days() : [];
  const maxForecastCount = Math.max(1, ...forecast.map(f => f.count));
  const leeches = (typeof StorageManager.getLeechWords === 'function') ? StorageManager.getLeechWords(10) : [];
  const chapterDir = currentChapter ? currentChapter.dir : 'chapter_01';

  const isAfk = (typeof TimeTracker !== 'undefined') ? TimeTracker.isAfk() : false;
  const afkThresholdSec = (typeof TimeTracker !== 'undefined') ? TimeTracker.getAfkThresholdSeconds() : 120;

  // Max daily seconds for chart scaling
  const maxDaySeconds = Math.max(1, ...recentDays.map(d => d.totalSeconds));

  container.innerHTML = `
    <div class="stats-dashboard-container">
      <!-- Dashboard Top Header -->
      <div class="stats-header-card">
        <div class="stats-title-group">
          <h2>📊 Study Analytics & Review Forecast</h2>
          <p class="stats-subtitle">Continuous activity tracking, spaced repetition forecast, and leech vocabulary drill.</p>
        </div>

        <!-- AFK Status & Threshold Control -->
        <div class="afk-status-box">
          <div class="afk-indicator-pill ${isAfk ? 'pill-afk' : 'pill-active'}">
            <span class="afk-dot"></span>
            <span>${isAfk ? '⏸️ Idle / AFK (Tracking Paused)' : '🟢 Active (Time Tracking)'}</span>
          </div>

          <div class="afk-selector-wrap">
            <label for="afk-timeout-select">AFK Inactivity Timeout:</label>
            <select id="afk-timeout-select" class="chapter-select" style="padding: 3px 8px; font-size: 0.78rem;" onchange="App.changeAfkThreshold(this.value)">
              <option value="60" ${afkThresholdSec === 60 ? 'selected' : ''}>1 minute</option>
              <option value="120" ${afkThresholdSec === 120 ? 'selected' : ''}>2 minutes (Default)</option>
              <option value="180" ${afkThresholdSec === 180 ? 'selected' : ''}>3 minutes</option>
              <option value="300" ${afkThresholdSec === 300 ? 'selected' : ''}>5 minutes</option>
            </select>
          </div>
        </div>
      </div>

      <!-- 7-Day Spaced Repetition Review Forecast -->
      <div class="forecast-chart-container">
        <div class="forecast-header">
          <div>
            <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--text);">📅 7-Day Review Forecast</h3>
            <p style="font-size: 0.78rem; color: var(--text-muted); margin-top: 2px;">Cards scheduled for spaced repetition review across the next 7 days.</p>
          </div>
          <div style="font-size: 0.8rem; font-weight: 700; color: var(--primary);">
            Due This Week: ${forecast.reduce((sum, f) => sum + f.count, 0)} cards
          </div>
        </div>
        <div class="forecast-bars-row">
          ${forecast.map(f => {
            const heightPct = Math.max(6, Math.round((f.count / maxForecastCount) * 100));
            return `
              <div class="forecast-bar-col">
                <span class="forecast-count-label">${f.count}</span>
                <div class="forecast-bar-fill ${f.dayOffset === 0 ? 'is-today' : ''}" style="height: ${heightPct}%;"></div>
                <div class="forecast-label-group">
                  <div class="forecast-day-name">${f.dayLabel}</div>
                  <div class="forecast-date-str">${f.dateStr}</div>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>

      <!-- Leech Vocabulary Section (Top 10 Lapsed Cards) -->
      <div class="leech-section-card">
        <div class="leech-header-row">
          <div>
            <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--text);">🔴 Leech Vocabulary (Difficult Cards)</h3>
            <p style="font-size: 0.78rem; color: var(--text-muted); margin-top: 2px;">Words with repeated lapses and low ease factor requiring extra reinforcement.</p>
          </div>
          <button type="button" class="btn btn-primary" onclick="App.practiceLeeches()" style="font-size: 0.82rem; padding: 6px 14px; white-space: nowrap;">
            ⚡ Practice Leeches (${leeches.length})
          </button>
        </div>
        ${leeches.length === 0 ? `
          <div style="text-align: center; padding: 20px 0; color: var(--text-muted); font-size: 0.88rem;">
            🎉 No leeches found! Your retention is in great shape.
          </div>
        ` : `
          <div class="leech-table-wrap">
            <table class="leech-table">
              <thead>
                <tr>
                  <th>Word</th>
                  <th>Pinyin</th>
                  <th>Lapses</th>
                  <th>Interval</th>
                  <th>Ease</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                ${leeches.map(rec => {
                  const w = words.find(item => String(item.id) === String(rec.wordId)) || { hanzi: rec.wordId, pinyin: '' };
                  return `
                    <tr>
                      <td><strong style="font-size: 1.05rem;">${w.hanzi || rec.wordId}</strong></td>
                      <td>${colorizePinyinHTML(w.pinyin || '')}</td>
                      <td><span class="leech-lapse-badge">🔴 ${rec.lapses}x</span></td>
                      <td>${rec.interval}d</td>
                      <td>${(rec.ease || 2.5).toFixed(2)}</td>
                      <td>
                        <button type="button" class="btn" style="padding: 3px 8px; font-size: 0.75rem;" onclick="speak('${(w.hanzi || '').replace(/'/g, "\\'")}', 1.0)">🔊</button>
                        <button type="button" class="btn" style="padding: 3px 8px; font-size: 0.75rem;" onclick="App.openWordDetail('${rec.chapterId}', '${rec.wordId}')">🔍</button>
                      </td>
                    </tr>
                  `;
                }).join('')}
              </tbody>
            </table>
          </div>
        `}
      </div>

      <!-- Top KPI Metric Cards Grid -->
      <div class="stats-kpi-grid">
        <!-- Today's Active Time -->
        <div class="kpi-card">
          <div class="kpi-icon">⏱️</div>
          <div class="kpi-data">
            <div class="kpi-label">Active Time Today</div>
            <div class="kpi-value">${formatSecondsToHMS((todayStats.studySeconds || 0) + (todayStats.readingSeconds || 0))}</div>
            <div class="kpi-sub">
              <span>🗂️ Study: ${formatSecondsToShort(todayStats.studySeconds)}</span> · 
              <span>📖 Reading: ${formatSecondsToShort(todayStats.readingSeconds)}</span>
            </div>
          </div>
        </div>

        <!-- Lifetime Active Time -->
        <div class="kpi-card">
          <div class="kpi-icon">⏳</div>
          <div class="kpi-data">
            <div class="kpi-label">All-Time Study Time</div>
            <div class="kpi-value">${formatSecondsToHMS(allTimeStats.totalSeconds)}</div>
            <div class="kpi-sub">
              <span>Total Reviews: <strong>${allTimeStats.totalReviews}</strong></span>
            </div>
          </div>
        </div>

        <!-- Daily Streak -->
        <div class="kpi-card">
          <div class="kpi-icon">🔥</div>
          <div class="kpi-data">
            <div class="kpi-label">Current Study Streak</div>
            <div class="kpi-value">${allTimeStats.streak?.currentStreak || 0} <span style="font-size: 1rem; font-weight: 500;">Days</span></div>
            <div class="kpi-sub">
              <span>Longest: ${allTimeStats.streak?.longestStreak || 0} Days</span>
            </div>
          </div>
        </div>

        <!-- Retention Accuracy -->
        <div class="kpi-card">
          <div class="kpi-icon">🎯</div>
          <div class="kpi-data">
            <div class="kpi-label">Flashcard Retention</div>
            <div class="kpi-value ${habits.retentionRate >= 80 ? 'text-green' : 'text-amber'}">${habits.retentionRate}%</div>
            <div class="kpi-sub">
              <span>🟢 ${habits.totalGood} Good</span> · <span>🔴 ${habits.totalAgain} Again</span>
            </div>
          </div>
        </div>
      </div>

      <!-- "How You Study" Behavior Analytics Section -->
      <div class="section-card">
        <div class="section-title">🧠 Study Methodology & Habit Tracking ("How I Study")</div>
        <div class="habits-grid">
          <!-- Recall Pace -->
          <div class="habit-box">
            <div class="habit-icon">⚡</div>
            <div class="habit-info">
              <div class="habit-label">Average Recall Pace</div>
              <div class="habit-value">${habits.avgCardSeconds > 0 ? `${habits.avgCardSeconds}s` : 'N/A'} <span style="font-size: 0.8rem; font-weight: normal; color: var(--text-dim);">/ card</span></div>
              <div class="habit-desc">${habits.avgCardSeconds > 10 ? 'Thoughtful & deep reading pace' : habits.avgCardSeconds > 0 ? 'Fast, fluid recall speed' : 'Pending more reviews'}</div>
            </div>
          </div>

          <!-- Hint Peek Reliance -->
          <div class="habit-box">
            <div class="habit-icon">💡</div>
            <div class="habit-info">
              <div class="habit-label">Hint Peek Rate (H)</div>
              <div class="habit-value">${habits.hintRate}% <span style="font-size: 0.8rem; font-weight: normal; color: var(--text-dim);">(${habits.totalHintPeeks} total peeks)</span></div>
              <div class="habit-desc">${habits.hintRate < 20 ? 'High confidence (rarely peeks hints)' : 'Frequently checks pinyin/radical anchors'}</div>
            </div>
          </div>

          <!-- Audio Pronunciation Frequency -->
          <div class="habit-box">
            <div class="habit-icon">🔊</div>
            <div class="habit-info">
              <div class="habit-label">Audio Replay Practice</div>
              <div class="habit-value">${habits.totalAudioPlays} <span style="font-size: 0.8rem; font-weight: normal; color: var(--text-dim);">listens</span></div>
              <div class="habit-desc">Speech synthesizer and MiniMax native audio playback clicks</div>
            </div>
          </div>

          <!-- Study Mode Balance -->
          <div class="habit-box">
            <div class="habit-icon">⚖️</div>
            <div class="habit-info">
              <div class="habit-label">Flashcards vs Reading Ratio</div>
              <div class="habit-value">
                ${allTimeStats.totalSeconds > 0 ? `${Math.round(((allTimeStats.totalStudySeconds || 0) / allTimeStats.totalSeconds) * 100)}% 🗂️ · ${Math.round(((allTimeStats.totalReadingSeconds || 0) / allTimeStats.totalSeconds) * 100)}% 📖` : '50% · 50%'}
              </div>
              <div class="habit-desc">Balance between active recall drills and deep lexicographical reading</div>
            </div>
          </div>
        </div>

        <!-- Detail Tab Exploration Breakdown -->
        <div style="margin-top: 18px;">
          <div style="font-size: 0.86rem; font-weight: 700; color: var(--text); margin-bottom: 8px;">
            📑 Detail Tab Exploration Distribution
          </div>
          <div class="tab-exploration-grid">
            ${[
              { id: 'sentences', name: 'Example Sentences', count: habits.tabClicks?.sentences || 0 },
              { id: 'collocations', name: 'Collocations & Phrases', count: habits.tabClicks?.collocations || 0 },
              { id: 'decomposition', name: 'Radical Decomposition', count: habits.tabClicks?.decomposition || 0 },
              { id: 'contrasts', name: 'Contrasts & Nuances', count: habits.tabClicks?.contrasts || 0 },
              { id: 'mnemonics', name: 'Memory Hooks', count: habits.tabClicks?.mnemonics || 0 },
              { id: 'passages', name: 'Reading Passages', count: habits.tabClicks?.passages || 0 }
            ].map(tab => `
              <div class="tab-exp-chip">
                <span class="tab-exp-name">${tab.name}</span>
                <span class="tab-exp-count">${tab.count}</span>
              </div>
            `).join('')}
          </div>
        </div>
      </div>

      <!-- 14-Day Activity Chart -->
      <div class="section-card">
        <div class="section-title">📅 14-Day Study Activity & Time Heatmap</div>
        <div class="chart-container">
          <div class="chart-bars-row">
            ${recentDays.map(day => {
              const heightPct = Math.round((day.totalSeconds / maxDaySeconds) * 100);
              const studyPct = day.totalSeconds > 0 ? (day.studySeconds / day.totalSeconds) * 100 : 0;
              const readingPct = 100 - studyPct;

              return `
                <div class="chart-col" title="${day.date} (${day.dayOfWeek}): ${formatSecondsToShort(day.totalSeconds)} active (${day.reviewsCount} reviews)">
                  <div class="chart-bar-wrap">
                    <div class="chart-bar-track" style="height: ${Math.max(6, heightPct)}%;">
                      <div class="chart-bar-study" style="height: ${studyPct}%;"></div>
                      <div class="chart-bar-reading" style="height: ${readingPct}%;"></div>
                    </div>
                  </div>
                  <div class="chart-label">${day.label}</div>
                  <div class="chart-sublabel">${day.dayOfWeek}</div>
                </div>
              `;
            }).join('')}
          </div>
          <div class="chart-legend-row">
            <span class="chart-legend-item"><span class="legend-dot dot-study"></span> Study Time (Flashcards)</span>
            <span class="chart-legend-item"><span class="legend-dot dot-reading"></span> Reading Time (Dictionary & Passages)</span>
          </div>
        </div>
      </div>

      <!-- Character Review & Lapse Timeline Component -->
      ${renderCharacterTimeline(chapterDir, words)}

      <!-- Curriculum Chapters Progress Table -->
      <div class="section-card">
        <div class="section-title">📚 Curriculum Chapters Breakdown</div>
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Chapter</th>
                <th>Theme Title</th>
                <th>Words</th>
                <th>Mastery %</th>
                <th>Study Time</th>
                <th>Reading Time</th>
                <th>Reviews</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              ${chapters.map(ch => {
                const isCurrent = ch.dir === chapterDir;
                const chWords = ch.words || [];
                const chStats = StorageManager.getChapterStats(ch.dir, chWords);
                const timeData = (habits.chapters && habits.chapters[ch.dir]) || { studySeconds: 0, readingSeconds: 0, reviewsCount: 0 };

                return `
                  <tr class="${isCurrent ? 'row-active' : ''}">
                    <td><strong>CHP ${ch.id}</strong></td>
                    <td>${ch.title || ch.name}</td>
                    <td>${ch.word_count || chWords.length || 38}</td>
                    <td>
                      <div style="display: flex; align-items: center; gap: 8px;">
                        <span>${chStats.percent}%</span>
                        <div class="table-progress-track">
                          <div class="table-progress-fill" style="width: ${chStats.percent}%;"></div>
                        </div>
                      </div>
                    </td>
                    <td>${formatSecondsToShort(timeData.studySeconds)}</td>
                    <td>${formatSecondsToShort(timeData.readingSeconds)}</td>
                    <td>${timeData.reviewsCount || chStats.remembered + chStats.dontRemember}</td>
                    <td>
                      <button class="btn btn-sm ${isCurrent ? 'btn-primary' : ''}" onclick="App.switchChapter('${ch.dir}')">
                        ${isCurrent ? 'Selected' : 'Open'}
                      </button>
                    </td>
                  </tr>
                `;
              }).join('')}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Recent Study Sessions Log -->
      <div class="section-card">
        <div class="section-title">⏱️ Recent Study Sessions</div>
        ${recentSessions.length === 0 ? `
          <div style="font-size: 0.86rem; color: var(--text-dim); padding: 12px 0;">No completed sessions recorded yet. Review cards to log sessions.</div>
        ` : `
          <div class="table-responsive">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Date & Time</th>
                  <th>Mode</th>
                  <th>Chapter</th>
                  <th>Duration</th>
                  <th>Reviews</th>
                  <th>Accuracy</th>
                </tr>
              </thead>
              <tbody>
                ${recentSessions.map(s => `
                  <tr>
                    <td>${new Date(s.timestamp).toLocaleDateString()} ${new Date(s.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</td>
                    <td><span class="badge ${s.mode === 'flashcard' ? 'badge-primary' : 'badge-num'}">${s.mode === 'flashcard' ? '🗂️ Flashcard' : '📖 Dictionary'}</span></td>
                    <td>${s.chapterDir || 'Chapter 1'}</td>
                    <td>${formatSecondsToShort(s.durationSeconds)}</td>
                    <td>${s.reviewsCount || '-'}</td>
                    <td>${s.accuracy ? `${s.accuracy}%` : '-'}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        `}
      </div>

      <!-- Data Management Actions -->
      <div class="section-card" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: gap: 12px;">
        <div>
          <div style="font-weight: 700; font-size: 0.9rem; color: var(--text);">Export & Reset Analytics Data</div>
          <div style="font-size: 0.8rem; color: var(--text-dim);">Download your learning record or clear time metrics.</div>
        </div>
        <div style="display: flex; gap: 8px;">
          <button class="btn btn-primary" onclick="App.exportStudyAnalytics()">
            📥 Export Analytics (JSON)
          </button>
          <button class="btn" style="color: #ef4444; border-color: rgba(239, 68, 68, 0.4);" onclick="App.resetTimeTrackerPrompt()">
            🗑️ Reset Time Tracker
          </button>
        </div>
      </div>
    </div>
  `;
}

// Render Chapters & Word Browser View
function renderChaptersAndWordBrowser({
  chapters = [],
  activeChapter = null,
  allWords = [],
  currentLang = 'both',
  frontierChapter = 'chapter_01',
  searchQuery = '',
  statusFilter = 'all'
}) {
  const container = document.getElementById('chapters-view-container');
  if (!container) return;

  const showEn = currentLang === 'both' || currentLang === 'en';
  const showEs = currentLang === 'both' || currentLang === 'es';

  // 1. Compute Mastery Breakdown for all 8 Chapters
  const chapterCardsHtml = chapters.map(ch => {
    const isFrontier = ch.dir === frontierChapter;
    const chWords = ch.words || allWords.filter(w => w.chapterId === ch.dir);
    const totalWords = chWords.length || ch.word_count || 38;
    const reviews = (typeof StorageManager !== 'undefined') ? StorageManager.getChapterReviews(ch.dir) : {};

    let mastered = 0;
    let review = 0;
    let learning = 0;
    let unlearned = 0;

    chWords.forEach(w => {
      const rev = reviews[String(w.id)];
      if (!rev || rev.state === 'new') {
        unlearned++;
      } else if (rev.state === 'learning' || rev.state === 'relearning') {
        learning++;
      } else if (rev.state === 'review') {
        if ((rev.interval || 0) > 21) mastered++;
        else review++;
      } else {
        unlearned++;
      }
    });

    const masteredPct = Math.round((mastered / totalWords) * 100);
    const reviewPct = Math.round((review / totalWords) * 100);
    const learningPct = Math.round((learning / totalWords) * 100);
    const newPct = 100 - masteredPct - reviewPct - learningPct;

    return `
      <div class="chapter-card-item ${isFrontier ? 'frontier-chapter' : ''}" data-ch="${ch.dir}">
        <div class="chapter-header-row">
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span class="chapter-card-title">${ch.name || 'Chapter'}</span>
              ${isFrontier ? '<span class="chapter-frontier-badge">⭐ Frontier</span>' : ''}
            </div>
            <div class="chapter-card-desc">${ch.title || ''} · ${totalWords} words</div>
          </div>
          <span class="badge" style="font-weight: 700; background: var(--bg-card-sub);">${mastered + review}/${totalWords} Learned</span>
        </div>

        <div class="chapter-stacked-bar" title="Mastered: ${mastered}, Review: ${review}, Learning: ${learning}, New: ${unlearned}">
          <div class="seg-fill" style="width: ${masteredPct}%; background: #10b981;" title="Mastered (>21d): ${mastered}"></div>
          <div class="seg-fill" style="width: ${reviewPct}%; background: #06b6d4;" title="Review (1-21d): ${review}"></div>
          <div class="seg-fill" style="width: ${learningPct}%; background: #f59e0b;" title="Learning / Intraday: ${learning}"></div>
          <div class="seg-fill" style="width: ${Math.max(0, newPct)}%; background: rgba(148, 163, 184, 0.2);" title="New: ${unlearned}"></div>
        </div>

        <div class="chapter-stat-legend">
          <span class="legend-item"><span class="legend-dot" style="background: #10b981;"></span> Mastered ${masteredPct}%</span>
          <span class="legend-item"><span class="legend-dot" style="background: #06b6d4;"></span> Review ${reviewPct}%</span>
          <span class="legend-item"><span class="legend-dot" style="background: #f59e0b;"></span> Learning ${learningPct}%</span>
          <span class="legend-item"><span class="legend-dot" style="background: rgba(148, 163, 184, 0.4);"></span> New ${unlearned}</span>
        </div>

        <div style="display: flex; gap: 8px; margin-top: 6px;">
          <button type="button" class="btn btn-primary" style="flex: 1; font-size: 0.8rem; padding: 6px 10px;" onclick="App.studySpecificChapter('${ch.dir}')">
            🗂️ Study Chapter
          </button>
          <button type="button" class="btn" style="font-size: 0.8rem; padding: 6px 10px;" onclick="App.setFrontierChapter('${ch.dir}')" title="Set this chapter as your active curriculum frontier">
            ${isFrontier ? '⭐ Active' : 'Set Frontier'}
          </button>
        </div>
      </div>
    `;
  }).join('');

  // 2. Filter Word List Table
  let filteredList = [...allWords];
  if (searchQuery) {
    const q = searchQuery.toLowerCase().trim();
    filteredList = filteredList.filter(w => {
      const hz = (w.hanzi || '').toLowerCase();
      const py = (w.pinyin || '').toLowerCase();
      const en = (getWordTranslation(w, 'en') || '').toLowerCase();
      const es = (getWordTranslation(w, 'es') || '').toLowerCase();
      return hz.includes(q) || py.includes(q) || en.includes(q) || es.includes(q);
    });
  }

  if (statusFilter !== 'all') {
    filteredList = filteredList.filter(w => {
      const chDir = w.chapterId || (activeChapter ? activeChapter.dir : 'chapter_01');
      const rev = (typeof StorageManager !== 'undefined') ? StorageManager.getWordReview(chDir, w.id) : null;
      if (statusFilter === 'due') {
        return rev && rev.state !== 'new' && (rev.dueAt || rev.dueDate || 0) <= Date.now();
      }
      if (statusFilter === 'learning') {
        return rev && (rev.state === 'learning' || rev.state === 'relearning');
      }
      if (statusFilter === 'review') {
        return rev && rev.state === 'review';
      }
      if (statusFilter === 'leeches') {
        return rev && (rev.lapses || 0) > 0;
      }
      if (statusFilter === 'new') {
        return !rev || rev.state === 'new';
      }
      return true;
    });
  }

  container.innerHTML = `
    <div>
      <div style="margin-bottom: 20px;">
        <h2 style="font-size: 1.3rem; font-weight: 800; color: var(--text);">📚 Curriculum Chapters & Vocabulary Browser</h2>
        <p style="font-size: 0.84rem; color: var(--text-muted); margin-top: 4px;">Track mastery progress across all 8 HSK chapters and inspect vocabulary with audio and reset controls.</p>
      </div>

      <!-- 8-Chapter Mastery Grid -->
      <div class="chapter-mastery-grid">
        ${chapterCardsHtml}
      </div>

      <!-- Searchable & Filterable Word Table Section -->
      <div class="section-card" style="padding: 20px;">
        <div style="display: flex; flex-direction: column; gap: 14px; margin-bottom: 16px;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
            <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--text);">Vocabulary Catalog (${filteredList.length} words)</h3>
            <div style="display: flex; gap: 6px; flex-wrap: wrap;">
              <button type="button" class="study-filter-pill ${statusFilter === 'all' ? 'active' : ''}" onclick="App.filterBrowserStatus('all')">All</button>
              <button type="button" class="study-filter-pill ${statusFilter === 'due' ? 'active' : ''}" onclick="App.filterBrowserStatus('due')">Due (SRS)</button>
              <button type="button" class="study-filter-pill ${statusFilter === 'learning' ? 'active' : ''}" onclick="App.filterBrowserStatus('learning')">Learning</button>
              <button type="button" class="study-filter-pill ${statusFilter === 'review' ? 'active' : ''}" onclick="App.filterBrowserStatus('review')">Review</button>
              <button type="button" class="study-filter-pill ${statusFilter === 'leeches' ? 'active' : ''}" onclick="App.filterBrowserStatus('leeches')">🔴 Leeches</button>
              <button type="button" class="study-filter-pill ${statusFilter === 'new' ? 'active' : ''}" onclick="App.filterBrowserStatus('new')">New</button>
            </div>
          </div>

          <div class="search-box" style="margin: 0;">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            <input type="text" id="chapter-word-search-input" value="${searchQuery}" placeholder="Search Hanzi, Pinyin, English, Spanish..." oninput="App.onBrowserSearch(this.value)">
            ${searchQuery ? `<button type="button" class="search-clear-btn" onclick="App.onBrowserSearch('')">&times;</button>` : ''}
          </div>
        </div>

        <div class="table-responsive" style="max-height: 600px; overflow-y: auto;">
          <table class="data-table">
            <thead>
              <tr>
                <th style="width: 50px;">#</th>
                <th>Hanzi & Pinyin</th>
                <th>Part of Speech</th>
                <th>Translation</th>
                <th>SRS State</th>
                <th>Lapses</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              ${filteredList.map((w, idx) => {
                const chDir = w.chapterId || (activeChapter ? activeChapter.dir : 'chapter_01');
                const rev = (typeof StorageManager !== 'undefined') ? StorageManager.getWordReview(chDir, w.id) : null;
                const badge = renderSRSStatusBadge(rev);
                const lapses = rev?.lapses || 0;
                const enStr = getWordTranslation(w, 'en');
                const esStr = getWordTranslation(w, 'es');
                const trans = showEn && showEs
                  ? (enStr && esStr ? `${enStr} / ${esStr}` : (enStr || esStr))
                  : (showEs ? esStr : enStr);

                return `
                  <tr>
                    <td><span class="badge badge-num">${idx + 1}</span></td>
                    <td>
                      <div style="display: flex; flex-direction: column;">
                        <span style="font-size: 1.15rem; font-weight: 700; cursor: pointer;" onclick="App.openWordDetail('${chDir}', '${w.id}')">${w.hanzi}</span>
                        <span style="font-size: 0.78rem;">${colorizePinyinHTML(w.pinyin || '')}</span>
                      </div>
                    </td>
                    <td><span class="badge badge-pos">${w.part_of_speech || 'Word'}</span></td>
                    <td style="max-width: 260px; font-size: 0.82rem; color: var(--text-muted);">${trans || '-'}</td>
                    <td>${badge}</td>
                    <td>${lapses > 0 ? `<span class="leech-lapse-badge">🔴 ${lapses}x</span>` : '<span style="color: var(--text-dim);">-</span>'}</td>
                    <td>
                      <div style="display: flex; gap: 4px;">
                        <button type="button" class="btn" style="padding: 3px 8px; font-size: 0.75rem;" onclick="speak('${(w.hanzi || '').replace(/'/g, "\\'")}', 1.0)" title="Play Pronunciation">🔊</button>
                        <button type="button" class="btn" style="padding: 3px 8px; font-size: 0.75rem;" onclick="App.openWordDetail('${chDir}', '${w.id}')" title="Inspect Word Details">🔍</button>
                        <button type="button" class="btn" style="padding: 3px 8px; font-size: 0.75rem; color: #ef4444; border-color: rgba(239, 68, 68, 0.3);" onclick="App.confirmResetWord('${chDir}', '${w.id}')" title="Reset Card Progress to New">🗑️</button>
                      </div>
                    </td>
                  </tr>
                `;
              }).join('')}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  `;
}

// Render Word Detail Modal
function renderWordDetailModal(word, reviewItem, chapterDir, currentLang = 'both') {
  const modalEl = document.getElementById('word-detail-modal');
  const titleEl = document.getElementById('word-detail-title');
  const bodyEl = document.getElementById('word-detail-body');
  if (!modalEl || !titleEl || !bodyEl || !word) return;

  const showEn = currentLang === 'both' || currentLang === 'en';
  const showEs = currentLang === 'both' || currentLang === 'es';
  const statusBadge = renderSRSStatusBadge(reviewItem);
  const decomp = word.character_decomposition || [];

  titleEl.innerHTML = `📖 ${word.hanzi} · ${colorizePinyinHTML(word.pinyin || '')}`;
  bodyEl.innerHTML = `
    <div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <span style="font-size: 2.2rem; font-weight: 800; color: var(--text);">${word.hanzi}</span>
          <div style="display: flex; flex-direction: column;">
            <span style="font-size: 1.15rem; font-weight: 700;">${colorizePinyinHTML(word.pinyin || '')}</span>
            <span style="font-size: 0.75rem; color: var(--text-dim);">${word.part_of_speech || 'Word'} · ${word.level || 'HSK 5'}</span>
          </div>
        </div>
        ${statusBadge}
      </div>

      <div style="display: flex; gap: 8px; margin-bottom: 16px;">
        <button type="button" class="btn btn-primary" onclick="speak('${word.hanzi}', 1.0)">🔊 Normal (1.0x)</button>
        <button type="button" class="btn" onclick="speak('${word.hanzi}', 0.75)">🐢 Slow (0.75x)</button>
      </div>

      <div style="margin-bottom: 16px; background: var(--bg-card-sub); padding: 12px; border-radius: 10px;">
        <div style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); margin-bottom: 4px;">TRANSLATIONS</div>
        ${showEn ? `<div style="font-size: 0.88rem; margin-bottom: 2px;"><strong>EN:</strong> ${getWordTranslation(word, 'en') || '-'}</div>` : ''}
        ${showEs ? `<div style="font-size: 0.88rem;"><strong>ES:</strong> ${getWordTranslation(word, 'es') || '-'}</div>` : ''}
      </div>

      ${decomp.length > 0 ? `
        <div style="margin-bottom: 16px; background: var(--bg-card-sub); padding: 12px; border-radius: 10px;">
          <div style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); margin-bottom: 4px;">RADICAL BREAKDOWN</div>
          <div style="font-size: 0.82rem;">
            ${decomp.map(d => `<strong>${d.character}</strong>: Radical ${d.radical} (${d.radical_meaning_en || ''})`).join(' · ')}
          </div>
        </div>
      ` : ''}

      ${Array.isArray(word.example_sentences) && word.example_sentences.length > 0 ? `
        <div style="margin-bottom: 16px;">
          <div style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); margin-bottom: 6px;">EXAMPLE SENTENCE</div>
          <div style="background: var(--bg-card-sub); padding: 12px; border-radius: 10px;">
            <div style="font-size: 0.95rem; font-weight: 600; margin-bottom: 4px;">${word.example_sentences[0].hanzi}</div>
            <div style="font-size: 0.82rem; margin-bottom: 4px;">${colorizePinyinHTML(word.example_sentences[0].pinyin)}</div>
            ${showEn ? `<div style="font-size: 0.8rem; color: var(--text-muted);"><strong>EN:</strong> ${word.example_sentences[0].en}</div>` : ''}
            <div style="margin-top: 8px;">
              <button type="button" class="btn" style="padding: 2px 8px; font-size: 0.75rem;" onclick="speak('${(word.example_sentences[0].hanzi || '').replace(/'/g, "\\'")}', 1.0)">🔊 Listen Sentence</button>
            </div>
          </div>
        </div>
      ` : ''}

      <div style="display: flex; gap: 8px; margin-top: 20px; border-top: 1px solid var(--border); padding-top: 16px;">
        <button type="button" class="btn btn-primary" style="flex: 1;" onclick="App.studySpecificWord('${chapterDir}', '${word.id}')">
          🗂️ Study This Word
        </button>
        <button type="button" class="btn" style="color: #ef4444; border-color: rgba(239, 68, 68, 0.4);" onclick="App.confirmResetWord('${chapterDir}', '${word.id}')">
          🗑️ Reset Progress
        </button>
      </div>
    </div>
  `;

  modalEl.classList.add('active');
}

if (typeof window !== 'undefined') {
  window.speak = speak;
  window.getWordTranslation = getWordTranslation;
  window.colorizePinyinHTML = colorizePinyinHTML;
  window.computeToneContour = computeToneContour;
  window.highlightHeadword = highlightHeadword;
  window.renderSidebar = renderSidebar;
  window.renderFlashcardFront = renderFlashcardFront;
  window.renderFlashcardBack = renderFlashcardBack;
  window.renderActionBar = renderActionBar;
  window.renderCompletionScreen = renderCompletionScreen;
  window.renderBrowseView = renderBrowseView;
  window.renderDictionaryWindow = renderDictionaryWindow;
  window.renderCharacterTimeline = renderCharacterTimeline;
  window.renderStatisticsDashboard = renderStatisticsDashboard;
  window.renderWordMiniTimeline = renderWordMiniTimeline;
  window.renderStudyFilterPills = renderStudyFilterPills;
  window.renderSRSStatusBadge = renderSRSStatusBadge;
  window.renderChapterOriginBadge = renderChapterOriginBadge;
  window.renderChaptersAndWordBrowser = renderChaptersAndWordBrowser;
  window.renderWordDetailModal = renderWordDetailModal;
  window.formatSecondsToHMS = formatSecondsToHMS;
  window.formatSecondsToShort = formatSecondsToShort;
}

