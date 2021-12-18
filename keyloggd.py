from pynput import keyboard

def on_press(key):
    global keys_pressed
    if key == keyboard.Key.shift:
        return
    print(str(key).replace("'", "").replace("Key.", ""))

while True:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
