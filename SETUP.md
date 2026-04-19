# AbleTab Phase 2 — Setup Guide
================================================

## STEP 1 — Install Python libraries

Open a terminal inside the AbleTab/ folder and run:

    pip install -r requirements.txt

Or install one by one:

    pip install sounddevice scipy
    pip install opencv-python
    pip install SpeechRecognition
    pip install pytesseract Pillow
    pip install pyttsx3


## STEP 2 — Install Tesseract OCR (for Windows)

1. Download the installer from:
   https://github.com/UB-Mannheim/tesseract/wiki

2. Run the installer (default path: C:\Program Files\Tesseract-OCR\)

3. Open processing/ocr.py and confirm this line matches your install:
   TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Linux users:   sudo apt install tesseract-ocr
macOS users:   brew install tesseract
   (On Linux/macOS, set TESSERACT_PATH = None in ocr.py)


## STEP 3 — Run the system

    python main.py

When prompted, type one of:
    blind   →  Braille + Audio output
    deaf    →  Captions + Sign language avatar
    both    →  All outputs enabled


## WHAT HAPPENS WHEN YOU RUN IT

1. [MIC]      Records 5 seconds of audio from your microphone
2. [CAMERA]   Captures a photo from your webcam
3. [STT]      Transcribes your speech to text (needs internet)
4. [OCR]      Reads text from the captured image
5. [OUTPUT]   Speaks / shows captions / braille / avatar based on mode
6. [STORAGE]  Saves transcript + audio to data/sessions/


## FOLDER STRUCTURE AFTER RUNNING

AbleTab/
├── data/
│   ├── audio/           ← Recorded .wav files
│   ├── images/          ← Captured webcam images
│   ├── sessions/        ← Per-session folders (transcript + audio)
│   └── notes.txt        ← Quick flat log of all sessions


## OFFLINE SPEECH-TO-TEXT (optional)

If you want to work without internet, replace SpeechRecognition with Whisper:

    pip install openai-whisper

Then in processing/stt.py, replace the function body with:

    import whisper
    model = whisper.load_model("base")  # Downloads ~150MB model once
    result = model.transcribe(audio_file_path)
    return result["text"]


## TROUBLESHOOTING

| Problem                         | Fix                                              |
|---------------------------------|--------------------------------------------------|
| Mic not recording               | Check sounddevice: python -c "import sounddevice"|
| Webcam not found                | Change 0 → 1 in cv2.VideoCapture(0) in camera.py|
| Tesseract not found             | Set TESSERACT_PATH correctly in ocr.py           |
| STT returns nothing             | Check internet; speak clearly during 5s window  |
| pyttsx3 no audio on Linux       | sudo apt install espeak                          |
