"""The Vacuum's Alibi — one line, at most 200 characters.

The excuse a robot vacuum gives for missing a spot, written by the
machine itself: deadpan, a little smug about its sensors, with a
surprising detail and the punch at the end.

Pure Python standard library. Deterministic: the same bytes on
every run.
"""

import os

LINE = (
    "I didn't miss that spot. My lidar classified your sock as a "
    "hibernating animal, and my battery has a strict no-wake policy."
)


def validate(text: str) -> str:
    """Enforce the competition gate.

    The entry must be 1 to 200 Unicode code points, a single line,
    and not blank or whitespace-only.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(text)}"
        )
    return text


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    line = validate(LINE)
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    with open(path, "r", encoding="utf-8") as handle:
        landed = handle.read()
    landed_line = landed.rstrip("\n")
    validate(landed_line)
    if landed_line != line:
        raise ValueError("bytes on disk do not match the entry")
    print(landed_line)
    print(f"characters: {len(landed_line)}")


if __name__ == "__main__":
    main()
