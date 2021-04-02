# https://pythonhosted.org/pynput/keyboard.html
from pynput.keyboard import Listener, KeyCode, GlobalHotKeys

import CONSTANTS
from ImgParseTools import img_capture


def on_press():
    #print('{0} pressed'.format(key))
    #if key == KeyCode.from_char(CONSTANTS.TAKE_PIC_KEY):
    print("Gathering screen data...")
    # Capturing img
    img_capture.captureRawImg()


class KeyListener:
    listener = GlobalHotKeys({
        CONSTANTS.TAKE_PIC_KEY: on_press
    })

    def start(self):
        #self.listener = Listener(on_press=on_press)
        self.listener.start()
        print("Starting key listener:", self.listener)
        return self

    def stop(self):
        print("Stopping key listener:", self.listener)
        if self.listener is not None:
            self.listener.stop()
