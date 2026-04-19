# input/camera.py
# Phase 2: Captures a REAL image from the webcam
# Saves it to data/images/ and returns the file path
# Requires: opencv-python
#   pip install opencv-python

import cv2
import os
from datetime import datetime

# Folder to save captured images
IMAGE_DIR = "data/images"

def get_camera_input():
    """
    Opens the webcam, captures one frame, saves it as a .jpg file.
    Returns the path to the saved image, or None on failure.
    """
    try:
        # Create images folder if it doesn't exist
        os.makedirs(IMAGE_DIR, exist_ok=True)

        print("[CAMERA] 📷 Opening webcam...")

        # 0 = default webcam. Change to 1, 2, etc. if you have multiple cameras
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("[CAMERA] ❌ Could not open webcam. Is it connected?")
            return None

        # Let the camera warm up for a moment (avoids dark first frame)
        for _ in range(5):
            cap.read()

        # Capture the actual frame
        ret, frame = cap.read()
        cap.release()  # Always release the camera after use

        if not ret or frame is None:
            print("[CAMERA] ❌ Failed to capture image frame.")
            return None

        # Save with a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename  = f"capture_{timestamp}.jpg"
        filepath  = os.path.join(IMAGE_DIR, filename)

        cv2.imwrite(filepath, frame)
        print(f"[CAMERA] ✅ Image saved to: '{filepath}'")

        return filepath

    except Exception as e:
        print(f"[CAMERA] ❌ Camera error: {e}")
        print("[CAMERA] ⚠️  Make sure 'opencv-python' is installed: pip install opencv-python")
        return None
