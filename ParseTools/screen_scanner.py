from win32api import GetSystemMetrics
import numpy
from mss import mss
import cv2
import imutils

# Gets 1st monitors size and we start at the top left
import CONSTANTS

monitor = {'top': 0, 'left': 0, 'width': GetSystemMetrics(0), 'height': GetSystemMetrics(1)}


def getImage() -> CONSTANTS.ImageData:
    returnData = CONSTANTS.ImageData()
    rawImg = numpy.array(mss().grab(monitor))
    gray = cv2.cvtColor(rawImg, cv2.COLOR_BGR2GRAY)
    # Turns all the non black pixels white
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
    # Inverts the colour of the black and white image
    thresh = cv2.bitwise_not(thresh)
    # Finds contours cv2.RETR_LIST seems to work best
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    returnData.setRawImage(rawImg)  # Storing for display purposes

    targetRec = None
    for c in cnts:

        # Approximates all the points
        approx = cv2.approxPolyDP(c, 1, True)

        # if approx is 4 its a rectangle
        if len(approx) == 4:
            minArea = 7000
            area = cv2.contourArea(approx)

            # Area of rectangle has to be bigger than the minArea
            # I know that my item rectangle has to be above a certain size
            if area > minArea:
                # There is 2 rectangle enveloping the item, I want the inner one
                if targetRec is None or cv2.contourArea(targetRec) > area:
                    targetRec = approx
                    returnData.setRecBounds(targetRec)
                    returnData.setGrayImage(gray)
                    # x,y,w,h = cv2.boundingRect(c)
                    # Draws green lines around the rectangle
                    # cv2.drawContours(imgToDrawOn, [c], -1, (0, 255, 0), 1)
    return returnData
