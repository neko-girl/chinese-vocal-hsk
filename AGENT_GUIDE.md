# AI Agent Generation Guide (HSK TOON Lexicography)

This guide provides instructions for AI agents (such as Antigravity, Claude, ChatGPT, Gemini) tasked with generating vocabulary chapters for this repository.

---

## 1. Overview of the Pipeline

The generation pipeline has 4 main phases:
1. **Scaffold Chapter**: Prepare the chapter subfolder and vocabulary list.
2. **Generate Words in Batches**: Directly create `.toon` files in `chapters/chapter_XX/words/`.
3. **Validate**: Self-correct any schema discrepancies using `python cli.py validate`.
4. **Compile & Build**: Run `python cli.py build` to integrate the chapter into the web visualizer.

---

## 2. Step-by-Step Agent Workflow

### Step 1: Scaffold a New Chapter
If starting a new chapter from a CSV file (columns: `No,Hanzi,Pinyin,Part_of_Speech,Meaning`):
```bash
python cli.py new-chapter <CHAPTER_NUMBER> <PATH_TO_CSV> --title "<CHAPTER_TITLE>"
```
*Example:*
```bash
python cli.py new-chapter 2 source_ch2.csv --title "现代生活与科技 (Modern Life & Technology)"
```
This automatically sets up `chapters/chapter_02/` with `vocabulary.csv`, `chapter_info.json`, and an empty `words/` folder.

---

### Step 2: Check Status & Pending Words
Check how many words have been generated and what remains:
```bash
python cli.py status --chapter <CHAPTER_NUMBER>
```
The status command displays:
- Total words in `vocabulary.csv`
- Number of `.toon` files generated
- Number of validated files
- Exact list of remaining words and recommended batch (e.g., words 1–5, 6–10, etc.)

---

### Step 3: Generating `.toon` Files (Direct Output)

> [!IMPORTANT]
> **Generate `.toon` files directly!**
> Do not generate throwaway Python scripts with nested dictionaries. Generating `.toon` files directly into `chapters/chapter_XX/words/{id_padded}_{hanzi}.toon` is:
> - **40% more token-efficient** (no Python formatting overhead)
> - Free from syntax errors or import issues
> - Directly validated by the test suite

#### Output File Convention:
- Path: `chapters/chapter_{CHAPTER_NUMBER:02d}/words/{No_padded}_{Hanzi}.toon`
- Examples: `chapters/chapter_02/words/01_电脑.toon`, `chapters/chapter_02/words/12_网络.toon`

#### Batch Size Recommendation:
Generate words in batches of **4 to 5 words per agent turn**. Because each word contains deep etymology, bilingual stories, 2 full reading passages (50–90 Hanzi each), and 3 semantic boundary contrasts, generating more than 5 words in a single turn risks output token truncation.

---

## 3. Strict TOON File Schema Reference

Refer to [`tasks.md`](tasks.md) for full lexicographical rules. Every generated `.toon` file must strictly follow this structure:

