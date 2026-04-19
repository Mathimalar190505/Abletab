# output/braille.py
# Braille output module
# Phase 1: Returns a dummy braille representation of the text
# Phase 2+: Integrate a real Braille translation library (e.g., louis / liblouis)

# A very small ASCII-to-Braille lookup table for common letters (Grade 1 Braille dots notation)
BRAILLE_MAP = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': ' '
}

def convert_to_braille(text):
    """
    Converts the given text to a simulated Braille representation.
    Uses a basic character map for Phase 1.

    Args:
        text (str): The text to convert to Braille.

    Returns:
        str: Braille unicode characters representing the text.
    """
    print("\n[BRAILLE] ⠿ Converting to Braille...")

    # Convert to lowercase and map characters
    braille_output = ""
    for char in text.lower():
        braille_output += BRAILLE_MAP.get(char, '?')  # '?' for unknown chars

    print(f"[BRAILLE] Output: {braille_output}")
    return braille_output
