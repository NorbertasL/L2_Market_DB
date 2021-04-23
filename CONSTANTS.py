# Dir paths
from collections import namedtuple
from dataclasses import dataclass

DEBUG_DIR = 'DEBUG'
LOGFILE_DIR = DEBUG_DIR + '/LOGS'
TESS_DEBUG_DIR_RAW_IMG = DEBUG_DIR + '/TESS/RAW_IMG'
TESS_DEBUG_DIR_GREY_IMG = DEBUG_DIR + '/TESS/GREY_IMG'  # Grey scale
TESS_DEBUG_DIR_RAW_TXT = DEBUG_DIR + '/TESS/RAW_TXT'
TESS_DEBUG_DIR_PARSED_TXT = DEBUG_DIR + '/TESS/PARSED_TXT'

# Img box sizes and locations
NAME_LOC = (876, 0)
NAME_BOX_SIZE = (170, 45)
ITEM_BOX_SIZE = (200, 120)
# Debug log settings
LOG = True
LOG_NAME = "L2_Market_DB_Log.txt"
LOGFILE_PATH = LOGFILE_DIR + '/' + LOG_NAME
RAW_IMG_DATA = True
GREY_IMG_DATA = True
RAW_TXT_DATA = True
PARSED_TXT_DATA = True



