# storage/save.py
# Storage module — saves session text to a file
# Keeps a running log of all processed text across sessions

import os
from datetime import datetime

# Path to the notes file (relative to where main.py is run from)
NOTES_FILE = "data/notes.txt"

def save_text(text):
    """
    Appends the given text to the notes file with a timestamp.
    Creates the file if it doesn't exist.

    Args:
        text (str): The final combined text to save.
    """
    # Make sure the data/ folder exists
    os.makedirs("data", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {text}\n"

    # Append to the file (creates it if it doesn't exist)
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"\n[STORAGE] 💾 Text saved to '{NOTES_FILE}'")
    print(f"[STORAGE] Entry: {entry.strip()}")


def read_all_notes():
    """
    Reads and prints all saved notes from the storage file.
    Useful for reviewing past sessions.
    """
    if not os.path.exists(NOTES_FILE):
        print("[STORAGE] No saved notes found yet.")
        return

    print(f"\n[STORAGE] 📂 All saved notes from '{NOTES_FILE}':")
    print("-" * 50)
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        contents = f.read()
        print(contents if contents.strip() else "(File is empty)")
    print("-" * 50)
