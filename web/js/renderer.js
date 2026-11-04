/**
 * Renderer module for Chinese Vocal HSK Visualizer.
 * Generates DOM structures for the sidebar word list and the detailed lexical cards.
 */

function speak(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'zh-CN';
  u.rate = 0.9;
  window.speechSynthesis.speak(u);
}

function renderSidebar(filteredWords, allWords, currentIndex, currentLang, onSelect) {
  const listEl = document.getElementById('word-list');
  listEl.innerHTML = '';
  const currentWord = allWords[currentIndex];

  filteredWords.forEach((w) => {
    const isSelected = currentWord && currentWord.id === w.id;
    const item = document.createElement('div');
    item.className = `word-item ${isSelected ? 'active' : ''}`;
    item.innerHTML = `
      <div class="num">${String(w.id).padStart(2, '0')}</div>
      <div class="meta-col">
        <div style="display: flex; align-items: baseline; justify-content: space-between;">
          <span class="hanzi-sm">${w.hanzi}</span>
          <span class="pos-tag">${w.part_of_speech}</span>
        </div>
        <div class="pinyin-sm">${w.pinyin}</div>
        <div class="meaning-sm">${currentLang === 'es' ? (w.meanings_summary.es || '') : (w.meanings_summary.en || '')}</div>
      </div>
    `;
    item.onclick = () => onSelect(w.id);
    listEl.appendChild(item);
  });
}

