# output/display.py
# Display module — shows captions on screen
# In a real system, this could drive an LCD or send text to a screen overlay

def show_captions(text):
    """
    Displays the final text as captions on the console.
    Simulates a screen or caption display for deaf users.

    Args:
        text (str): The combined text to be displayed.
    """
    print("\n" + "=" * 50)
    print("[DISPLAY] 📺 CAPTIONS:")
    print(f"  {text}")
    print("=" * 50)
