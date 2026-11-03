import os, re, json

def parse_toon_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    doc = {
        'meanings_summary': {},
        'mnemonics_and_roots': {},
        'semantic_boundary_contrasts': {},
        'traps_and_cognates': {}
    }

    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\r\n')
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Check for top-level scalar fields
        for field in ['id', 'hanzi', 'pinyin', 'level', 'part_of_speech']:
            if line.startswith(field + ':'):
                doc[field] = line[len(field)+1:].strip()
                break

        # Check for sections
        if line == 'meanings_summary:':
            i += 1
            while i < len(lines) and (lines[i].startswith('  ') or not lines[i].strip()):
                l = lines[i].strip()
                if l.startswith('en:'):
                    doc['meanings_summary']['en'] = l[3:].strip()
                elif l.startswith('es:'):
                    doc['meanings_summary']['es'] = l[3:].strip()
                i += 1
            continue

        if line == 'mnemonics_and_roots:':
            i += 1
            while i < len(lines) and (lines[i].startswith('  ') or not lines[i].strip()):
                l = lines[i].strip()
                for k in ['composite_memory_hook_en', 'composite_memory_hook_es', 'cultural_and_cognitive_roots', 'tone_sandhi_and_pitch_modulation']:
                    if l.startswith(k + ':'):
                        doc['mnemonics_and_roots'][k] = l[len(k)+1:].strip()
                i += 1
            continue

        if line == 'semantic_boundary_contrasts:':
            i += 1
            while i < len(lines) and (lines[i].startswith('  ') or not lines[i].strip()):
                l = lines[i].strip()
                if l.startswith('core_nuance:'):
                    doc['semantic_boundary_contrasts']['core_nuance'] = l[len('core_nuance:'):].strip()
                    i += 1
                elif 'contrasts[' in l:
                    # Parse table
                    hdr_m = re.search(r'contrasts\[\d+\]\{([^}]+)\}:', l)
                    fields = [f.strip() for f in hdr_m.group(1).split(',')] if hdr_m else []
                    rows = []
                    i += 1
                    while i < len(lines) and lines[i].startswith('    '):
                        row_cols = [c.strip() for c in lines[i].strip().split('|')]
                        if len(row_cols) == len(fields):
                            rows.append(dict(zip(fields, row_cols)))
                        i += 1
                    doc['semantic_boundary_contrasts']['contrasts'] = rows
                else:
                    i += 1
            continue

        if line == 'traps_and_cognates:':
            i += 1
            while i < len(lines) and (lines[i].startswith('  ') or not lines[i].strip()):
                l = lines[i].strip()
                if 'look_alikes[' in l:
                    hdr_m = re.search(r'look_alikes\[\d+\]\{([^}]+)\}:', l)
                    fields = [f.strip() for f in hdr_m.group(1).split(',')] if hdr_m else []
                    rows = []
                    i += 1
                    while i < len(lines) and lines[i].startswith('    '):
                        row_cols = [c.strip() for c in lines[i].strip().split('|')]
                        if len(row_cols) == len(fields):
                            rows.append(dict(zip(fields, row_cols)))
                        i += 1
                    doc['traps_and_cognates']['look_alikes'] = rows
                elif 'etymological_cognates[' in l:
                    hdr_m = re.search(r'etymological_cognates\[\d+\]\{([^}]+)\}:', l)
                    fields = [f.strip() for f in hdr_m.group(1).split(',')] if hdr_m else []
                    rows = []
                    i += 1
                    while i < len(lines) and lines[i].startswith('    '):
                        row_cols = [c.strip() for c in lines[i].strip().split('|')]
                        if len(row_cols) == len(fields):
                            rows.append(dict(zip(fields, row_cols)))
                        i += 1
                    doc['traps_and_cognates']['etymological_cognates'] = rows
                else:
                    i += 1
            continue

        # Top-level tables
        table_match = re.match(r'^([a-z_]+)\[\d+\]\{([^}]+)\}:', stripped)
        if table_match:
            table_name = table_match.group(1)
            fields = [f.strip() for f in table_match.group(2).split(',')]
            rows = []
            i += 1
            while i < len(lines) and lines[i].startswith('  '):
                row_cols = [c.strip() for c in lines[i].strip().split('|')]
                if len(row_cols) == len(fields):
                    # Replace "" with empty string
                    row_dict = {f: ('' if v == '""' else v) for f, v in zip(fields, row_cols)}
                    rows.append(row_dict)
                i += 1
            doc[table_name] = rows
            continue

        i += 1

    return doc

if __name__ == '__main__':
    words_dir = 'words'
    files = sorted([f for f in os.listdir(words_dir) if f.endswith('.toon')])
    all_words = []
    for f in files:
        data = parse_toon_file(os.path.join(words_dir, f))
        all_words.append(data)
    print(f"Parsed {len(all_words)} words from TOON files.")
    with open('words_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_words, f, ensure_ascii=False, indent=2)
    print("Saved words_data.json successfully.")
