import calendar
import time
import CONSTANTS


def logRawImgData(nameImg, itemImg, ts=calendar.timegm(time.gmtime())):
    if CONSTANTS.RAW_IMG_DATA:
        # Saving raw img data
        itemImgName = 'Rew_Item ' + str(ts) + '.png'
        nameImgName = 'Raw_Name ' + str(ts) + '.png'
        itemImg.save(CONSTANTS.TESS_DEBUG_DIR_RAW + '/' + itemImgName)
        addLog("Created " + itemImgName, ts)
        nameImg.save(CONSTANTS.TESS_DEBUG_DIR_RAW + '/' + nameImgName)
        addLog("Created " + nameImgName, ts)

def addLog(message, ts=calendar.timegm(time.gmtime())):
    if CONSTANTS.LOG:
        log = open(CONSTANTS.LOGFILE, 'a')
        log.write(ts + ':' + message)
        log.close()