function renderDetail(w, currentLang) {
  const container = document.getElementById('detail-container');
  if (!w) {
    container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-dim);">No word selected.</div>';
    return;
  }

  const showEn = currentLang === 'both' || currentLang === 'en';
  const showEs = currentLang === 'both' || currentLang === 'es';

  // Senses HTML
  const senses = w.senses || [];
  const sensesHtml = senses.map(s => `
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
  `).join('');

  // Example Sentences HTML
  const sentences = w.example_sentences || [];
  const sentencesHtml = sentences.map(sent => `
    <div class="sentence-card">
      <span class="tag-ctx">${sent.id === '#1' ? 'Context: Daily / Life' : 'Context: Formal / Professional'}</span>
      <div class="sentence-hanzi">${sent.hanzi}</div>
      <div class="sentence-pinyin">${sent.pinyin}</div>
      ${showEn ? `<div class="sentence-trans"><strong>EN:</strong> ${sent.en}</div>` : ''}
      ${showEs ? `<div class="sentence-trans"><strong>ES:</strong> ${sent.es}</div>` : ''}
      <div style="margin-top: 10px;">
        <button class="btn btn-icon" style="padding: 3px 8px; font-size: 0.75rem;" onclick="speak('${sent.hanzi}')">🔊 Listen</button>
      </div>
    </div>
  `).join('');

  // Collocations HTML
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

  // Idioms HTML
  const idioms = w.idioms || [];
  const idiomsHtml = idioms.map(im => `
    <div class="colloc-item" onclick="speak('${im.hanzi}')">
      <div class="colloc-hanzi">
        <span>${im.hanzi}</span>
        <span style="font-size: 0.8rem; color: var(--primary);">🔊</span>
      </div>
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: var(--primary);">${im.pinyin}</div>
      <div class="colloc-en">${im.meaning_en}</div>
    </div>
  `).join('');

  // Character Decomposition HTML
  const decomp = w.character_decomposition || [];
  const decompHtml = decomp.map(ch => `
    <div class="decomp-card">
      <div class="decomp-header">
        <div class="char-big">${ch.character}</div>
        <div class="char-meta-top">
          <div style="display: flex; align-items: baseline; gap: 8px;">
            <span class="char-pinyin">${ch.pinyin}</span>
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
      ${showEn ? `<div class="mnemonic-story"><strong>Visual Hook (EN):</strong> ${ch.visual_mnemonic_story_en}</div>` : ''}
      ${showEs ? `<div class="mnemonic-story" style="border-left-color: var(--accent-green);"><strong>Visual Hook (ES):</strong> ${ch.visual_mnemonic_story_es}</div>` : ''}
    </div>
  `).join('');

  // Look-alikes HTML
  const traps = w.traps_and_cognates || {};
  const lookAlikes = traps.look_alikes || [];
  const lookAlikesHtml = lookAlikes.map(la => `
    <tr>
      <td class="char-cell" onclick="speak('${la.character}')">${la.character} <span style="font-size: 0.75rem; cursor: pointer;">🔊</span></td>
      <td style="font-family: 'JetBrains Mono', monospace; color: var(--primary);">${la.pinyin}</td>
      <td>${la.meaning_en}</td>
      <td style="color: var(--text-muted); font-size: 0.8rem;">${la.distinction_note}</td>
    </tr>
  `).join('');

  // Etymological Cognates HTML
  const cognates = traps.etymological_cognates || [];
  const cognatesHtml = cognates.map(cg => `
    <div class="cognate-chip" onclick="speak('${cg.character}')">
      <span class="ch">${cg.character}</span>
      <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: var(--primary);">${cg.pinyin}</span>
      <span style="color: var(--text-dim); font-size: 0.72rem;">${cg.gloss_en}</span>
    </div>
  `).join('');

  // Semantic Boundary Contrasts HTML
  const sbc = w.semantic_boundary_contrasts || {};
  const contrasts = sbc.contrasts || [];
  const contrastsHtml = contrasts.map(ct => `
    <div class="contrast-item">
      <div class="contrast-header">
        <span class="contrast-pair">${ct.compared_word}</span>
        <span class="contrast-pinyin">${ct.pinyin}</span>
      </div>
      <div class="contrast-desc">${ct.analysis}</div>
    </div>
  `).join('');

  // Extended Reading Passages HTML
  const passages = w.extended_reading_passages || [];
  const passagesHtml = passages.map((p, idx) => `
    <div class="passage-block">
      <div class="passage-header">
        <span class="passage-badge">${idx === 0 ? 'Passage #1: Reflective / Philosophical' : 'Passage #2: Socio-economic / Formal'}</span>
        <button class="btn btn-icon" onclick="speak('${p.hanzi}')">🔊 Read Passage</button>
      </div>
      <div class="passage-hanzi">${p.hanzi}</div>
      <div class="passage-pinyin">${p.pinyin}</div>
      ${showEn ? `<div class="passage-trans" style="margin-bottom: 8px;"><strong>EN:</strong> ${p.en}</div>` : ''}
      ${showEs ? `<div class="passage-trans"><strong>ES:</strong> ${p.es}</div>` : ''}
    </div>
  `).join('');

  const mr = w.mnemonics_and_roots || {};

  container.innerHTML = `
    <!-- Hero Header -->
    <div class="hero-card">
      <div class="hero-top">
        <div class="hero-main">
          <span class="hanzi-hero">${w.hanzi}</span>
          <span class="pinyin-hero">${w.pinyin}</span>
          <button class="audio-btn" title="Pronounce Word" onclick="speak('${w.hanzi}')">🔊</button>
        </div>
        <div class="hero-badges">
          <span class="badge badge-num">NO. ${String(w.id).padStart(2, '0')}</span>
          <span class="badge badge-hsk">${w.level || 'HSK 5'}</span>
          <span class="badge badge-pos">${w.part_of_speech}</span>
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

    <!-- Senses & Usage -->
    <div class="section-card">
      <div class="section-title">
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
        Core Lexical Senses (${senses.length})
      </div>
      ${sensesHtml}
    </div>

    <!-- Example Sentences -->
    <div class="section-card">
      <div class="section-title">
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
        Contextual Example Sentences (${sentences.length})
      </div>
      ${sentencesHtml}
    </div>

    <!-- Collocations & Idioms Grid -->
    <div class="grid-2">
      <div class="section-card" style="margin-bottom: 0;">
        <div class="section-title">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          High-Frequency Collocations (${collocations.length})
        </div>
        <div class="colloc-grid">${collocHtml}</div>
      </div>

      <div class="section-card" style="margin-bottom: 0;">
        <div class="section-title">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          Classical Idioms (成语 ${idioms.length})
        </div>
        <div class="colloc-grid">${idiomsHtml}</div>
      </div>
    </div>
    <div style="height: 20px;"></div>

    <!-- Character Decomposition -->
    <div class="section-card">
      <div class="section-title">
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
        Character Decomposition & Etymology (K=${decomp.length})
      </div>
      <div class="decomp-grid">${decompHtml}</div>
    </div>

    <!-- Mnemonics & Cognitive Roots -->
    <div class="section-card">
      <div class="section-title">
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path></svg>
        Memory Hooks & Cultural Foundations
      </div>
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

    <!-- Traps & Cognates -->
    <div class="grid-2">
      <div class="section-card" style="margin-bottom: 0;">
        <div class="section-title">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
          Look-Alike Characters (字形陷阱)
        </div>
        <table class="data-table">
          <thead>
            <tr>
              <th>Char</th>
              <th>Pinyin</th>
              <th>Meaning</th>
              <th>Distinction</th>
            </tr>
          </thead>
          <tbody>${lookAlikesHtml}</tbody>
        </table>
      </div>

      <div class="section-card" style="margin-bottom: 0;">
        <div class="section-title">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
          Etymological Cognates Family (同族字)
        </div>
        <div class="cognate-chips">${cognatesHtml}</div>
      </div>
    </div>
    <div style="height: 20px;"></div>

    <!-- Semantic Contrasts -->
    <div class="section-card">
      <div class="section-title">
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
        Semantic Boundary Contrasts (${contrasts.length})
      </div>
      ${sbc.core_nuance ? `
        <div style="margin-bottom: 14px; font-size: 0.92rem; color: var(--text);">
          <strong>Core Semantic Nuance:</strong> ${sbc.core_nuance}
        </div>` : ''}
      ${contrastsHtml}
    </div>

    <!-- Extended Reading Passages -->
    <div class="section-card">
      <div class="section-title">
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"></path></svg>
        Extended Reading Passages (${passages.length})
      </div>
      ${passagesHtml}
    </div>
  `;
}
