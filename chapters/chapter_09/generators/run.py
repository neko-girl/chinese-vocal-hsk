import os
import sys

# Ensure repository root is in python path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from core.toon_builder import save_word

def run_all_batches(target_dir: str = None):
    if target_dir is None:
        target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../words"))

    os.makedirs(target_dir, exist_ok=True)
    curr_dir = os.path.dirname(__file__)
    if curr_dir not in sys.path:
        sys.path.insert(0, curr_dir)

    total_saved = 0
    for i in range(1, 5):
        mod_name = f"batch_{i:02d}"
        try:
            mod = __import__(mod_name)
            words_list = getattr(mod, f"words_batch{i}", None)
            if words_list:
                for w in words_list:
                    save_word(w, target_dir=target_dir)
                    total_saved += 1
                print(f"[{mod_name}] Processed {len(words_list)} words.")
            else:
                print(f"[{mod_name}] Warning: words_batch{i} not found.")
        except Exception as e:
            print(f"[{mod_name}] Error running batch: {e}")

    print(f"\nSuccessfully generated {total_saved} words in {target_dir}")

if __name__ == '__main__':
    run_all_batches()
