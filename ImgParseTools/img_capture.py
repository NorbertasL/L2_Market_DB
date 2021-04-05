import time

import pyautogui as pyautogui
import win32gui
from PIL import ImageGrab
import cv2
import numpy as np
import pytesseract
import calendar

import CONSTANTS
from DebugTools import debugg_log
from ImgParseTools import text_parse


def captureRawImg():
    ts = calendar.timegm(time.gmtime())
    imgTargetName = getTargetNameImg()
    imgItemInfo = getItemInfoImg()
    debugg_log.logRawImgData(imgTargetName, imgItemInfo, ts)

    # Overwriting the variable since we have no more use for raw img
    imgTargetName = convertToGray(imgTargetName)
    imgItemInfo = convertToGray(imgItemInfo)
    debugg_log.logGreyImgData(imgTargetName, imgItemInfo, ts)

    text_parse.extractNameAndItemData(imgTargetName, imgItemInfo, ts)  # passing in ts for debugging


def convertToGray(img):
    return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)


def getText(saveData=True):
    itemImg = getItemInfoImg(saveData)
    nameImg = getTargetNameImg(saveData)
    itemImgText = pytesseract.image_to_string(itemImg[0])
    nameImgText = pytesseract.image_to_string(nameImg[0])
    if saveData:
        file = open(CONSTANTS.TESS_DEBUG_DIR + '/Name ' + str(nameImg[1]) + '.txt', "w+")
        file.write(nameImgText)
        file.close()
        file = open(CONSTANTS.TESS_DEBUG_DIR + '/Item ' + str(itemImg[1]) + '.txt', "w+")
        file.write(itemImgText)
        file.close()

    return itemImgText, nameImgText


# Grab the image of the name tag
def getTargetNameImg():
    return pyautogui.screenshot(region=(CONSTANTS.NAME_LOC[0], CONSTANTS.NAME_LOC[1],
                                CONSTANTS.NAME_BOX_SIZE[0], CONSTANTS.NAME_BOX_SIZE[1]))

    # if saveImg:
    #    img.save(CONSTANTS.TESS_DEBUG_DIR+'/Name '+str(ts)+'.png')
    # img_np = np.array(img)
    # nameImage = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)


# Grab the image of the item hovered by the mouse
def getItemInfoImg():
    # So tha grap bbox par are X , Y , X+W, Y+H, what genius designed this?
    # Stupides par i have ever seen for a image capturing
    point = win32gui.GetCursorPos()
    # NOTE: The offset numbers are here, because to get item the mouse needs to be anywhere in the item box,
    # but the info window always starts from the top left cornet(it invert flips if space is an issue, but
    # im not going to deal with it any time soon)
    return pyautogui.screenshot(region=(point[0]-40, point[1] - CONSTANTS.ITEM_BOX_SIZE[1],
                                        CONSTANTS.ITEM_BOX_SIZE[0], CONSTANTS.ITEM_BOX_SIZE[1]))
    #return ImageGrab.grab(bbox=(point[0], point[1],
    #                            point[0] + 200, point[1] + 200))
# ts = calendar.timegm(time.gmtime())
# if saveImg:
#     img.save(CONSTANTS.TESS_DEBUG_DIR+'/Item '+str(ts)+'.png')
# img_np = np.array(img)
# itemImage = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
# return itemImage, ts
