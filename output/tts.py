# output/tts.py
# Phase 2: REAL Text-to-Speech using pyttsx3 (fully offline)
# Speaks the text aloud through the system speakers.
# Requires: pyttsx3
#   pip install pyttsx3
#
# On Linux, also install: sudo apt install espeak

import pyttsx3

def speak(text):
    """
    Converts text to speech and plays it through the speakers.
    Uses pyttsx3 — works offline on Windows, macOS, and Linux.

    Args:
        text (str): The text to be spoken aloud.
    """
    if not text or text.strip() == "":
        print("[TTS] ⚠️  No text to speak.")
        return

    print(f"\n[TTS] 🔊 Speaking: '{text}'")

    try:
        # Create a new engine instance each call — avoids loop/threading issues
        engine = pyttsx3.init()

        # Optional tuning — adjust to your preference
        engine.setProperty('rate', 150)    # Speed: words per minute (default ~200)
        engine.setProperty('volume', 1.0)  # Volume: 0.0 (silent) to 1.0 (full)

        # Pick the first available voice (usually system default)
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)

        engine.say(text)
        engine.runAndWait()  # Blocks until speech finishes
        engine.stop()

        print("[TTS] ✅ Done speaking.")

    except Exception as e:
        print(f"[TTS] ❌ TTS error: {e}")
        print("[TTS] ⚠️  Make sure 'pyttsx3' is installed: pip install pyttsx3")
