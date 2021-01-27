import mss
import win32gui
from PIL import ImageGrab
import cv2
import numpy as np


class ImageHelper:
    # currentTargetImg = None
    currentItemImage = None

    def getTargetNameImg(self):
        img = ImageGrab.grab(bbox=(100,10,400,780))
        img_np = np.array(img)
        return cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    def getItemInfoImg(self, point):
        print(point[0]," ", point[1])
        #So tha grap bbox par are X , Y , X+W, Y+H, what genius designed this?
        #Stupides par i have ever seen for a image capturing
        img_np = np.array(ImageGrab.grab(bbox=(point[0], point[1], point[0]+500, point[1]+500)))
        return cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)



    def showImage(self, img):
        cv2.imshow('test', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


imgHelper = ImageHelper()
imgHelper.showImage(imgHelper.getItemInfoImg(win32gui.GetCursorPos()))
