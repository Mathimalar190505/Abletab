# input/buttons.py
# Simulates physical button presses for mode selection
# In a real system, GPIO buttons would set the mode

VALID_MODES = ["blind", "deaf", "both"]

def get_mode():
    """
    Simulates a button press to select the assistive mode.
    Prompts the user via terminal input.
    Returns: 'blind', 'deaf', or 'both'
    """
    print("\n[BUTTONS] Select assistive mode:")
    print("  1. blind  → Braille + Audio output")
    print("  2. deaf   → Captions + Sign language avatar")
    print("  3. both   → All outputs enabled")

    while True:
        choice = input("Enter mode (blind / deaf / both): ").strip().lower()
        if choice in VALID_MODES:
            print(f"[BUTTONS] Mode selected: '{choice}'")
            return choice
        else:
            print(f"[BUTTONS] Invalid choice '{choice}'. Please enter: blind, deaf, or both.")
