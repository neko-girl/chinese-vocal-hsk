import json, html

with open('words_data.json', 'r', encoding='utf-8') as f:
    words_data = json.load(f)

json_str = json.dumps(words_data, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HSK 5 Chinese Vocabulary Visualizer - Chapter 1</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0f172a;
      --bg-card: #1e293b;
      --bg-card-sub: #162032;
      --border: #334155;
      --border-accent: #3b82f6;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --primary: #38bdf8;
      --primary-glow: rgba(56, 189, 248, 0.2);
      --accent: #f59e0b;
      --accent-green: #10b981;
      --accent-purple: #a855f7;
      --accent-rose: #f43f5e;
      --sidebar-w: 320px;
      --radius: 12px;
      --radius-sm: 8px;
    }}

    [data-theme="light"] {{
      --bg: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-sub: #f1f5f9;
      --border: #e2e8f0;
      --border-accent: #2563eb;
      --text: #0f172a;
      --text-muted: #475569;
      --text-dim: #94a3b8;
      --primary: #0284c7;
      --primary-glow: rgba(2, 132, 199, 0.15);
      --accent: #d97706;
      --accent-green: #059669;
      --accent-purple: #9333ea;
      --accent-rose: #e11d48;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
      background: var(--bg);
      color: var(--text);
      display: flex;
      height: 100vh;
      overflow: hidden;
      line-height: 1.5;
    }}

    /* Sidebar */
    aside {{
      width: var(--sidebar-w);
      min-width: var(--sidebar-w);
      background: var(--bg-card);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      height: 100%;
      z-index: 20;
    }}

    .sidebar-header {{
      padding: 18px 20px 14px;
      border-bottom: 1px solid var(--border);
    }}

    .logo-area {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }}

    .logo-badge {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 800;
      font-size: 1.05rem;
      color: var(--primary);
    }}

    .logo-badge span.pill {{
      background: var(--primary);
      color: #0f172a;
      padding: 2px 8px;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
    }}

    .search-box {{
      position: relative;
      margin-bottom: 10px;
    }}

    .search-box input {{
      width: 100%;
      padding: 8px 12px 8px 32px;
      background: var(--bg-card-sub);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      color: var(--text);
      font-size: 0.85rem;
      outline: none;
      transition: all 0.2s;
    }}

    .search-box input:focus {{
      border-color: var(--primary);
      box-shadow: 0 0 0 3px var(--primary-glow);
    }}

    .search-box svg {{
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      width: 15px;
      height: 15px;
      color: var(--text-dim);
    }}

    .pos-filters {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }}
    .pos-filters::-webkit-scrollbar {{ display: none; }}

    .filter-chip {{
      padding: 3px 9px;
      background: var(--bg-card-sub);
      border: 1px solid var(--border);
      border-radius: 999px;
      font-size: 0.72rem;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s;
    }}

    .filter-chip.active, .filter-chip:hover {{
      background: var(--primary);
      color: #0f172a;
      border-color: var(--primary);
      font-weight: 600;
    }}

    .word-list {{
      flex: 1;
      overflow-y: auto;
      padding: 8px 10px;
    }}

    .word-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.15s;
      margin-bottom: 4px;
      border: 1px solid transparent;
    }}

    .word-item:hover {{
      background: var(--bg-card-sub);
      border-color: var(--border);
    }}

    .word-item.active {{
      background: var(--primary-glow);
      border-color: var(--primary);
    }}

    .word-item .num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      color: var(--text-dim);
      font-weight: 600;
      min-width: 22px;
    }}

    .word-item .hanzi-sm {{
      font-family: 'Noto Serif SC', serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text);
    }}

    .word-item.active .hanzi-sm {{
      color: var(--primary);
    }}

    .word-item .meta-col {{
      flex: 1;
      min-width: 0;
    }}

    .word-item .pinyin-sm {{
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 500;
    }}

    .word-item .meaning-sm {{
      font-size: 0.72rem;
      color: var(--text-dim);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .word-item .pos-tag {{
      font-size: 0.65rem;
      padding: 1px 6px;
      border-radius: 4px;
      background: var(--bg);
      color: var(--text-muted);
      border: 1px solid var(--border);
    }}

    /* Main Container */
    main {{
      flex: 1;
      height: 100%;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      position: relative;
    }}

    /* Top Navigation Bar */
    header.topbar {{
      position: sticky;
      top: 0;
      background: var(--bg);
      border-bottom: 1px solid var(--border);
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 10;
      backdrop-filter: blur(12px);
    }}

    .nav-controls {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text);
      transition: all 0.15s;
    }}

    .btn:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}

    .btn-icon {{
      padding: 6px 10px;
    }}

    .lang-toggle {{
      display: flex;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 2px;
    }}

    .lang-btn {{
      padding: 4px 10px;
      font-size: 0.75rem;
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      border-radius: 6px;
      font-weight: 600;
      transition: all 0.15s;
    }}

    .lang-btn.active {{
      background: var(--primary);
      color: #0f172a;
    }}

    /* Content Area */
    .content-wrap {{
      max-width: 1050px;
      margin: 0 auto;
      padding: 28px;
      width: 100%;
    }}

    /* Hero Card */
    .hero-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 28px 32px;
      margin-bottom: 24px;
      position: relative;
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.2);
    }}

    .hero-top {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 20px;
      margin-bottom: 16px;
    }}

    .hero-main {{
      display: flex;
      align-items: baseline;
      gap: 20px;
      flex-wrap: wrap;
    }}

    .hanzi-hero {{
      font-family: 'Noto Serif SC', serif;
      font-size: 3.8rem;
      font-weight: 900;
      color: var(--text);
      letter-spacing: 2px;
      line-height: 1;
    }}

    .pinyin-hero {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.5rem;
      color: var(--primary);
      font-weight: 600;
    }}

    .hero-badges {{
      display: flex;
      gap: 8px;
      align-items: center;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 10px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .badge-hsk {{ background: rgba(56, 189, 248, 0.15); color: var(--primary); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-pos {{ background: rgba(245, 158, 11, 0.15); color: var(--accent); border: 1px solid rgba(245, 158, 11, 0.3); }}
    .badge-num {{ background: var(--bg-card-sub); color: var(--text-muted); border: 1px solid var(--border); }}

    .audio-btn {{
      background: var(--primary-glow);
      border: 1px solid var(--primary);
      color: var(--primary);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .audio-btn:hover {{
      transform: scale(1.08);
      background: var(--primary);
      color: #0f172a;
    }}

    .hero-summary {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      background: var(--bg-card-sub);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 14px 18px;
    }}

    .summary-box .label {{
      font-size: 0.7rem;
      text-transform: uppercase;
      color: var(--text-dim);
      font-weight: 700;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .summary-box .text {{
      font-size: 0.95rem;
      color: var(--text);
      font-weight: 500;
    }}

    /* Grid Sections */
    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 20px;
    }}

    .section-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 22px;
      margin-bottom: 20px;
    }}

    .section-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.6px;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 16px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border);
    }}

    .section-title svg {{
      color: var(--primary);
    }}

    /* Senses */
    .sense-row {{
      background: var(--bg-card-sub);
      border-left: 3px solid var(--primary);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      padding: 12px 16px;
      margin-bottom: 10px;
    }}

    .sense-meta {{
      display: flex;
      gap: 8px;
      align-items: center;
      margin-bottom: 6px;
    }}

    .sense-def {{
      font-size: 0.92rem;
      margin-bottom: 4px;
    }}

    .sense-eg {{
      font-size: 0.82rem;
      color: var(--primary);
      font-family: 'Noto Serif SC', serif;
      background: rgba(56, 189, 248, 0.08);
      padding: 2px 8px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-top: 4px;
      cursor: pointer;
    }}

    /* Sentences */
    .sentence-card {{
      background: var(--bg-card-sub);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 16px 18px;
      margin-bottom: 12px;
      position: relative;
    }}

    .sentence-card .tag-ctx {{
      position: absolute;
      top: 12px;
      right: 14px;
      font-size: 0.68rem;
      color: var(--text-dim);
      background: var(--bg);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid var(--border);
    }}

    .sentence-hanzi {{
      font-family: 'Noto Serif SC', serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 6px;
      line-height: 1.6;
      padding-right: 80px;
    }}

    .sentence-pinyin {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      color: var(--primary);
      margin-bottom: 8px;
      line-height: 1.4;
    }}

    .sentence-trans {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 4px;
    }}

    /* Collocations & Idioms Grid */
    .colloc-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 10px;
    }}

    .colloc-item {{
      background: var(--bg-card-sub);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      gap: 2px;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .colloc-item:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
    }}

    .colloc-hanzi {{
      font-family: 'Noto Serif SC', serif;
      font-size: 1rem;
      font-weight: 700;
      color: var(--text);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .colloc-en {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    /* Character Decomposition Cards */
    .decomp-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 16px;
    }}

    .decomp-card {{
      background: var(--bg-card-sub);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .decomp-header {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .char-big {{
      font-family: 'Noto Serif SC', serif;
      font-size: 2.6rem;
      font-weight: 900;
      color: var(--primary);
      line-height: 1;
      width: 52px;
      height: 52px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
    }}

    .char-meta-top {{
      flex: 1;
    }}

    .char-pinyin {{
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--text);
      font-size: 1.1rem;
    }}

    .char-pills {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-top: 4px;
    }}

    .pill-sm {{
      font-size: 0.68rem;
      padding: 1px 6px;
      border-radius: 4px;
      background: var(--bg);
      color: var(--text-muted);
      border: 1px solid var(--border);
    }}

    .decomp-detail-row {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    .decomp-detail-row strong {{
      color: var(--text);
    }}

    .mnemonic-story {{
      background: var(--bg);
      border-left: 2px solid var(--accent);
      padding: 8px 12px;
      font-size: 0.78rem;
      color: var(--text);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-top: 4px;
    }}

    /* Mnemonics & Roots Callout */
    .alert-box {{
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      margin-bottom: 14px;
    }}

    .alert-box.blue {{
      background: rgba(56, 189, 248, 0.08);
      border-color: rgba(56, 189, 248, 0.3);
    }}

    .alert-title {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .alert-box.blue .alert-title {{
      color: var(--primary);
    }}

    /* Contrasts Table */
    .contrast-item {{
      background: var(--bg-card-sub);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
      margin-bottom: 10px;
    }}

    .contrast-header {{
      display: flex;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 6px;
    }}

    .contrast-pair {{
      font-family: 'Noto Serif SC', serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text);
    }}

    .contrast-pinyin {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      color: var(--primary);
    }}

    .contrast-desc {{
      font-size: 0.84rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Reading Passages */
    .passage-block {{
      background: var(--bg-card-sub);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 20px;
      margin-bottom: 16px;
    }}

    .passage-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }}

    .passage-badge {{
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      background: var(--primary-glow);
      color: var(--primary);
      border: 1px solid var(--primary);
    }}

    .passage-hanzi {{
      font-family: 'Noto Serif SC', serif;
      font-size: 1.15rem;
      line-height: 1.8;
      color: var(--text);
      margin-bottom: 12px;
      letter-spacing: 0.5px;
    }}

    .passage-pinyin {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      color: var(--primary);
      margin-bottom: 12px;
      line-height: 1.6;
    }}

    .passage-trans {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    /* Table styles for lookalikes */
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
    }}

    table.data-table th, table.data-table td {{
      padding: 8px 12px;
      text-align: left;
      border-bottom: 1px solid var(--border);
    }}

    table.data-table th {{
      color: var(--text-dim);
      font-size: 0.72rem;
      text-transform: uppercase;
      font-weight: 700;
      background: var(--bg-card-sub);
    }}

    table.data-table td.char-cell {{
      font-family: 'Noto Serif SC', serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary);
    }}

    .cognate-chips {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 10px;
    }}

    .cognate-chip {{
      background: var(--bg-card-sub);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .cognate-chip .ch {{
      font-family: 'Noto Serif SC', serif;
      font-weight: 700;
      color: var(--accent);
      font-size: 0.95rem;
    }}

    /* Responsive */
    @media (max-width: 900px) {{
      aside {{
        position: fixed;
        left: -100%;
        transition: left 0.3s;
      }}
      aside.open {{
        left: 0;
      }}
      .grid-2 {{
        grid-template-columns: 1fr;
      }}
      .hero-summary {{
        grid-template-columns: 1fr;
      }}
      .content-wrap {{
        padding: 16px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Left Sidebar Navigation -->
  <aside id="sidebar">
    <div class="sidebar-header">
      <div class="logo-area">
        <div class="logo-badge">
          <span>HSK 5 VOCAB</span>
          <span class="pill">CHP 1</span>
        </div>
        <button class="btn btn-icon" id="theme-btn" title="Toggle Light/Dark Theme">🌓</button>
      </div>
      <div class="search-box">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        <input type="text" id="search-input" placeholder="Search Hanzi, Pinyin, EN, ES...">
      </div>
      <div class="pos-filters" id="pos-filters">
        <button class="filter-chip active" data-pos="ALL">All (38)</button>
        <button class="filter-chip" data-pos="Noun">Noun</button>
        <button class="filter-chip" data-pos="Verb">Verb</button>
        <button class="filter-chip" data-pos="Adjective">Adjective</button>
        <button class="filter-chip" data-pos="Adverb">Adverb</button>
        <button class="filter-chip" data-pos="Pronoun">Pronoun</button>
        <button class="filter-chip" data-pos="Measure Word">Measure Word</button>
        <button class="filter-chip" data-pos="Idiom">Idiom</button>
      </div>
    </div>

    <div class="word-list" id="word-list">
      <!-- Populated via JS -->
    </div>
  </aside>

  <!-- Main View Area -->
  <main id="main-scroll">
    <header class="topbar">
      <div class="nav-controls">
        <button class="btn btn-icon" id="toggle-sidebar-btn" title="Toggle Sidebar">☰</button>
        <button class="btn" id="prev-btn">← Prev</button>
        <button class="btn" id="next-btn">Next →</button>
        <span style="font-size: 0.82rem; color: var(--text-dim);" id="word-counter">01 / 38</span>
      </div>

      <div class="nav-controls">
        <div class="lang-toggle">
          <button class="lang-btn active" data-lang="both">Bilingual</button>
          <button class="lang-btn" data-lang="en">EN</button>
          <button class="lang-btn" data-lang="es">ES</button>
        </div>
      </div>
    </header>

    <div class="content-wrap" id="detail-container">
      <!-- Word details rendered dynamically -->
    </div>
  </main>

  <!-- Embedded Dataset -->
  <script>
    const WORDS = {json_str};
  </script>

  <!-- Application Logic -->
  <script>
    let currentIndex = 0;
    let filteredWords = [...WORDS];
    let currentLang = 'both'; // 'both', 'en', 'es'
    let currentPosFilter = 'ALL';

    // Speech synthesis helper
    function speak(text) {{
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'zh-CN';
      u.rate = 0.9;
      window.speechSynthesis.speak(u);
    }}

    // Render word item in sidebar
    function renderSidebar() {{
      const listEl = document.getElementById('word-list');
      listEl.innerHTML = '';

      filteredWords.forEach((w, idx) => {{
        const isSelected = WORDS[currentIndex].id === w.id;
        const item = document.createElement('div');
        item.className = `word-item ${{isSelected ? 'active' : ''}}`;
        item.innerHTML = `
          <div class="num">${{String(w.id).padStart(2, '0')}}</div>
          <div class="meta-col">
            <div style="display: flex; align-items: baseline; justify-content: space-between;">
              <span class="hanzi-sm">${{w.hanzi}}</span>
              <span class="pos-tag">${{w.part_of_speech}}</span>
            </div>
            <div class="pinyin-sm">${{w.pinyin}}</div>
            <div class="meaning-sm">${{currentLang === 'es' ? w.meanings_summary.es : w.meanings_summary.en}}</div>
          </div>
        `;
        item.onclick = () => {{
          const realIdx = WORDS.findIndex(item => item.id === w.id);
          selectWord(realIdx);
        }};
        listEl.appendChild(item);
      }});
    }}

    function selectWord(index) {{
      currentIndex = index;
      renderDetail(WORDS[currentIndex]);
      renderSidebar();
      document.getElementById('word-counter').textContent = `${{String(WORDS[currentIndex].id).padStart(2, '0')}} / ${{WORDS.length}}`;
      document.getElementById('main-scroll').scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function renderDetail(w) {{
      const container = document.getElementById('detail-container');
      const showEn = currentLang === 'both' || currentLang === 'en';
      const showEs = currentLang === 'both' || currentLang === 'es';

      // Senses HTML
      const sensesHtml = w.senses.map(s => `
        <div class="sense-row">
          <div class="sense-meta">
            <span class="badge badge-pos">${{s.part_of_speech}}</span>
            <span class="badge badge-num">${{s.register}}</span>
          </div>
          ${{showEn ? `<div class="sense-def"><strong>EN:</strong> ${{s.definition_en}}</div>` : ''}}
          ${{showEs ? `<div class="sense-def" style="color: var(--text-muted);"><strong>ES:</strong> ${{s.definition_es}}</div>` : ''}}
          <div class="sense-eg" onclick="speak('${{s.example_phrase.split(' ')[0]}}')">
            <span>🔊 ${{s.example_phrase}}</span>
          </div>
        </div>
      `).join('');

      // Example Sentences HTML
      const sentencesHtml = w.example_sentences.map(sent => `
        <div class="sentence-card">
          <span class="tag-ctx">${{sent.id === '#1' ? 'Context: Daily / Life' : 'Context: Formal / Professional'}}</span>
          <div class="sentence-hanzi">${{sent.hanzi}}</div>
          <div class="sentence-pinyin">${{sent.pinyin}}</div>
          ${{showEn ? `<div class="sentence-trans"><strong>EN:</strong> ${{sent.en}}</div>` : ''}}
          ${{showEs ? `<div class="sentence-trans"><strong>ES:</strong> ${{sent.es}}</div>` : ''}}
          <div style="margin-top: 10px;">
            <button class="btn btn-icon" style="padding: 3px 8px; font-size: 0.75rem;" onclick="speak('${{sent.hanzi}}')">🔊 Listen</button>
          </div>
        </div>
      `).join('');

      // Collocations HTML
      const collocHtml = w.collocations.map(c => `
        <div class="colloc-item" onclick="speak('${{c.hanzi}}')">
          <div class="colloc-hanzi">
            <span>${{c.hanzi}}</span>
            <span style="font-size: 0.8rem; color: var(--primary);">🔊</span>
          </div>
          <div class="colloc-en">${{c.en}}</div>
        </div>
      `).join('');

      // Idioms HTML
      const idiomsHtml = w.idioms.map(im => `
        <div class="colloc-item" onclick="speak('${{im.hanzi}}')">
          <div class="colloc-hanzi">
            <span>${{im.hanzi}}</span>
            <span style="font-size: 0.8rem; color: var(--primary);">🔊</span>
          </div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: var(--primary);">${{im.pinyin}}</div>
          <div class="colloc-en">${{im.meaning_en}}</div>
        </div>
      `).join('');

      // Character Decomposition HTML
      const decompHtml = w.character_decomposition.map(ch => `
        <div class="decomp-card">
          <div class="decomp-header">
            <div class="char-big">${{ch.character}}</div>
            <div class="char-meta-top">
              <div style="display: flex; align-items: baseline; gap: 8px;">
                <span class="char-pinyin">${{ch.pinyin}}</span>
                <span class="badge badge-pos">Tone ${{ch.tone_mnemonic_anchor}}</span>
                <button class="btn btn-icon" style="padding: 2px 6px; font-size: 0.7rem;" onclick="speak('${{ch.character}}')">🔊</button>
              </div>
              <div class="char-pills">
                <span class="pill-sm">Rad: ${{ch.radical}} (${{ch.radical_meaning_en}})</span>
                <span class="pill-sm">${{ch.stroke_count}} strokes</span>
                <span class="pill-sm">${{ch.composition_type}}</span>
                ${{ch.cangjie ? `<span class="pill-sm">CJ: ${{ch.cangjie}}</span>` : ''}}
                ${{ch.traditional ? `<span class="pill-sm">Trad: ${{ch.traditional}}</span>` : ''}}
              </div>
            </div>
          </div>
          <div class="decomp-detail-row">
            <strong>Components:</strong> Meaning ${{ch.meaning_component}} · Sound ${{ch.sound_component}}
          </div>
          <div class="decomp-detail-row">
            <strong>Etymology:</strong> ${{ch.etymology_and_mnemonic}}
          </div>
          ${{showEn ? `<div class="mnemonic-story"><strong>Visual Hook (EN):</strong> ${{ch.visual_mnemonic_story_en}}</div>` : ''}}
          ${{showEs ? `<div class="mnemonic-story" style="border-left-color: var(--accent-green);"><strong>Visual Hook (ES):</strong> ${{ch.visual_mnemonic_story_es}}</div>` : ''}}
        </div>
      `).join('');

      // Look alikes HTML
      const lookAlikesHtml = w.traps_and_cognates.look_alikes.map(la => `
        <tr>
          <td class="char-cell" onclick="speak('${{la.character}}')">${{la.character}} <span style="font-size: 0.75rem; cursor: pointer;">🔊</span></td>
          <td style="font-family: 'JetBrains Mono', monospace; color: var(--primary);">${{la.pinyin}}</td>
          <td>${{la.meaning_en}}</td>
          <td style="color: var(--text-muted); font-size: 0.8rem;">${{la.distinction_note}}</td>
        </tr>
      `).join('');

      // Cognates HTML
      const cognatesHtml = w.traps_and_cognates.etymological_cognates.map(cg => `
        <div class="cognate-chip" onclick="speak('${{cg.character}}')">
          <span class="ch">${{cg.character}}</span>
          <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: var(--primary);">${{cg.pinyin}}</span>
          <span style="color: var(--text-dim); font-size: 0.72rem;">${{cg.gloss_en}}</span>
        </div>
      `).join('');

      // Contrasts HTML
      const contrastsHtml = w.semantic_boundary_contrasts.contrasts.map(ct => `
        <div class="contrast-item">
          <div class="contrast-header">
            <span class="contrast-pair">${{ct.compared_word}}</span>
            <span class="contrast-pinyin">${{ct.pinyin}}</span>
          </div>
          <div class="contrast-desc">${{ct.analysis}}</div>
        </div>
      `).join('');

      // Extended Passages HTML
      const passagesHtml = w.extended_reading_passages.map((p, idx) => `
        <div class="passage-block">
          <div class="passage-header">
            <span class="passage-badge">${{idx === 0 ? 'Passage #1: Reflective / Philosophical' : 'Passage #2: Socio-economic / Formal'}}</span>
            <button class="btn btn-icon" onclick="speak('${{p.hanzi}}')">🔊 Read Passage</button>
          </div>
          <div class="passage-hanzi">${{p.hanzi}}</div>
          <div class="passage-pinyin">${{p.pinyin}}</div>
          ${{showEn ? `<div class="passage-trans" style="margin-bottom: 8px;"><strong>EN:</strong> ${{p.en}}</div>` : ''}}
          ${{showEs ? `<div class="passage-trans"><strong>ES:</strong> ${{p.es}}</div>` : ''}}
        </div>
      `).join('');

      container.innerHTML = `
        <!-- Hero Header -->
        <div class="hero-card">
          <div class="hero-top">
            <div class="hero-main">
              <span class="hanzi-hero">${{w.hanzi}}</span>
              <span class="pinyin-hero">${{w.pinyin}}</span>
              <button class="audio-btn" title="Pronounce Word" onclick="speak('${{w.hanzi}}')">🔊</button>
            </div>
            <div class="hero-badges">
              <span class="badge badge-num">NO. ${{String(w.id).padStart(2, '0')}}</span>
              <span class="badge badge-hsk">${{w.level}}</span>
              <span class="badge badge-pos">${{w.part_of_speech}}</span>
            </div>
          </div>
          <div class="hero-summary">
            ${{showEn ? `
              <div class="summary-box">
                <div class="label">English Definition</div>
                <div class="text">${{w.meanings_summary.en}}</div>
              </div>` : ''}}
            ${{showEs ? `
              <div class="summary-box">
                <div class="label">Definición en Español</div>
                <div class="text">${{w.meanings_summary.es}}</div>
              </div>` : ''}}
          </div>
        </div>

        <!-- Senses & Usage -->
        <div class="section-card">
          <div class="section-title">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
            Core Lexical Senses (${{w.senses.length}})
          </div>
          ${{sensesHtml}}
        </div>

        <!-- Example Sentences -->
        <div class="section-card">
          <div class="section-title">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
            Contextual Example Sentences (2)
          </div>
          ${{sentencesHtml}}
        </div>

        <!-- Collocations & Idioms Grid -->
        <div class="grid-2">
          <div class="section-card" style="margin-bottom: 0;">
            <div class="section-title">
              <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              High-Frequency Collocations (6)
            </div>
            <div class="colloc-grid">${{collocHtml}}</div>
          </div>

          <div class="section-card" style="margin-bottom: 0;">
            <div class="section-title">
              <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              Classical Idioms (成语 4)
            </div>
            <div class="colloc-grid">${{idiomsHtml}}</div>
          </div>
        </div>
        <div style="height: 20px;"></div>

        <!-- Character Decomposition -->
        <div class="section-card">
          <div class="section-title">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
            Character Decomposition & Etymology (K=${{w.character_decomposition.length}})
          </div>
          <div class="decomp-grid">${{decompHtml}}</div>
        </div>

        <!-- Mnemonics & Cognitive Roots -->
        <div class="section-card">
          <div class="section-title">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path></svg>
            Memory Hooks & Cultural Foundations
          </div>
          ${{showEn ? `
            <div class="alert-box">
              <div class="alert-title">Composite Memory Hook (EN)</div>
              <div style="font-size: 0.9rem;">${{w.mnemonics_and_roots.composite_memory_hook_en}}</div>
            </div>` : ''}}
          ${{showEs ? `
            <div class="alert-box" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.3);">
              <div class="alert-title" style="color: var(--accent-green);">Gancho Mnemotécnico Compuesto (ES)</div>
              <div style="font-size: 0.9rem;">${{w.mnemonics_and_roots.composite_memory_hook_es}}</div>
            </div>` : ''}}
          <div class="alert-box blue">
            <div class="alert-title">Cultural & Cognitive Metaphor</div>
            <div style="font-size: 0.88rem; line-height: 1.6;">${{w.mnemonics_and_roots.cultural_and_cognitive_roots}}</div>
          </div>
          <div class="alert-box" style="background: rgba(168, 85, 247, 0.08); border-color: rgba(168, 85, 247, 0.3);">
            <div class="alert-title" style="color: var(--accent-purple);">Tone Sandhi & Pitch Contours</div>
            <div style="font-size: 0.88rem; line-height: 1.6;">${{w.mnemonics_and_roots.tone_sandhi_and_pitch_modulation}}</div>
          </div>
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
              <tbody>${{lookAlikesHtml}}</tbody>
            </table>
          </div>

          <div class="section-card" style="margin-bottom: 0;">
            <div class="section-title">
              <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
              Etymological Cognates Family (同族字)
            </div>
            <div class="cognate-chips">${{cognatesHtml}}</div>
          </div>
        </div>
        <div style="height: 20px;"></div>

        <!-- Semantic Contrasts -->
        <div class="section-card">
          <div class="section-title">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
            Semantic Boundary Contrasts (3)
          </div>
          <div style="margin-bottom: 14px; font-size: 0.92rem; color: var(--text);">
            <strong>Core Semantic Nuance:</strong> ${{w.semantic_boundary_contrasts.core_nuance}}
          </div>
          ${{contrastsHtml}}
        </div>

        <!-- Extended Reading Passages -->
        <div class="section-card">
          <div class="section-title">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"></path></svg>
            Extended Reading Passages (2)
          </div>
          ${{passagesHtml}}
        </div>
      `;
    }}

    // Filter logic
    function applyFilters() {{
      const query = document.getElementById('search-input').value.trim().toLowerCase();
      filteredWords = WORDS.filter(w => {{
        const matchesPos = currentPosFilter === 'ALL' || w.part_of_speech.toLowerCase().includes(currentPosFilter.toLowerCase());
        const matchesQuery = !query ||
          w.hanzi.includes(query) ||
          w.pinyin.toLowerCase().includes(query) ||
          w.meanings_summary.en.toLowerCase().includes(query) ||
          w.meanings_summary.es.toLowerCase().includes(query);
        return matchesPos && matchesQuery;
      }});

      renderSidebar();
      if (filteredWords.length > 0 && !filteredWords.some(item => item.id === WORDS[currentIndex].id)) {{
        const newIdx = WORDS.findIndex(item => item.id === filteredWords[0].id);
        selectWord(newIdx);
      }}
    }}

    // Event Listeners
    document.getElementById('search-input').addEventListener('input', applyFilters);

    document.querySelectorAll('.filter-chip').forEach(chip => {{
      chip.addEventListener('click', () => {{
        document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        currentPosFilter = chip.getAttribute('data-pos');
        applyFilters();
      }});
    }});

    document.querySelectorAll('.lang-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentLang = btn.getAttribute('data-lang');
        renderDetail(WORDS[currentIndex]);
        renderSidebar();
      }});
    }});

    document.getElementById('prev-btn').addEventListener('click', () => {{
      if (currentIndex > 0) {{
        selectWord(currentIndex - 1);
      }}
    }});

    document.getElementById('next-btn').addEventListener('click', () => {{
      if (currentIndex < WORDS.length - 1) {{
        selectWord(currentIndex + 1);
      }}
    }});

    document.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'INPUT') return;
      if (e.key === 'ArrowLeft' && currentIndex > 0) {{
        selectWord(currentIndex - 1);
      }} else if (e.key === 'ArrowRight' && currentIndex < WORDS.length - 1) {{
        selectWord(currentIndex + 1);
      }}
    }});

    document.getElementById('toggle-sidebar-btn').addEventListener('click', () => {{
      document.getElementById('sidebar').classList.toggle('open');
    }});

    document.getElementById('theme-btn').addEventListener('click', () => {{
      const isLight = document.body.getAttribute('data-theme') === 'light';
      document.body.setAttribute('data-theme', isLight ? 'dark' : 'light');
    }});

    // Initialize
    selectWord(0);
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated index.html successfully ({len(html_content)} bytes)")
