import cv2
from win32api import GetSystemMetrics


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
            cv2.drawContours(backgroundImg, [contours], -1, (0, 255, 0), 1)
        cv2.imshow(self.windowName, backgroundImg)

    def destroy(self):
        cv2.destroyWindow(self.windowName)
