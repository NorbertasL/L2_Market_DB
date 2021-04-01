import time

import mss
import win32gui
from PIL import ImageGrab, Image
import cv2
import numpy as np
import pytesseract
import calendar

import CONSTANTS
from DebugTools import debugg_log


def captureRawImg():
    ts = calendar.timegm(time.gmtime())
    imgTargetName = getTargetNameImg()
    imgItemInfo = getItemInfoImg()
    debugg_log.logRawImgData(imgTargetName, imgItemInfo, ts)

    # Overwriting the variable since we have no more use for raw img
    imgTargetName = convertToGray(imgTargetName)
    imgItemInfo = convertToGray(imgItemInfo)
    debugg_log.logGreyImgData(imgTargetName, imgItemInfo, ts)

def convertToGray(img):
    return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)

def getText(saveData = True):
    itemImg = getItemInfoImg(saveData)
    nameImg = getTargetNameImg(saveData)
    itemImgText = pytesseract.image_to_string(itemImg[0])
    nameImgText = pytesseract.image_to_string(nameImg[0])
    if saveData:
        file = open(CONSTANTS.TESS_DEBUG_DIR+'/Name '+str(nameImg[1])+'.txt', "w+")
        file.write(nameImgText)
        file.close()
        file = open(CONSTANTS.TESS_DEBUG_DIR+'/Item '+str(itemImg[1])+'.txt', "w+")
        file.write(itemImgText)
        file.close()

    return itemImgText, nameImgText


# Grab the image of the name tag
def getTargetNameImg():
    return ImageGrab.grab(bbox=(100, 10, 400, 780))


    #if saveImg:
    #    img.save(CONSTANTS.TESS_DEBUG_DIR+'/Name '+str(ts)+'.png')
    #img_np = np.array(img)
    #nameImage = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)


# Grab the image of the item hovered by the mouse
def getItemInfoImg():
    # So tha grap bbox par are X , Y , X+W, Y+H, what genius designed this?
    # Stupides par i have ever seen for a image capturing
    point = win32gui.GetCursorPos()
    return ImageGrab.grab(bbox=(point[0], point[1], point[0] + 500, point[1] + 500))
   # ts = calendar.timegm(time.gmtime())
    #if saveImg:
   #     img.save(CONSTANTS.TESS_DEBUG_DIR+'/Item '+str(ts)+'.png')
    #img_np = np.array(img)
    #itemImage = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    #return itemImage, ts
