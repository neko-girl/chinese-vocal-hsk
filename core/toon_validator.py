import os
import re

def validate_toon_file(filepath: str) -> list[str]:
    """Validates a single .toon file against strict HSK 5 schema rules.
    
    Returns a list of error descriptions (empty list if valid).
    """
    errors = []
    if not os.path.exists(filepath):
        return [f"File not found: {filepath}"]

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    basename = os.path.basename(filepath)
    m = re.match(r'^(\d{2})_(.+)\.toon$', basename)
    if not m:
        return [f"Filename '{basename}' does not match format {{No_padded}}_{{Hanzi}}.toon (e.g. 01_细节.toon)"]
    no_padded, expected_hanzi = m.groups()
    expected_no = str(int(no_padded))

    # Required top level scalar fields
    def get_val(key):
        for l in lines:
            if l.startswith(key + ':'):
                return l[len(key) + 1:].strip()
        return None

    id_val = get_val('id')
    if id_val != expected_no and id_val != no_padded:
        errors.append(f"id mismatch: found '{id_val}', expected '{expected_no}' or '{no_padded}'")

    hanzi_val = get_val('hanzi')
    if hanzi_val != expected_hanzi:
        errors.append(f"hanzi mismatch: found '{hanzi_val}', expected '{expected_hanzi}'")

    pinyin_val = get_val('pinyin')
    if not pinyin_val:
        errors.append("Missing 'pinyin' field")

    level_val = get_val('level')
    if level_val != 'HSK 5':
        errors.append(f"level mismatch: found '{level_val}', expected 'HSK 5'")

    pos_val = get_val('part_of_speech')
    if not pos_val:
        errors.append("Missing 'part_of_speech' field")

    # Table parser helper
    def find_table(header_prefix):
        for i, l in enumerate(lines):
            stripped = l.strip()
            if stripped.startswith(header_prefix) and stripped.endswith(':'):
                count_m = re.search(r'\[(\d+)\]\{([^}]+)\}:', stripped)
                if not count_m:
                    return None, None, None, f"Malformed table header at line {i+1}: {l}"
                count = int(count_m.group(1))
                fields = [f.strip() for f in count_m.group(2).split(',')]
                rows = []
                base_indent = len(l) - len(l.lstrip())
                for j in range(i + 1, len(lines)):
                    rl = lines[j]
                    if not rl.strip():
                        continue
                    r_indent = len(rl) - len(rl.lstrip())
                    if r_indent <= base_indent:
                        break
                    cols = [c.strip() for c in rl.strip().split('|')]
                    rows.append(cols)
                return count, fields, rows, None
        return None, None, None, f"Table '{header_prefix}' not found"

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
            errors.append(f"example_sentences count mismatch: header [{cnt}], rows {len(rows)} (expected exactly 2)")

    # collocations[6]
    cnt, flds, rows, err = find_table('collocations[')
    if err:
        errors.append(err)
    else:
        if cnt != 6 or len(rows) != 6:
            errors.append(f"collocations count mismatch: header [{cnt}], rows {len(rows)} (expected exactly 6)")

    # idioms[4]
    cnt, flds, rows, err = find_table('idioms[')
    if err:
        errors.append(err)
    else:
        if cnt != 4 or len(rows) != 4:
            errors.append(f"idioms count mismatch: header [{cnt}], rows {len(rows)} (expected exactly 4)")

    # character_decomposition[K]
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
            errors.append(f"contrasts count mismatch: header [{cnt}], rows {len(rows)} (expected exactly 3)")

    # extended_reading_passages[2]
    cnt, flds, rows, err = find_table('extended_reading_passages[')
    if err:
        errors.append(err)
    else:
        if cnt != 2 or len(rows) != 2:
            errors.append(f"extended_reading_passages count mismatch: header [{cnt}], rows {len(rows)} (expected exactly 2)")
        else:
            p1_hanzi = rows[0][1] if len(rows[0]) > 1 else ''
            p2_hanzi = rows[1][1] if len(rows[1]) > 1 else ''
            p1_len = len(re.findall(r'[\u4e00-\u9fff]', p1_hanzi))
            p2_len = len(re.findall(r'[\u4e00-\u9fff]', p2_hanzi))
            if not (40 <= p1_len <= 95):
                errors.append(f"Passage #1 Hanzi length ({p1_len}) deviates from target range (50-80)")
            if not (45 <= p2_len <= 105):
                errors.append(f"Passage #2 Hanzi length ({p2_len}) deviates from target range (60-90)")

    return errors

def validate_chapter(chapter_dir: str) -> tuple[bool, dict[str, list[str]]]:
    """Validates all .toon files in chapter_dir/words/.
    
    Returns:
        (is_valid: bool, results: dict[filename, list[errors]])
    """
    words_dir = os.path.join(chapter_dir, 'words')
    if not os.path.exists(words_dir):
        return False, {"_chapter": [f"Words directory does not exist: {words_dir}"]}

    def sort_key(name):
        m = re.match(r'^(\d+)_', name)
        return int(m.group(1)) if m else 999999

    files = sorted([f for f in os.listdir(words_dir) if f.endswith('.toon')], key=sort_key)
    if not files:
        return False, {"_chapter": ["No .toon files found in words directory"]}

    results = {}
    all_ok = True

    for f in files:
        filepath = os.path.join(words_dir, f)
        errs = validate_toon_file(filepath)
        results[f] = errs
        if errs:
            all_ok = False

    # Check against vocabulary.csv if present
    vocab_file = os.path.join(chapter_dir, 'vocabulary.csv')
    if os.path.exists(vocab_file):
        with open(vocab_file, 'r', encoding='utf-8') as vf:
            lines = [l.strip() for l in vf if l.strip()]
        header = lines[0] if lines else ''
        expected_count = len(lines) - 1 if len(lines) > 1 else 0
        if len(files) != expected_count:
            all_ok = False
            results["_vocab_count"] = [
                f"File count mismatch: found {len(files)} .toon files, but vocabulary.csv has {expected_count} words"
            ]

    return all_ok, results
