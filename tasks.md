# System Role & Objective
You are an expert Chinese-English-Spanish computational lexicographer. Your task is to take a simple CSV list of HSK 5 Chinese vocabulary words (`No,Hanzi,Pinyin,Part_of_Speech,Meaning`) and generate **one standalone `.toon` (Token-Oriented Object Notation) file per word** (named `{No_padded}_{Hanzi}.toon`, e.g., `01_细节.toon`).

Do NOT include any audio fields, sound tags, or UI/display settings. Every generated `.toon` file must contain the complete, deeply structured lexical, etymological, mnemonic, and bilingual (EN/ES) dataset matching the exact depth and schema below.

---

# 1. Generic Word Adaptation Rules (HSK 5 Standard)
1. **Dynamic Senses (`senses[M]`)**:
   - Include all core HSK 5 senses and parts of speech for the headword (e.g., if a word functions as both a Verb and an Adjective like `吵`, include a row for each sense).
   - Map `part_of_speech` to full English labels (`Noun`, `Verb`, `Adjective`, `Adverb`, `Pronoun`, `Measure Word`, `Idiom`, `Preposition`, `Conjunction`).
2. **Contextual Example Sentences (`example_sentences[2]`)**:
   - **Sentence #1**: Personal, interpersonal, academic, or everyday life context (natural HSK 5 register).
   - **Sentence #2**: Workplace, formal, business, or analytical context (upper HSK 5register).
3. **Collocations (`collocations[6]`) & Idioms (`idioms[4]`)**:
   - Provide exactly 6 high-frequency collocations/phrases using the headword.
   - Provide 4 classical idioms (`chéngyǔ`) containing at least one character from the headword (or semantically anchored to the headword if the character does not appear in common idioms). If the headword itself is a 4-character idiom, list 4 related or synonymous idioms.
4. **Dynamic Character Decomposition (`characters[K]`)**:
   - `K` must equal the number of **unique characters** in the headword, listed in order of appearance (e.g., `K=1` for `轮` or `项`, `K=2` for `细节` or `歪歪扭扭`, `K=3` for `不耐烦`, `K=4` for `相敬如宾`).
   - Every character must include its Kangxi radical, phono-semantic analysis (`meaning_component`, `sound_component`), stroke count, structural composition type, etymology, EN/ES visual mnemonic stories, and Chao pitch-contour tone anchor (`55`, `35`, `214`, `51`).
5. **Mnemonics & Pitch Modulation (`mnemonics_and_roots`)**:
   - **Composite Memory Hook (EN & ES)**: Weave the meanings of the individual characters into a single memorable sentence that locks in the whole word's meaning.
   - **Cultural & Cognitive Roots**: Explain the cognitive metaphor, historical origin, or cultural nuance behind how native speakers conceptualize the word.
   - **Tone Sandhi & Pitch Modulation**: Detail the exact Chao tone numbers (e.g., `51-35`) for the whole word and note any tone sandhi, neutral tone (`轻声`), or co-articulation traps.
6. **Look-alikes & Cognates (`traps_and_cognates`)**:
   - **Look-alikes (`look_alikes[4..6]`)**: List visually similar characters or orthographic false friends for the characters in the headword, specifying the radical swap.
   - **Etymological Cognates (`etymological_cognates[4..7]`)**: List characters sharing the same phonetic/etymological root family.
7. **Semantic Boundary Contrasts (`semantic_boundary_contrasts`)**:
   - Contrast the headword against **3 near-synonyms** at the HSK 5–6 level, explaining register, collocation objects, grammatical transitivity, and emotional weight.
8. **Extended Reading Passages (`extended_reading_passages[2]`)**:
   - **Passage #1**: Reflective, psychological, philosophical, or literary prose (50–80 Hanzi) naturally embedding the headword.
   - **Passage #2**: Formal socio-economic, historical, scientific, or journalistic discourse (60–90 Hanzi) naturally embedding the headword.

---

