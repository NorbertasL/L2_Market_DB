import time

from PIL import Image

import CONSTANTS
import db_conn
import main_gui
import app_variables
import overlay_display
from DebugTools.debug_log import logGreyImgData

from ParseTools import screen_scanner, img_parse, text_parse
from DebugTools import debug_display

app_variables.appRunning = True
gui = main_gui.MasterGui()
debugDisplayWindow = None
debugDisplayWindowName = "Debug Display"
lastRec = None

# Test rectangle for overlay

overlay = None


def compareRec(rec1, rec2) -> bool:
    # Checking two opposite corners to see if its the same rec
    topLeftCorner = rec1[0][0][0] == rec2[0][0][0] and rec1[0][0][1] == rec2[0][0][1]
    botRightCorner = rec1[2][0][0] == rec2[2][0][0] and rec1[2][0][1] == rec2[2][0][1]
    return topLeftCorner and botRightCorner


def __closeDebugWindow():
    if debugDisplayWindow is not None:
        debugDisplayWindow.destroy()


def __closeApp():
    __closeDebugWindow()


while app_variables.appRunning:
    gui.mainWindow.update_idletasks()
    gui.mainWindow.update()

    if app_variables.gatherDataOn:
        # Starts gathering data from screen/monitor
        data = screen_scanner.getImage()

        if app_variables.isOverlayOn():
            if overlay is None:
                overlay = overlay_display.Overlay()
            rec = data.get("targetRec")
            overlay.updatePaint(rec)

        if app_variables.isDebugWindowOn():
            # Displays image in real time with boundary boxes on 2nd screen
            if debugDisplayWindow is None:
                debugDisplayWindow = debug_display.Display(debugDisplayWindowName)
            # TODO draw around name box too
            debugDisplayWindow.display(data.getRawImage(), data.getRecBounds())

        if data.getRecBounds() is not None:
            if lastRec is None or not compareRec(lastRec, data.getRecBounds()):
                lastRec = data.getRecBounds()
                print("New Item!")
                # Parsing img
                croppedImgs = img_parse.cropImage(data)

                # Debug log
                logGreyImgData(croppedImgs[0], croppedImgs[1])

                itemData = (text_parse.parseDataFromImgs(croppedImgs[0], croppedImgs[1]))
                print(itemData)
                # Checking if item name exists in DB
                if not db_conn.checkItemNameExists(itemData[1]):
                    print("Unseen item:", itemData[1])
                    db_conn.addNewItemName(itemData[1])
                else:
                    print("Item:", itemData[1], " - is in the DB")



    else:
        __closeApp()

    # What do we do when main gui is closed
    if not app_variables.mainGuiRunning:
        __closeApp()
        # TODO Close all resources and do any config/data saves
        break
