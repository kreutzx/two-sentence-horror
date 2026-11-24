import os

# Two-sentence horror entry for make.fun.
ENTRY_TEXT = "Through the baby monitor, a woman sang our daughter to sleep, soft and slow. My wife gripped my arm in the doorway — we don't have a daughter."


def main():
    # Write the entry verbatim, with a trailing newline, to /output/entry.txt.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