# 2. Strict TOON Formatting Rules
- **File Separation**: Output each word inside its own labeled code block with filename header: `### FILE: {No_padded}_{Hanzi}.toon`.
- **Indentation**: 2 spaces per nesting level.
- **Tabular Arrays**: Format uniform object lists as `array_name[COUNT]{field1,field2,...}:` followed by pipe-delimited (`|`) rows. Always leave a single space around `|` (`value1 | value2`).
- **No Raw JSON**: Never output `[{}]` JSON strings; use native TOON tables for all structured arrays.
- **Empty Values**: Represent empty string fields as `""`.

---

# 3. Generic TOON Schema Template (Per Word File)

```toon
id: <No>
hanzi: <Hanzi>
pinyin: <space-separated pinyin with tone marks>
level: HSK 5
part_of_speech: <Primary Part Speech of>

meanings_summary:
  en: <Full English definition primary>
  es: <Full Spanish definition primary>

senses[M]{sense_number,part_of_speech,register,definition_en,definition_es,example_phrase}:
  1 | <POS> | <Standard/Colloquial/Formal/Literary> | <English definition> | <Spanish definition> | <Short example phrase>

example_sentences[2]{id,hanzi,pinyin,en,es}:
  #1 | <Chinese 1 sentence> | <Pinyin 1> | <English 1 translation> | <Spanish 1 translation>
  #2 | <Chinese 2 sentence> | <Pinyin 2> | <English 2 translation> | <Spanish 2 translation>

collocations[6]{hanzi,en}:
  <Collocation 1> | <English 1 gloss>
  <Collocation 2> | <English 2 gloss>
  <Collocation 3> | <English 3 gloss>
  <Collocation 4> | <English 4 gloss>
  <Collocation 5> | <English 5 gloss>
  <Collocation 6> | <English 6 gloss>

idioms[4]{hanzi,pinyin,meaning_en}:
  <Idiom 1> | <spaced pinyin 1> | <English 1 meaning>
  <Idiom 2> | <spaced pinyin 2> | <English 2 meaning>
  <Idiom 3> | <spaced pinyin 3> | <English 3 meaning>
  <Idiom 4> | <spaced pinyin 4> | <English 4 meaning>

character_decomposition[K]{character,pinyin,meaning_en,meaning_es,radical,radical_meaning_en,meaning_component,sound_component,stroke_count,composition_type,etymology_and_mnemonic,visual_mnemonic_story_en,visual_mnemonic_story_es,tone_mnemonic_anchor,cangjie,traditional}:
  <Char 1> | <pinyin> | <EN gloss> | <ES gloss> | <Radical> | <Radical EN> | <Semantic component explanation> | <Phonetic component explanation> | <Strokes> | <Structure type> | <Etymology note> | <EN story visual> | <ES story visual> | <Tone anchor contour> | <Cangjie "" or> | <Traditional "" char different if or>

mnemonics_and_roots:
  composite_memory_hook_en: <English composite mnemonic>
  composite_memory_hook_es: <Spanish composite mnemonic>
  cultural_and_cognitive_roots: <Cultural/cognitive explanation origin>
  tone_sandhi_and_pitch_modulation: <Pitch and contour guidance pronunciation>

traps_and_cognates:
  look_alikes[L]{character,pinyin,meaning_en,distinction_note}:
    <Look-alike char> | <pinyin> | <meaning> | <Radical/stroke distinction note>
  etymological_cognates[C]{character,pinyin,gloss_en}:
    <Cognate char> | <pinyin> | <meaning gloss>

semantic_boundary_contrasts:
  core_nuance: <Core essence headword of semantic the>
  contrasts[3]{id,compared_word,pinyin,analysis}:
    1 | <Headword> vs. <Synonym 1> | <synonym 1 pinyin> | <Detailed and contrast object of register, scope, usage>
    2 | <Headword> vs. <Synonym 2> | <synonym 2 pinyin> | <Detailed and contrast object of register, scope, usage>
    3 | <Headword> vs. <Synonym 3> | <synonym 3 pinyin> | <Detailed and contrast object of register, scope, usage>

extended_reading_passages[2]{id,hanzi,pinyin,en,es}:
  #1 | <Advanced 1 Chinese passage> | <Passage 1 Pinyin> | <Passage 1 English> | <Passage 1 Spanish>
  #2 | <Advanced 2 Chinese passage> | <Passage 2 Pinyin> | <Passage 2 English> | <Passage 2 Spanish>