```toon
id: <No>
hanzi: <Hanzi>
pinyin: <spaced pinyin with tone marks>
level: HSK 5
part_of_speech: <Noun/Verb/Adjective/Adverb/Pronoun/Measure Word/Idiom>

meanings_summary:
  en: <Full English definition>
  es: <Full Spanish definition>

senses[M]{sense_number,part_of_speech,register,definition_en,definition_es,example_phrase}:
  1 | <POS> | <Standard/Colloquial/Formal/Literary> | <EN def> | <ES def> | <Short example phrase>

example_sentences[2]{id,hanzi,pinyin,en,es}:
  #1 | <Daily life context sentence> | <Pinyin> | <EN translation> | <ES translation>
  #2 | <Formal / workplace sentence> | <Pinyin> | <EN translation> | <ES translation>

collocations[6]{hanzi,en}:
  <Collocation 1> | <EN translation>
  <Collocation 2> | <EN translation>
  <Collocation 3> | <EN translation>
  <Collocation 4> | <EN translation>
  <Collocation 5> | <EN translation>
  <Collocation 6> | <EN translation>

idioms[4]{hanzi,pinyin,meaning_en}:
  <Idiom 1> | <spaced pinyin> | <English meaning>
  <Idiom 2> | <spaced pinyin> | <English meaning>
  <Idiom 3> | <spaced pinyin> | <English meaning>
  <Idiom 4> | <spaced pinyin> | <English meaning>

character_decomposition[K]{character,pinyin,meaning_en,meaning_es,radical,radical_meaning_en,meaning_component,sound_component,stroke_count,composition_type,etymology_and_mnemonic,visual_mnemonic_story_en,visual_mnemonic_story_es,tone_mnemonic_anchor,cangjie,traditional}:
  <Char 1> | <pinyin> | <EN> | <ES> | <Radical> | <Radical EN> | <Semantic comp> | <Phonetic comp> | <Strokes> | <Structure> | <Etymology> | <EN visual story> | <ES visual story> | <Tone contour 55/35/214/51> | <CJ or ""> | <Trad or "">

mnemonics_and_roots:
  composite_memory_hook_en: <Single memorable English sentence weaving characters together>
  composite_memory_hook_es: <Single memorable Spanish sentence weaving characters together>
  cultural_and_cognitive_roots: <Cultural origin or cognitive metaphor explanation>
  tone_sandhi_and_pitch_modulation: <Pitch contour guidance, e.g. 51-35, neutral tone tips>

traps_and_cognates:
  look_alikes[L]{character,pinyin,meaning_en,distinction_note}:
    <Look-alike> | <pinyin> | <meaning> | <Radical/stroke distinction>
  etymological_cognates[C]{character,pinyin,gloss_en}:
    <Cognate> | <pinyin> | <meaning gloss>

semantic_boundary_contrasts:
  core_nuance: <Core semantic essence of headword>
  contrasts[3]{id,compared_word,pinyin,analysis}:
    1 | <Headword> vs. <Synonym 1> | <synonym pinyin> | <Detailed comparison of usage, register, object>
    2 | <Headword> vs. <Synonym 2> | <synonym pinyin> | <Detailed comparison of usage, register, object>
    3 | <Headword> vs. <Synonym 3> | <synonym pinyin> | <Detailed comparison of usage, register, object>

extended_reading_passages[2]{id,hanzi,pinyin,en,es}:
  #1 | <Passage 1: 50-80 Hanzi, reflective/literary> | <Pinyin> | <EN> | <ES>
  #2 | <Passage 2: 60-90 Hanzi, journalistic/analytical> | <Pinyin> | <EN> | <ES>
```

#### Exact Table Counts to Obey:
- `example_sentences`: Exactly **2** rows.
- `collocations`: Exactly **6** rows.
- `idioms`: Exactly **4** rows.
- `character_decomposition`: Exactly **K** rows (K = unique characters in headword, in order of appearance).
- `look_alikes`: **4 to 6** rows.
- `etymological_cognates`: **4 to 7** rows.
- `contrasts`: Exactly **3** rows.
- `extended_reading_passages`: Exactly **2** rows (Passage 1: 50–80 Hanzi; Passage 2: 60–90 Hanzi).

---

## 4. Validating and Self-Correcting

After writing files, run:
```bash
python cli.py validate --chapter <CHAPTER_NUMBER>
```

If the validator outputs failures, read the specific line and adjust:
- If a passage is too short or too long, adjust the Chinese text to meet the 50–80 or 60–90 Hanzi limit.
- If a collocation or idiom count is off, verify the declared header count `[N]` matches the actual rows.

---

## 5. Compiling into the Web Visualizer

Once all words for the chapter pass validation:
```bash
python cli.py build --chapter <CHAPTER_NUMBER>
```
This compiles `data.json`, `data.js`, and registers the chapter into `data/chapters.json`.
The visualizer will instantly reflect the new chapter in its dropdown.
