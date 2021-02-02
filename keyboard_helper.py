#https://pythonhosted.org/pynput/keyboard.html
from pynput.keyboard import Key, Listener, KeyCode

import img_helper


def on_release(key):
    print('{0} release'.format(
        key))


def on_press(key):
    print('{0} pressed'.format(key))

    first, second = (img_helper.getText(True))
    print(first)
    #print(second)


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




