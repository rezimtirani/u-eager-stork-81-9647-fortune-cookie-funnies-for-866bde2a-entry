"""Fortune Cookie Funnies for Engineers.

The program writes a single fortune-cookie line to the output directory:
a prediction an engineer would actually dread finding inside a cookie.
Nothing else is written. The line is short, deadpan, and lands on one
read: the codebase you are about to inherit is the one you wrote yourself.
"""

import os

FORTUNE = "You will inherit a codebase with no tests and one comment: 'good luck'. It was written by you."


def validate_fortune(text):
    """Refuse to write a fortune the sealed gate would reject.

    The gate wants UTF-8 text of 1 to 140 characters that is not only
    whitespace and holds no line break, so a fortune that breaks any of
    those rules never reaches the output file. Checking here keeps a bad
    line from failing silently at grading time.
    """
    if not isinstance(text, str):
        raise TypeError("fortune must be text")
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    if len(text) > 140:
        raise ValueError("fortune is {} chars, over the 140-char gate".format(len(text)))
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if text != text.strip():
        raise ValueError("fortune must not have leading or trailing space")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    line = validate_fortune(FORTUNE)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote {} ({} chars)".format(target, len(line)))


if __name__ == "__main__":
    main()
