#https://pythonhosted.org/pynput/keyboard.html
from pynput.keyboard import Listener, KeyCode

import CONSTANTS
from ImgParseTools import img_capture


def on_release(key):
    print('{0} release'.format(
        key))


def on_press(key):
    print('{0} pressed'.format(key))
    if key == KeyCode.from_char(CONSTANTS.TAKE_PIC_KEY):
        print("Gathering screen data...")
        # Capturing img
        img_capture.captureRawImg()



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




