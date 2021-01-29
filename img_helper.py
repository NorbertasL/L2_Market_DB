import mss
import win32gui
from PIL import ImageGrab
import cv2
import numpy as np
import pytesseract
from enum import Enum


class ImageHelper:
    itemImage = None
    nameImage = None

    # Grab the image of the name tag
    def getTargetNameImg(self):
        img_np = np.array(ImageGrab.grab(bbox=(100, 10, 400, 780)))
        self.nameImage = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        return self.nameImage

    # Grab the image of the item hovered by the mouse
    def getItemInfoImg(self):
        # So tha grap bbox par are X , Y , X+W, Y+H, what genius designed this?
        # Stupides par i have ever seen for a image capturing
        point = win32gui.GetCursorPos()
        img_np = np.array(ImageGrab.grab(bbox=(point[0], point[1], point[0] + 500, point[1] + 500)))
        self.itemImage = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        return self.itemImage

    def showImage(self, ImageRef):
        img = None
        # using enum here for future expansion.IFs will prob be replaced by switches too
        if ImageRef == ImageRef.ITEM:
            img = self.itemImage
        elif ImageRef == ImageRef.NAME:
            img = self.nameImage

        cv2.imshow(ImageRef.value + ' test', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    class ImageRef(Enum):
        ITEM = "ITEM"
        NAME = "NAME"


# TEST
ih = ImageHelper()
ih.getItemInfoImg()
ih.showImage(ImageHelper.ImageRef.ITEM)

