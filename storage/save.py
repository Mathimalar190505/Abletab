# storage/save.py
# Phase 2: Upgraded storage with session folders and audio file tracking
# Each session gets its own timestamped folder inside data/sessions/
# Saves: session text log + reference to audio file used

import os
import shutil
from datetime import datetime

# Root folder for all session data
SESSIONS_DIR = "data/sessions"

# Legacy flat notes file (kept for backward compatibility)
NOTES_FILE = "data/notes.txt"

def _get_session_dir():
    """
    Creates and returns a unique session folder path based on current timestamp.
    Example: data/sessions/session_20260419_143022/
    """
    timestamp  = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = os.path.join(SESSIONS_DIR, f"session_{timestamp}")
    os.makedirs(session_dir, exist_ok=True)
    return session_dir, timestamp


def save_text(text, audio_path=None):
    """
    Saves the session text to both a per-session folder and the legacy notes file.
    Optionally copies the recorded audio file into the session folder.

    Args:
        text       (str):       The final combined text from this session.
        audio_path (str|None):  Path to the recorded .wav file (from mic.py), if any.
    """
    os.makedirs("data", exist_ok=True)

    # ── Per-session folder ──────────────────────────────────────────────────
    session_dir, timestamp = _get_session_dir()

    # Save text log for this session
    text_log_path = os.path.join(session_dir, "transcript.txt")
    with open(text_log_path, "w", encoding="utf-8") as f:
        f.write(f"Session: {timestamp}\n")
        f.write(f"Text   : {text}\n")
        if audio_path:
            f.write(f"Audio  : {os.path.basename(audio_path)}\n")

    print(f"\n[STORAGE] 💾 Session saved to: '{session_dir}/'")
    print(f"[STORAGE]    transcript.txt → '{text}'")

    # ── Copy audio file into session folder ─────────────────────────────────
    if audio_path and os.path.exists(audio_path):
        dest = os.path.join(session_dir, os.path.basename(audio_path))
        shutil.copy2(audio_path, dest)
        print(f"[STORAGE]    audio copied  → '{os.path.basename(audio_path)}'")

    # ── Append to legacy flat notes file ────────────────────────────────────
    entry = f"[{timestamp}] {text}\n"
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


def read_all_notes():
    """
    Reads and prints all entries from the legacy notes.txt file.
    Gives a quick overview of all past sessions.
    """
    if not os.path.exists(NOTES_FILE):
        print("[STORAGE] No saved notes found yet.")
        return

    print(f"\n[STORAGE] 📂 All saved sessions (from '{NOTES_FILE}'):")
    print("─" * 55)
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        contents = f.read()
        print(contents.strip() if contents.strip() else "(No entries yet)")
    print("─" * 55)


def list_sessions():
    """
    Lists all saved session folders with a summary of their contents.
    Useful for reviewing what was captured across multiple runs.
    """
    if not os.path.exists(SESSIONS_DIR):
        print("[STORAGE] No sessions saved yet.")
        return

    sessions = sorted(os.listdir(SESSIONS_DIR))
    print(f"\n[STORAGE] 📁 {len(sessions)} session(s) found in '{SESSIONS_DIR}':")
    for session in sessions:
        session_path = os.path.join(SESSIONS_DIR, session)
        files = os.listdir(session_path)
        print(f"  • {session}  ({', '.join(files)})")
