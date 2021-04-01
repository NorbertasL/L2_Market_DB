import calendar
import time
import CONSTANTS


def logRawImgData(nameImg, itemImg, ts=calendar.timegm(time.gmtime())):
    if CONSTANTS.RAW_IMG_DATA:
        # Saving raw img data
        print("Saving RAW imgs")
        itemImgName = 'Rew_Item ' + str(ts) + '.png'
        nameImgName = 'Raw_Name ' + str(ts) + '.png'
        itemImg.save(CONSTANTS.TESS_DEBUG_DIR_RAW + '/' + itemImgName)
        addLog("Created " + itemImgName, ts)
        nameImg.save(CONSTANTS.TESS_DEBUG_DIR_RAW + '/' + nameImgName)
        addLog("Created " + nameImgName, ts)

def addLog(message, ts=calendar.timegm(time.gmtime())):
    if CONSTANTS.LOG:
        print("logging data into log file")
        log = open(CONSTANTS.LOGFILE, 'a')
        log.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts)) + ':' + message + '\n')
        log.close()
