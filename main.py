#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — one short rant writer.

Writes a single original rant (1-400 characters) about a small everyday
annoyance to /output/entry.txt. The rant is a self-contained piece of text:
a shopper, a self-checkout machine, and an accusation nobody deserved.
"""
import os

RANT = (
    "The self-checkout screamed UNEXPECTED ITEM IN THE BAGGING AREA at rice "
    "I had already scanned, weighed and apologised to. I stood there, hands "
    "up like a suspect, while a teenager in a vest strolled over, pressed "
    "one button and fixed in three seconds what the machine spent two "
    "minutes accusing me of. I didn't steal anything. I just wanted rice. "
    "The machine wanted a confession."
)


def main():
    # Exactly one text: no trailing newline, no extra whitespace.
    text = RANT.strip()
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
