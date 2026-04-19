# output/tts.py
# Text-to-Speech (TTS) output module
# Phase 1: Simulates audio playback by printing to the console
# Phase 2+: Can integrate pyttsx3, gTTS, or ElevenLabs here

def speak(text):
    """
    Simulates speaking the given text aloud.
    Prints a message instead of producing real audio in Phase 1.

    Args:
        text (str): The text to be spoken.
    """
    print("\n[TTS] 🔊 Speaking...")
    print(f'  (Audio) → "{text}"')
    print("[TTS] Done speaking.")
