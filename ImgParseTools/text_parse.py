from pytesseract import pytesseract

from DebugTools import debug_log


def extractNameAndItemData(nameImg, itemImg, ts):
    nameTxt = pytesseract.image_to_string(nameImg)
    itemText = pytesseract.image_to_string(itemImg)
    debug_log.logRawTxTData(nameTxt, itemText, ts)

    # TODO continue process path by parsing the txt data into proper chunks
