#https://pythonhosted.org/pynput/keyboard.html
from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))

class KeyListener:
    listener = None

    def start(self):
        self.listener = Listener(on_press=on_press, on_release=on_release, suppress=True)
        self.listener.start()
        return self

    def stop(self):
        print("Stopping key listener:", self.listener)
        if self.listener is not None:
            self.listener.stop()
            self.listener = None




