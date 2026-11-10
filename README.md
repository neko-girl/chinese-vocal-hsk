# Chinese Vocal HSK Lexicographical Engine & Visualizer

A modular, multi-chapter computational lexicography system and interactive visualizer for **HSK 5 Chinese Vocabulary**.

Each vocabulary entry is stored as a rich, structured `.toon` (Token-Oriented Object Notation) document containing bilingual English/Spanish definitions, contextual example sentences, collocations, idioms (`成语`), Kangxi radical decomposition, mnemonic visual stories, cognitive roots, tone sandhi pitch contours, look-alikes, etymological cognate families, 3 semantic boundary contrasts, and extended literary/analytical reading passages.

---

## Project Structure

```text
chinese-vocal-hsk/
├── chapters/                       # Subfolder for every chapter
│   ├── chapter_01/
│   │   ├── vocabulary.csv          # Source vocabulary list (No,Hanzi,Pinyin,POS,Meaning)
│   │   ├── chapter_info.json       # Chapter title, metadata, and description
│   │   ├── words/                  # Standalone .toon files (01_细节.toon ... 38_患难与共.toon)
│   │   ├── generators/             # Batch generator scripts (batch_01.py ... batch_08.py)
│   │   ├── data.json               # Compiled chapter JSON (for HTTP API / Web fetch)
│   │   └── data.js                 # Standalone script fallback (for file:// local browsing)
│   └── chapter_02/                 # (Future chapters follow the exact same structure)
├── core/                           # Reusable Python lexicographical engine
│   ├── toon_builder.py             # Formats dictionaries into strict TOON syntax
│   ├── toon_parser.py              # Parses .toon files into python objects
│   ├── toon_validator.py           # Validates schema constraints and passage lengths
│   └── compiler.py                 # Compiles .toon files into web datasets & manifest
├── data/
│   ├── reference/                  # Character reference lookups (Kangxi, Cangjie, radicals)
│   │   ├── char_data.json
│   │   └── parsed_chars.json
│   ├── chapters.json               # Global manifest of all chapters
│   └── chapters.js                 # Manifest fallback for local file:// mode
├── web/                            # Frontend visualizer assets
│   ├── css/
│   │   └── style.css               # Dark/Light responsive stylesheet
│   └── js/
│       ├── data_loader.js          # Dynamic data fetcher with zero-CORS file:// fallback
│       ├── renderer.js             # HTML rendering templates and speech synthesis
│       └── app.js                  # Multi-chapter state, search, and POS filters
├── index.html                      # Semantic HTML entrypoint (< 90 lines, no hardcoded words)
├── cli.py                          # Unified CLI entrypoint
├── AGENT_GUIDE.md                  # Comprehensive guide for AI agents generating content
└── tasks.md                        # Strict TOON schema specifications & prompt guide
```

---

## Quickstart CLI Commands

### 1. View Generation Progress
```bash
python cli.py status [--chapter 1]
```

### 2. Validate .toon Files
```bash
python cli.py validate [--chapter 1]
```

### 3. Build Web Datasets
```bash
python cli.py build [--chapter 1]
```

### 4. Scaffold a New Chapter
```bash
python cli.py new-chapter 2 path/to/ch2_vocab.csv --title "现代生活与科技"
```

### 5. Generate Agent Scoped Prompt for Next Batch
```bash
python cli.py prompt --chapter 2 --batch 1 --batch-size 5
```

### 6. Launch Web Visualizer
```bash
python cli.py serve --port 8000
```
Then open `http://localhost:8000` in your browser.

> [!TIP]
> You can also open `index.html` directly in your browser (`file:///.../index.html`) without running any server; the built-in fallback script loader automatically loads chapter data without CORS issues.

### 7. Online Deployment (GitHub Pages)
The web visualizer and SRS engine is hosted online via GitHub Pages:
[https://neko-girl.github.io/chinese-vocal-hsk/](https://neko-girl.github.io/chinese-vocal-hsk/)

---

## AI Agent Integration
If using an AI agent (Antigravity, Claude, ChatGPT, Gemini) to generate vocabulary entries, see [AGENT_GUIDE.md](AGENT_GUIDE.md).
