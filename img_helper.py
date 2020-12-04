# Handles Taking the image and proceeding the text
import mss
from PIL import ImageGrab
import cv2
import numpy as np


class ImageHelper:
    # currentTargetImg = None
    currentItemImage = None

    def getTargetNameImg(self):
        global currentTargetImg
        img = ImageGrab.grab(bbox=(100,10,400,780))
        img_np = np.array(img)
        currentTargetImg = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)


    def showImage(self):
        cv2.imshow('test', currentTargetImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


imgHelper = ImageHelper()
imgHelper.getTargetNameImg()
imgHelper.showImage()