# input/mic.py
# Simulates microphone input
# In a real system, this would capture audio from a hardware mic

def get_mic_input():
    """
    Simulates capturing audio from a microphone.
    Returns a pre-defined text string as if it were spoken by the user.
    """
    # Simulated spoken input (replace this with real STT later)
    simulated_speech = "The mitochondria is the powerhouse of the cell."
    print(f"[MIC] Simulated audio captured: '{simulated_speech}'")
    return simulated_speech
