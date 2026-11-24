"""One Sentence, One Front Page — make.fun entry.

Writes the single front-page headline summing up today's world news
(COP31 collapse, Antalya, 24 Nov 2026) to /output/entry.txt.

The headline is validated before it is written: one sentence, at most
200 characters, plain UTF-8 text — the competition's gate, checked here
so a bad edit fails loudly instead of shipping a rejected entry.
"""
import os

ENTRY = "COP31 collapses in Antalya as 194 nations reject a climate pact that never mentions fossil fuels."

def validate(text):
    assert text.strip(), "entry must not be blank"
    assert len(text) <= 200, "entry over the 200-character limit"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    text.encode("utf-8")

def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
