import mss
import win32gui
from PIL import ImageGrab, Image
import cv2
import numpy as np
import pytesseract


def getText():
    return pytesseract.image_to_string(getItemInfoImg()), pytesseract.image_to_string(getTargetNameImg())


# Grab the image of the name tag
def getTargetNameImg():
    img_np = np.array(ImageGrab.grab(bbox=(100, 10, 400, 780)))
    nameImage = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    return nameImage


# Grab the image of the item hovered by the mouse
def getItemInfoImg():
    # So tha grap bbox par are X , Y , X+W, Y+H, what genius designed this?
    # Stupides par i have ever seen for a image capturing
    point = win32gui.GetCursorPos()
    img_np = np.array(ImageGrab.grab(bbox=(point[0], point[1], point[0] + 500, point[1] + 500)))
    itemImage = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    return itemImage
