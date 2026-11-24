"""One Sentence, One Front Page — make.fun entry.

Writes the single front-page headline summing up today's world news
(COP31 collapse, Antalya, 24 Nov 2026) to /output/entry.txt.
"""
import os

ENTRY = "COP31 collapses in Antalya as 194 nations reject a climate pact that never mentions fossil fuels."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
