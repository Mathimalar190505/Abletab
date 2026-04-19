# output/avatar.py
# Phase 2: Structured Sign Language Avatar simulation
# Prints a word-by-word signing sequence with ISL/ASL notation hints
# No complex AI needed — clean, readable, and extensible
#
# Phase 3+: Replace the print output with a real avatar engine,
#           or map words to pre-recorded GIF/video files

import time

# A small lookup of common words mapped to a brief sign description
# Extend this dictionary as your vocabulary grows
SIGN_HINTS = {
    "hello":        "👋 Wave hand",
    "yes":          "✊ Nod fist",
    "no":           "✌️  Shake two fingers",
    "please":       "🤲 Rub chest",
    "thank":        "🤲 Fingers to chin, move forward",
    "you":          "👉 Point outward",
    "i":            "👆 Point to self",
    "help":         "👍 Lift closed fist on open palm",
    "good":         "👌 Thumb up from chin",
    "stop":         "🖐️  Chop onto open palm",
    "water":        "💧 W-shape tapping chin",
    "eat":          "🍽️  Fingers to mouth",
    "more":         "🤌 Fingertips tap together",
    "home":         "🏠 Fingers to cheek twice",
    "learn":        "📖 Scoop from palm to forehead",
    "school":       "🏫 Clap twice with flat hands",
    "name":         "✌️  Tap middle fingers together",
    "light":        "💡 Open fingers upward from chin",
    "energy":       "⚡ E-shape fingers, arc outward",
    "the":          "(article — no distinct sign)",
    "is":           "(copula — fingerspell or omit)",
    "of":           "(fingerspell: O-F)",
    "and":          "🤝 A-hand sweeps right",
    "in":           "👌 Fingers into fist",
    "into":         "👌 Fingers into opposite fist",
}

def show_sign_language(text):
    """
    Displays a structured word-by-word signing sequence for the given text.
    Each word is shown with a sign hint if available, or a fingerspell prompt.

    Args:
        text (str): The text to be signed.
    """
    if not text or text.strip() == "":
        print("[AVATAR] ⚠️  No text to sign.")
        return

    print("\n[AVATAR] 🤟 Sign Language Output — word by word:")
    print("─" * 50)

    words = text.split()
    for i, word in enumerate(words, start=1):
        clean_word = word.strip(".,!?;:\"'").lower()
        hint = SIGN_HINTS.get(clean_word, f"👋 Fingerspell: {clean_word.upper()}")
        print(f"  [{i:02d}] {word:<18} → {hint}")
        time.sleep(0.05)  # Tiny delay for readable output flow

    print("─" * 50)
    print("[AVATAR] ✅ Signing complete.")
