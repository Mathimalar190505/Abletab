# processing/stt.py
# Speech-to-Text (STT) processing module
# Phase 1: Returns the input text as-is (no real ASR engine yet)
# Phase 2+: Can integrate Google STT, Whisper, or Vosk here

def speech_to_text(audio_text):
    """
    Simulates converting speech (audio) to text.
    In Phase 1, the mic already returns text, so we pass it through directly.

    Args:
        audio_text (str): The raw text captured from the mic simulation.

    Returns:
        str: The processed text (same as input in simulation).
    """
    print(f"[STT] Converting speech to text...")
    processed_text = audio_text  # No transformation in simulation
    print(f"[STT] Result: '{processed_text}'")
    return processed_text
