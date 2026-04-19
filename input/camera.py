# input/camera.py
# Simulates camera input
# In a real system, this would capture a live image frame from a camera

def get_camera_input():
    """
    Simulates capturing an image from a camera.
    Returns a dummy image path as if a photo was taken.
    """
    # Simulated image path (no real image needed for Phase 1)
    simulated_image_path = "data/sample_image.jpg"
    print(f"[CAMERA] Simulated image captured from path: '{simulated_image_path}'")
    return simulated_image_path
