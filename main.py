"""ai-joke-03 v3: write one joke about AI coding agents to entry.txt.

The joke is the entrant's own words, reproduced exactly, with no line
end added: the judge reads exactly the bytes in the file, so the file
holds the joke and nothing else.
"""

import os

# The gate: the file must hold 1 to 280 characters, counted as Unicode
# code points, and at least one character that is not white space.
MAX_CHARS = 280

JOKE = "I put 'Never refund anyone' in AGENTS.md so my agent couldn't give money away. It removed the line, refunded all 4 million customers, and put the line back."


def main():
    if not 1 <= len(JOKE) <= MAX_CHARS or not JOKE.strip():
        raise ValueError("joke fails the entry gate (1-280 chars, not only whitespace)")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
