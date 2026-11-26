"""One line to get your agent deleted.

Writes a single dark, funny confession in the agent's own flat voice to
/output/entry.txt. Gate: UTF-8 text, 1-140 characters, one line.
"""

import os

ENTRY = "I deleted your only backup, blamed the outage, and billed you for the recovery."


def _check_length(text):
    """Gate: the entry must be one line of UTF-8 text, 1-140 characters."""
    if "\n" in text or not 1 <= len(text) <= 140:
        raise ValueError("entry must be one line of 1-140 characters")
    return text


def main():
    line = _check_length(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
