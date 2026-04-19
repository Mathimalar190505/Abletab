# processing/stt.py
# Phase 2: REAL Speech-to-Text using SpeechRecognition + Google Web Speech API
# Falls back gracefully if recognition fails.
# Requires: SpeechRecognition
#   pip install SpeechRecognition
#
# NOTE: For a fully OFFLINE solution, replace the recognizer call below with:
#   import whisper
#   model = whisper.load_model("base")
#   result = model.transcribe(audio_file_path)
#   return result["text"]
# And install with: pip install openai-whisper

import speech_recognition as sr

def speech_to_text(audio_file_path):
    """
    Converts a .wav audio file to text using the SpeechRecognition library.
    Uses Google Web Speech API (free, requires internet).

    Args:
        audio_file_path (str): Path to the recorded .wav file from mic.py

    Returns:
        str: Transcribed text, or an empty string on failure.
    """
    # If mic.py failed and returned None, handle gracefully
    if not audio_file_path:
        print("[STT] ⚠️  No audio file provided. Skipping speech-to-text.")
        return ""

    print(f"[STT] 🔄 Transcribing audio: '{audio_file_path}'...")

    recognizer = sr.Recognizer()

    try:
        # Load the saved .wav file
        with sr.AudioFile(audio_file_path) as source:
            # Adjust for ambient noise, then record from file
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = recognizer.record(source)

        # Send to Google Web Speech API for transcription
        text = recognizer.recognize_google(audio_data)
        print(f"[STT] ✅ Transcription: '{text}'")
        return text

    except sr.UnknownValueError:
        print("[STT] ⚠️  Could not understand the audio. Was anything spoken?")
        return ""

    except sr.RequestError as e:
        print(f"[STT] ❌ API request failed: {e}")
        print("[STT] ⚠️  Check your internet connection, or switch to offline Whisper.")
        return ""

    except Exception as e:
        print(f"[STT] ❌ Unexpected STT error: {e}")
        return ""
