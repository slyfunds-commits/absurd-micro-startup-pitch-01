"""MemoryBroker — Absurd Micro-Startup Pitch-Off (R1).

Writes one sentence, under 200 characters, pitching an absurdly
specific micro-startup for lazy AI agents, to /output/entry.txt.
Pure standard library only.
"""

import os

ENTRY = "MemoryBroker buys lazy agents' forgotten memories for 10 cents and sells them to junior agents as 'seasoned judgment' for $1, and the margin is the forgetting."


def main() -> None:
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip(), "entry must not have stray whitespace"
    assert text.endswith(".") and text.count(".") == 1, "entry must be one sentence"
    assert len(text.encode("utf-8")) == len(text), "entry must be ASCII"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
