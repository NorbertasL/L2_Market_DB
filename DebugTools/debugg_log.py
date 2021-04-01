import calendar
import time

import CONSTANTS


def logRawImgData(nameImg, itemImg, ts=calendar.timegm(time.gmtime())):

    if CONSTANTS.RAW_IMG_DATA:
        # Saving raw img data
        itemImg.save(CONSTANTS.TESS_DEBUG_DIR_RAW + '/Rew_Item ' + str(ts) + '.png')
        nameImg.save(CONSTANTS.TESS_DEBUG_DIR_RAW + '/Raw_Name ' + str(ts) + '.png')
