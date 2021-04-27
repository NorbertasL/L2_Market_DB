# Dir paths
from collections import namedtuple
from dataclasses import dataclass

import numpy

DEBUG_DIR = 'DEBUG'
LOGFILE_DIR = DEBUG_DIR + '/LOGS'
TESS_DEBUG_DIR_GREY_IMG = DEBUG_DIR + '/TESS/GREY_IMG'  # Grey scale
TESS_DEBUG_DIR_PARSED_TXT = DEBUG_DIR + '/TESS/PARSED_TXT'

# Img box sizes and locations
NAME_LOC = (880, 7)
NAME_BOX_SIZE = (115, 17)

# Debug log settings
LOG = True
LOG_NAME = "L2_Market_DB_Log.txt"
LOGFILE_PATH = LOGFILE_DIR + '/' + LOG_NAME
GREY_IMG_DATA = True
PARSED_TXT_DATA = False


class ImageData:
    def __init__(self):
        self.__rawImage = None
        self.__grayImage = None
        self.__targetRec = None

    def setRawImage(self, rawImage: numpy.ndarray):
        self.__rawImage = rawImage.copy()

    def getRawImage(self) -> numpy.ndarray:
        return self.__rawImage

    def setGrayImage(self, grayImage: numpy.ndarray):
        self.__grayImage = grayImage.copy()

    def getGreyImage(self) -> numpy.ndarray:
        return self.__grayImage

    def setRecBounds(self, targetRec: numpy.ndarray):
        self.__targetRec = targetRec.copy()

    def getRecBounds(self) -> numpy.ndarray:
        return self.__targetRec
