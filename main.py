import os

LINE = (
    "The babysitter texted that the baby had finally stopped crying at "
    "3 a.m. I was still driving home, and my daughter was asleep in the "
    "back seat."
)


def main():
    # Exactly two sentences; the gate allows at most 400 characters; this story is 143.
    assert 1 <= len(LINE.strip()) <= 400, len(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
