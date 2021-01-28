#https://pythonhosted.org/pynput/keyboard.html
from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
def listener():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
def stopListener():
    Listener.stop


