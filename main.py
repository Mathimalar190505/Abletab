# main.py
# ============================================================
#   AbleTab — Assistive Learning System (Phase 1 Simulation)
#   Run with: python main.py
# ============================================================
#
# This is the main controller. It ties together all modules:
#   - Input:      mic, camera, buttons
#   - Processing: speech-to-text, OCR
#   - Output:     display, TTS, braille, avatar
#   - Storage:    save to file
# ============================================================

# ── Input modules ──────────────────────────────────────────
from input.mic      import get_mic_input
from input.camera   import get_camera_input
from input.buttons  import get_mode

# ── Processing modules ─────────────────────────────────────
from processing.stt import speech_to_text
from processing.ocr import extract_text_from_image

# ── Output modules ─────────────────────────────────────────
from output.display import show_captions
from output.tts     import speak
from output.braille import convert_to_braille
from output.avatar  import show_sign_language

# ── Storage module ─────────────────────────────────────────
from storage.save   import save_text, read_all_notes


def run():
    """
    Main function that runs the full AbleTab simulation pipeline.
    """
    print("\n" + "=" * 55)
    print("       Welcome to AbleTab — Assistive Learning System")
    print("              Phase 1: Software Simulation")
    print("=" * 55)

    # ── STEP 1: Collect inputs ─────────────────────────────
    print("\n--- [ INPUT PHASE ] ---")
    raw_audio   = get_mic_input()       # Simulated mic input
    image_path  = get_camera_input()    # Simulated camera input
    mode        = get_mode()            # User selects assistive mode

    # ── STEP 2: Process inputs ─────────────────────────────
    print("\n--- [ PROCESSING PHASE ] ---")
    speech_text = speech_to_text(raw_audio)         # STT: audio → text
    ocr_text    = extract_text_from_image(image_path)  # OCR: image → text

    # Combine both text sources into one final string
    final_text = f"{speech_text} | {ocr_text}"
    print(f"\n[MAIN] Combined final text: '{final_text}'")

    # ── STEP 3: Route outputs based on selected mode ───────
    print(f"\n--- [ OUTPUT PHASE — Mode: '{mode.upper()}' ] ---")

    if mode == "blind":
        # Blind mode: audio speech + braille
        speak(final_text)
        convert_to_braille(final_text)

    elif mode == "deaf":
        # Deaf mode: on-screen captions + sign language avatar
        show_captions(final_text)
        show_sign_language(final_text)

    elif mode == "both":
        # Both modes: all outputs enabled
        show_captions(final_text)
        speak(final_text)
        convert_to_braille(final_text)
        show_sign_language(final_text)

    # ── STEP 4: Save to storage ────────────────────────────
    print("\n--- [ STORAGE PHASE ] ---")
    save_text(final_text)

    # ── STEP 5: Show all saved notes ───────────────────────
    print("\n--- [ SESSION LOG ] ---")
    read_all_notes()

    print("\n" + "=" * 55)
    print("              AbleTab session complete. Goodbye!")
    print("=" * 55 + "\n")


# ── Entry point ────────────────────────────────────────────
if __name__ == "__main__":
    run()
