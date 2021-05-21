import calendar
import os
import time

from PIL import Image

import CONSTANTS


def logRawImgData(nameImg, itemImg, ts=None):
    if CONSTANTS.RAW_IMG_DATA:
        if ts is None:
            ts = calendar.timegm(time.gmtime())
        dirCheck(CONSTANTS.TESS_DEBUG_DIR_RAW_IMG)
        # Saving raw img data
        print("Saving RAW imgs")
        itemImgName = 'Rew_Item ' + str(ts) + '.png'
        nameImgName = 'Raw_Name ' + str(ts) + '.png'
        itemImg.save(CONSTANTS.TESS_DEBUG_DIR_RAW_IMG + '/' + itemImgName)
        addLog("TESSERACT", "Created " + itemImgName, ts)
        nameImg.save(CONSTANTS.TESS_DEBUG_DIR_RAW_IMG + '/' + nameImgName)
        addLog("TESSERACT", "Created " + nameImgName, ts)


def logGreyImgData(nameImg, itemImg, ts=None, force=False):
    if CONSTANTS.GREY_IMG_DATA or force:
        if ts is None:
            ts = calendar.timegm(time.gmtime())
        dirCheck(CONSTANTS.TESS_DEBUG_DIR_GREY_IMG)
        # Saving grey img data
        print("Saving grey imgs")
        itemImgName = 'Grey_Item ' + str(ts) + '.png'
        nameImgName = 'Grey_Name ' + str(ts) + '.png'

        itemPng = Image.fromarray(itemImg)
        namePng = Image.fromarray(nameImg)

        itemPng.save(CONSTANTS.TESS_DEBUG_DIR_GREY_IMG + '/' + itemImgName)
        addLog("TESSERACT", "Created " + itemImgName, ts)
        namePng.save(CONSTANTS.TESS_DEBUG_DIR_GREY_IMG + '/' + nameImgName)
        addLog("TESSERACT", "Created " + nameImgName, ts)


def logRawTxTData(nameTxt, itemTxt, ts=None):
    if CONSTANTS.RAW_TXT_DATA:
        if ts is None:
            ts = calendar.timegm(time.gmtime())
        dirCheck(CONSTANTS.TESS_DEBUG_DIR_RAW_TXT)
        print("Saving raw txt data")

        nameTxtName = 'Raw_Name ' + str(ts) + '.txt'
        nameData = open(CONSTANTS.TESS_DEBUG_DIR_RAW_TXT + '/' + nameTxtName, 'a')
        nameData.write(nameTxt)
        nameData.close()
        addLog("TESSERACT", "Created " + nameTxtName, ts)

        itemTxtName = 'Raw_Item ' + str(ts) + '.txt'
        itemData = open(CONSTANTS.TESS_DEBUG_DIR_RAW_TXT + '/' + itemTxtName, 'a')
        itemData.write(itemTxt)
        itemData.close()
        addLog("TESSERACT", "Created " + itemTxtName, ts)


def addLog(logType="UNNAMED", message="NO_MESSAGE", ts=None):
    if CONSTANTS.LOG:
        if ts is None:
            ts = calendar.timegm(time.gmtime())
        dirCheck(CONSTANTS.LOGFILE_DIR)
        print("logging data into log file")
        log = open(CONSTANTS.LOGFILE_PATH, 'a')
        log.write(logType + " : " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts)) + '-' + message + '\n')
        log.close()


def dirCheck(dirPath):
    # Checking if dirs exist
    if not os.path.isdir(dirPath):
        # Creating Dir
        os.makedirs(dirPath)
        print("Created dir: " + dirPath)
        addLog("Created new dir: "+dirPath)
