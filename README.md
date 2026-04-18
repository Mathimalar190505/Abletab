# AbleTab

AbleTab is an assistive learning device designed to help both blind and deaf students access classroom content in real-time.

---

## 🚀 Features

- 🎤 Speech to Text (Captions for deaf students)
- 📷 OCR (Extract text from board/images)
- ⠿ Braille Output (for blind students)
- 🧍 Sign Language Avatar (for deaf students)
- 🔊 Text to Speech (audio output)
- 💾 Session-based Storage & Review system

---

## 🧠 System Architecture

Input → Processing → Output → Storage

### Inputs:
- Microphone (Speech input)
- ESP32 Camera (Image capture)

### Processing:
- Speech-to-Text
- OCR
- Text Processing

### Outputs:
- Braille Strip
- TFT Display (Captions + Avatar)
- Speaker (Audio)

---

## 🔄 Working Flow

1. Capture speech and image
2. Convert to text using STT and OCR
3. Process text
4. Output:
   - Braille (for blind)
   - Caption + Avatar (for deaf)
   - Audio output
5. Store session data

---

## 📁 Project Structure
