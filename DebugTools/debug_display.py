import cv2
import numpy as np
from win32api import GetSystemMetrics
from CONSTANTS import NAME_LOC, NAME_BOX_SIZE


class Display:
    def __init__(self, windowName):
        self.windowName = windowName
        # Real time display window
        cv2.namedWindow(windowName)
        # Moving display window to 2nd monitor
        cv2.moveWindow(windowName, GetSystemMetrics(0), 0)

    def display(self, backgroundImg, contours):
        # Displays the image with the rectangle lines
        if contours is not None:
            # displaying item box
            cv2.drawContours(backgroundImg, [contours], -1, (0, 255, 0), 1)

        # crating contours for name box
        nameCon = np.array([[[NAME_LOC[0], NAME_LOC[1]]],[[NAME_LOC[0]+NAME_BOX_SIZE[0], NAME_LOC[1]]],
                            [[NAME_LOC[0]+NAME_BOX_SIZE[0], NAME_LOC[1]+NAME_BOX_SIZE[1]]],
                            [[NAME_LOC[0], NAME_LOC[1]+NAME_BOX_SIZE[1]]]])
        # Displaying name box
        cv2.drawContours(backgroundImg, [nameCon], -1, (0, 255, 0), 1)
        cv2.imshow(self.windowName, backgroundImg)

    def destroy(self):
        cv2.destroyWindow(self.windowName)
