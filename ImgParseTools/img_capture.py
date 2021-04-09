import time

import pyautogui as pyautogui
import win32gui
import cv2
import numpy as np
import pytesseract
import calendar

import CONSTANTS
from DebugTools import debug_log
from ImgParseTools import text_parse


def captureRawImg():
    ts = calendar.timegm(time.gmtime())
    imgTargetName = getTargetNameImg()
    imgItemInfo = getItemInfoImg()
    debug_log.logRawImgData(imgTargetName, imgItemInfo, ts)

    # Overwriting the variable since we have no more use for raw img
    imgTargetName = simplifyImg(imgTargetName)
    imgItemInfo = simplifyImg(imgItemInfo)
    debug_log.logGreyImgData(imgTargetName, imgItemInfo, ts)

    text_parse.extractNameAndItemData(imgTargetName, imgItemInfo, ts)  # passing in ts for debugging


def simplifyImg(img):
    # Making img grey scale
    tempImg = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)

    # inverting black and white, because tess works better with dark  text on light background
    tempImg = cv2.bitwise_not(tempImg)
    return tempImg

# TODO move this to text_parse.py
def getText(saveData=True):
    itemImg = getItemInfoImg()
    nameImg = getTargetNameImg()
    itemImgText = pytesseract.image_to_string(itemImg[0])
    nameImgText = pytesseract.image_to_string(nameImg[0])
    if saveData:
        file = open(CONSTANTS.TESS_DEBUG_DIR_RAW_TXT + '/Name ' + str(nameImg[1]) + '.txt', "w+")
        file.write(nameImgText)
        file.close()
        file = open(CONSTANTS.TESS_DEBUG_DIR_RAW_TXT + '/Item ' + str(itemImg[1]) + '.txt', "w+")
        file.write(itemImgText)
        file.close()

    return itemImgText, nameImgText


# Grab the image of the name tag
def getTargetNameImg():
    return pyautogui.screenshot(region=(CONSTANTS.NAME_LOC[0], CONSTANTS.NAME_LOC[1],
                                CONSTANTS.NAME_BOX_SIZE[0], CONSTANTS.NAME_BOX_SIZE[1]))

# Grab the image of the item hovered by the mouse
def getItemInfoImg():
    point = win32gui.GetCursorPos()
    # NOTE: The offset numbers are here, because to get item the mouse needs to be anywhere in the item box,
    # but the info window always starts from the top left cornet(it invert flips if space is an issue, but
    # im not going to deal with it any time soon)
    return pyautogui.screenshot(region=(point[0]-40, point[1] - CONSTANTS.ITEM_BOX_SIZE[1],
                                        CONSTANTS.ITEM_BOX_SIZE[0], CONSTANTS.ITEM_BOX_SIZE[1]))
