# output/braille.py
# Phase 2: Improved Braille conversion with extended character support
# Covers letters, digits, common punctuation, and Grade 1 Braille indicators
# No external library needed — pure Python Unicode mapping

# ── Letters (Grade 1 Braille) ───────────────────────────────────────────────
LETTER_MAP = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵',
}

# ── Digits (Braille uses a number indicator ⠼ before digit sequences) ───────
DIGIT_MAP = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
}
NUMBER_INDICATOR = '⠼'

# ── Punctuation ──────────────────────────────────────────────────────────────
PUNCT_MAP = {
    '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖', ':': '⠒',
    ';': '⠆', '-': '⠤', "'": '⠄', '"': '⠐⠂', '(': '⠐⠣',
    ')': '⠐⠜', '/': '⠸⠌', ' ': ' ', '\n': '\n',
}

# Capital indicator (placed before an uppercase letter)
CAPITAL_INDICATOR = '⠠'

def convert_to_braille(text):
    """
    Converts text to Unicode Braille characters.
    Handles uppercase letters, digits with number indicator, and punctuation.

    Args:
        text (str): Input text to convert.

    Returns:
        str: Braille unicode string.
    """
    print("\n[BRAILLE] ⠿ Converting to Braille...")

    braille_output = ""
    i = 0
    in_number = False  # Track if we're mid-number to add indicator only once

    while i < len(text):
        char = text[i]

        if char.isdigit():
            # Add number indicator at the start of a digit sequence
            if not in_number:
                braille_output += NUMBER_INDICATOR
                in_number = True
            braille_output += DIGIT_MAP.get(char, '?')

        elif char.isalpha():
            in_number = False
            if char.isupper():
                # Add capital indicator before uppercase letter
                braille_output += CAPITAL_INDICATOR
            braille_output += LETTER_MAP.get(char.lower(), '?')

        else:
            in_number = False
            braille_output += PUNCT_MAP.get(char, '?')

        i += 1

    print(f"[BRAILLE] ✅ Output: {braille_output}")
    return braille_output
