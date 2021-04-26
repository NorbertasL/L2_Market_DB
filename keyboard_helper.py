import keyboard

import app_variables
import CONSTANTS
from DebugTools import debug_log
from ParseTools import img_parse


# TODO Look into implementing this to solve the game suppressing keyEvents
# https://gist.github.com/ethanhs/80f0a7cc5c7881f5921f
# TODO will probably need to create my own low level key listener, but first i need to test is if the low level solution
# actually works.
def on_press(keyInfo):
    if app_variables.gatherDataOn:
        print("Gathering screen data...")
        # Capturing img
        debug_log.addLog("KEYBOARD", "Capture key was pressed.")
        img_parse.captureRawImg()
    # print("YOU DISABLED CAPTURING KEY IN keyboard_helper")


class KeyListener:

    def __init__(self):
        self.listener = keyboard.on_press_key(app_variables.TAKE_PIC_KEY, on_press)
        print("Starting key listener:", self.listener)

    def stop(self):
        print("Stopping key listener:", self.listener)
        if self.listener is not None:
            keyboard.unhook_all()
