import os

def render_toon(data):
    lines = []
    lines.append(f"id: {data['id']}")
    lines.append(f"hanzi: {data['hanzi']}")
    lines.append(f"pinyin: {data['pinyin']}")
    lines.append("level: HSK 5")
    lines.append(f"part_of_speech: {data['part_of_speech']}")
    lines.append("")
    lines.append("meanings_summary:")
    lines.append(f"  en: {data['meanings_summary']['en']}")
    lines.append(f"  es: {data['meanings_summary']['es']}")
    lines.append("")

    # senses
    senses = data['senses']
    lines.append(f"senses[{len(senses)}]{{sense_number,part_of_speech,register,definition_en,definition_es,example_phrase}}:")
    for s in senses:
        lines.append(f"  {s['sense_number']} | {s['part_of_speech']} | {s['register']} | {s['definition_en']} | {s['definition_es']} | {s['example_phrase']}")
    lines.append("")

    # example_sentences
    sentences = data['example_sentences']
    lines.append(f"example_sentences[{len(sentences)}]{{id,hanzi,pinyin,en,es}}:")
    for s in sentences:
        lines.append(f"  {s['id']} | {s['hanzi']} | {s['pinyin']} | {s['en']} | {s['es']}")
    lines.append("")

    # collocations
    collocations = data['collocations']
    lines.append(f"collocations[{len(collocations)}]{{hanzi,en}}:")
    for c in collocations:
        lines.append(f"  {c['hanzi']} | {c['en']}")
    lines.append("")

    # idioms
    idioms = data['idioms']
    lines.append(f"idioms[{len(idioms)}]{{hanzi,pinyin,meaning_en}}:")
    for im in idioms:
        lines.append(f"  {im['hanzi']} | {im['pinyin']} | {im['meaning_en']}")
    lines.append("")

    # character_decomposition
    decomp = data['character_decomposition']
    lines.append(f"character_decomposition[{len(decomp)}]{{character,pinyin,meaning_en,meaning_es,radical,radical_meaning_en,meaning_component,sound_component,stroke_count,composition_type,etymology_and_mnemonic,visual_mnemonic_story_en,visual_mnemonic_story_es,tone_mnemonic_anchor,cangjie,traditional}}:")
    for ch in decomp:
        trad = ch.get('traditional', '')
        if trad == '' or trad is None:
            trad = '""'
        cangjie = ch.get('cangjie', '')
        if cangjie == '' or cangjie is None:
            cangjie = '""'
        lines.append(f"  {ch['character']} | {ch['pinyin']} | {ch['meaning_en']} | {ch['meaning_es']} | {ch['radical']} | {ch['radical_meaning_en']} | {ch['meaning_component']} | {ch['sound_component']} | {ch['stroke_count']} | {ch['composition_type']} | {ch['etymology_and_mnemonic']} | {ch['visual_mnemonic_story_en']} | {ch['visual_mnemonic_story_es']} | {ch['tone_mnemonic_anchor']} | {cangjie} | {trad}")
    lines.append("")

    # mnemonics_and_roots
    mr = data['mnemonics_and_roots']
    lines.append("mnemonics_and_roots:")
    lines.append(f"  composite_memory_hook_en: {mr['composite_memory_hook_en']}")
    lines.append(f"  composite_memory_hook_es: {mr['composite_memory_hook_es']}")
    lines.append(f"  cultural_and_cognitive_roots: {mr['cultural_and_cognitive_roots']}")
    lines.append(f"  tone_sandhi_and_pitch_modulation: {mr['tone_sandhi_and_pitch_modulation']}")
    lines.append("")

    # traps_and_cognates
    tc = data['traps_and_cognates']
    lines.append("traps_and_cognates:")
    look_alikes = tc['look_alikes']
    lines.append(f"  look_alikes[{len(look_alikes)}]{{character,pinyin,meaning_en,distinction_note}}:")
    for la in look_alikes:
        lines.append(f"    {la['character']} | {la['pinyin']} | {la['meaning_en']} | {la['distinction_note']}")
    cognates = tc['etymological_cognates']
    lines.append(f"  etymological_cognates[{len(cognates)}]{{character,pinyin,gloss_en}}:")
    for cg in cognates:
        gloss = cg.get('gloss_en') or cg.get('meaning_en', '')
        lines.append(f"    {cg['character']} | {cg['pinyin']} | {gloss}")
    lines.append("")

    # semantic_boundary_contrasts
    sbc = data['semantic_boundary_contrasts']
    lines.append("semantic_boundary_contrasts:")
    lines.append(f"  core_nuance: {sbc['core_nuance']}")
    contrasts = sbc['contrasts']
    lines.append(f"  contrasts[{len(contrasts)}]{{id,compared_word,pinyin,analysis}}:")
    for ct in contrasts:
        lines.append(f"    {ct['id']} | {ct['compared_word']} | {ct['pinyin']} | {ct['analysis']}")
    lines.append("")

    # extended_reading_passages
    passages = data['extended_reading_passages']
    lines.append(f"extended_reading_passages[{len(passages)}]{{id,hanzi,pinyin,en,es}}:")
    for p in passages:
        lines.append(f"  {p['id']} | {p['hanzi']} | {p['pinyin']} | {p['en']} | {p['es']}")

    return "\n".join(lines) + "\n"

def save_word(data):
    no_padded = f"{int(data['id']):02d}"
    filename = f"{no_padded}_{data['hanzi']}.toon"
    filepath = os.path.join("words", filename)
    content = render_toon(data)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {filepath}")
