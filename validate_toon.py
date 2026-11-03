import os, sys, re

def validate_toon_file(filepath):
    errors = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    basename = os.path.basename(filepath)
    m = re.match(r'^(\d{2})_(.+)\.toon$', basename)
    if not m:
        return [f"Filename {basename} does not match format {{No_padded}}_{{Hanzi}}.toon"]
    no_padded, expected_hanzi = m.groups()
    expected_no = str(int(no_padded))

    # Required top level fields
    def get_val(key):
        for l in lines:
            if l.startswith(key + ':'):
                return l[len(key)+1:].strip()
        return None

    id_val = get_val('id')
    if id_val != expected_no and id_val != no_padded:
        errors.append(f"id mismatch: found '{id_val}', expected '{expected_no}' or '{no_padded}'")

    hanzi_val = get_val('hanzi')
    if hanzi_val != expected_hanzi:
        errors.append(f"hanzi mismatch: found '{hanzi_val}', expected '{expected_hanzi}'")

    pinyin_val = get_val('pinyin')
    if not pinyin_val:
        errors.append("Missing pinyin")

    level_val = get_val('level')
    if level_val != 'HSK 5':
        errors.append(f"level mismatch: found '{level_val}', expected 'HSK 5'")

    pos_val = get_val('part_of_speech')
    if not pos_val:
        errors.append("Missing part_of_speech")

    # Table parser helper
    def find_table(header_prefix):
        for i, l in enumerate(lines):
            stripped = l.strip()
            if stripped.startswith(header_prefix) and stripped.endswith(':'):
                # parse count
                count_m = re.search(r'\[(\d+)\]\{([^}]+)\}:', stripped)
                if not count_m:
                    return None, None, None, f"Malformed table header at line {i+1}: {l}"
                count = int(count_m.group(1))
                fields = [f.strip() for f in count_m.group(2).split(',')]
                # collect rows
                rows = []
                base_indent = len(l) - len(l.lstrip())
                for j in range(i+1, len(lines)):
                    rl = lines[j]
                    if not rl.strip():
                        continue
                    r_indent = len(rl) - len(rl.lstrip())
                    if r_indent <= base_indent:
                        break
                    cols = [c.strip() for c in rl.strip().split('|')]
                    rows.append(cols)
                return count, fields, rows, None
        return None, None, None, f"Table {header_prefix} not found"

    # senses
    cnt, flds, rows, err = find_table('senses[')
    if err:
        errors.append(err)
    else:
        if cnt != len(rows):
            errors.append(f"senses count mismatch: header declared [{cnt}], got {len(rows)} rows")
        if len(rows) < 1:
            errors.append("senses has 0 rows")

    # example_sentences[2]
    cnt, flds, rows, err = find_table('example_sentences[')
    if err:
        errors.append(err)
    else:
        if cnt != 2 or len(rows) != 2:
            errors.append(f"example_sentences count mismatch: header [{cnt}], rows {len(rows)} (expected 2)")

    # collocations[6]
    cnt, flds, rows, err = find_table('collocations[')
    if err:
        errors.append(err)
    else:
        if cnt != 6 or len(rows) != 6:
            errors.append(f"collocations count mismatch: header [{cnt}], rows {len(rows)} (expected 6)")

    # idioms[4]
    cnt, flds, rows, err = find_table('idioms[')
    if err:
        errors.append(err)
    else:
        if cnt != 4 or len(rows) != 4:
            errors.append(f"idioms count mismatch: header [{cnt}], rows {len(rows)} (expected 4)")

    # character_decomposition[K]
    # Unique characters count
    unique_chars = []
    for c in expected_hanzi:
        if c not in unique_chars:
            unique_chars.append(c)
    expected_k = len(unique_chars)

    cnt, flds, rows, err = find_table('character_decomposition[')
    if err:
        errors.append(err)
    else:
        if cnt != expected_k or len(rows) != expected_k:
            errors.append(f"character_decomposition count mismatch: header [{cnt}], rows {len(rows)}, expected {expected_k}")
        # verify characters match unique_chars in order
        chars_in_table = [r[0] for r in rows if len(r) > 0]
        if chars_in_table != unique_chars:
            errors.append(f"character_decomposition characters {chars_in_table} do not match unique chars {unique_chars}")

    # look_alikes[L]
    cnt, flds, rows, err = find_table('look_alikes[')
    if err:
        errors.append(err)
    else:
        if not (4 <= cnt <= 6) or cnt != len(rows):
            errors.append(f"look_alikes count mismatch or out of range (4..6): header [{cnt}], rows {len(rows)}")

    # etymological_cognates[C]
    cnt, flds, rows, err = find_table('etymological_cognates[')
    if err:
        errors.append(err)
    else:
        if not (4 <= cnt <= 7) or cnt != len(rows):
            errors.append(f"etymological_cognates count mismatch or out of range (4..7): header [{cnt}], rows {len(rows)}")

    # semantic_boundary_contrasts contrasts[3]
    cnt, flds, rows, err = find_table('contrasts[')
    if err:
        errors.append(err)
    else:
        if cnt != 3 or len(rows) != 3:
            errors.append(f"contrasts count mismatch: header [{cnt}], rows {len(rows)} (expected 3)")

    # extended_reading_passages[2]
    cnt, flds, rows, err = find_table('extended_reading_passages[')
    if err:
        errors.append(err)
    else:
        if cnt != 2 or len(rows) != 2:
            errors.append(f"extended_reading_passages count mismatch: header [{cnt}], rows {len(rows)} (expected 2)")
        else:
            # check passage length
            p1_hanzi = rows[0][1] if len(rows[0]) > 1 else ''
            p2_hanzi = rows[1][1] if len(rows[1]) > 1 else ''
            p1_len = len(re.findall(r'[\u4e00-\u9fff]', p1_hanzi))
            p2_len = len(re.findall(r'[\u4e00-\u9fff]', p2_hanzi))
            if not (40 <= p1_len <= 90):
                errors.append(f"Passage #1 Hanzi length ({p1_len}) deviates from target range (50-80)")
            if not (50 <= p2_len <= 100):
                errors.append(f"Passage #2 Hanzi length ({p2_len}) deviates from target range (60-90)")

    return errors

if __name__ == '__main__':
    words_dir = 'words'
    files = sorted([f for f in os.listdir(words_dir) if f.endswith('.toon')])
    print(f"Found {len(files)} files to validate.")
    all_ok = True
    for f in files:
        errs = validate_toon_file(os.path.join(words_dir, f))
        if errs:
            print(f"[FAIL] {f}:")
            for e in errs:
                print(f"  - {e}")
            all_ok = False
        else:
            print(f"[PASS] {f}")
    if all_ok and len(files) == 38:
        print("\nAll 38 TOON files validated successfully!")
    elif len(files) != 38:
        print(f"\nWarning: Expected 38 files, but found {len(files)}.")
