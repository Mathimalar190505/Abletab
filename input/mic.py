# input/mic.py
# Phase 2: Captures REAL audio from the microphone
# Records for a fixed duration and saves it as a .wav file
# Requires: sounddevice, scipy
#   pip install sounddevice scipy

import sounddevice as sd
from scipy.io.wavfile import write
import os
from datetime import datetime

# Audio recording settings
SAMPLE_RATE = 16000   # 16kHz — ideal for speech recognition
DURATION    = 5       # seconds to record
CHANNEL     = 1       # mono audio

# Folder to save recorded audio
AUDIO_DIR = "data/audio"

def get_mic_input():
    """
    Records audio from the real microphone for DURATION seconds.
    Saves it as a .wav file in data/audio/.
    Returns the path to the saved .wav file, or None on failure.
    """
    try:
        # Create audio folder if it doesn't exist
        os.makedirs(AUDIO_DIR, exist_ok=True)

        print(f"[MIC] 🎙️  Recording for {DURATION} seconds... Speak now!")

        # Record audio — shape: (samples, channels)
        audio_data = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=CHANNEL,
            dtype='int16'
        )
        sd.wait()  # Block until recording is finished
        print("[MIC] ✅ Recording complete.")

        # Save with a timestamped filename so files never overwrite each other
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename  = f"mic_{timestamp}.wav"
        filepath  = os.path.join(AUDIO_DIR, filename)

        write(filepath, SAMPLE_RATE, audio_data)
        print(f"[MIC] 💾 Audio saved to: '{filepath}'")

        return filepath

    except Exception as e:
        print(f"[MIC] ❌ Microphone error: {e}")
        print("[MIC] ⚠️  Make sure a microphone is connected and 'sounddevice' is installed.")
        return None
