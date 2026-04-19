# processing/ocr.py
# Phase 2: REAL OCR using Tesseract via pytesseract
# Extracts text from an image file captured by the webcam.
# Requires: pytesseract, Pillow
#   pip install pytesseract Pillow
#
# Also requires Tesseract OCR engine installed on your system:
#   Windows: https://github.com/UB-Mannheim/tesseract/wiki
#     → Install, then set TESSERACT_PATH below to your install path
#   Linux:   sudo apt install tesseract-ocr
#   macOS:   brew install tesseract

import pytesseract
from PIL import Image
import os

# ── Windows users: set this to your Tesseract install path ──────────────────
# Example: r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Leave as None on Linux/macOS (it's found automatically)
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_image(image_path):
    """
    Runs Tesseract OCR on the given image file and returns extracted text.

    Args:
        image_path (str): Path to the image file from camera.py

    Returns:
        str: Extracted text string, or empty string on failure.
    """
    # If camera.py failed and returned None, handle gracefully
    if not image_path:
        print("[OCR] ⚠️  No image path provided. Skipping OCR.")
        return ""

    if not os.path.exists(image_path):
        print(f"[OCR] ❌ Image not found at path: '{image_path}'")
        return ""

    print(f"[OCR] 🔍 Running OCR on: '{image_path}'...")

    try:
        # Open image using Pillow
        img = Image.open(image_path)

        # Run Tesseract OCR
        # lang='eng' means English; add '+hin' etc. for other languages
        extracted_text = pytesseract.image_to_string(img, lang='eng').strip()

        if extracted_text:
            print(f"[OCR] ✅ Extracted text:\n  '{extracted_text}'")
        else:
            print("[OCR] ⚠️  No text found in the image. Try better lighting or a clearer image.")

        return extracted_text

    except pytesseract.TesseractNotFoundError:
        print("[OCR] ❌ Tesseract is not installed or the path is wrong.")
        print("[OCR]    Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
        print("[OCR]    Then set TESSERACT_PATH in this file.")
        return ""

    except Exception as e:
        print(f"[OCR] ❌ OCR error: {e}")
        return ""
