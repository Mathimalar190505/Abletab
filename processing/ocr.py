# processing/ocr.py
# Optical Character Recognition (OCR) module
# Phase 1: Returns dummy extracted text from a simulated image path
# Phase 2+: Can integrate Tesseract OCR or Google Vision API here

def extract_text_from_image(image_path):
    """
    Simulates extracting text from an image using OCR.
    Returns a hardcoded dummy result for Phase 1 simulation.

    Args:
        image_path (str): The path to the captured image (simulated).

    Returns:
        str: Dummy text as if it were extracted from the image.
    """
    print(f"[OCR] Extracting text from image: '{image_path}'...")

    # Dummy OCR result — simulates what OCR would read from a textbook image
    dummy_extracted_text = "Photosynthesis converts light energy into chemical energy stored in glucose."

    print(f"[OCR] Extracted text: '{dummy_extracted_text}'")
    return dummy_extracted_text
