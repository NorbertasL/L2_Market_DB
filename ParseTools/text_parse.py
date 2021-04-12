from collections import namedtuple
import re

from pytesseract import pytesseract

from DebugTools import debug_log

ItemData = namedtuple('ItemData', ['itemName', 'seenAs', 'price', 'quantity', 'location', 'person'])


def parseDataFromImgs(nameImg, itemImg, ts):
    # Tess extraction
    nameText = pytesseract.image_to_string(nameImg)
    itemText = pytesseract.image_to_string(itemImg)
    debug_log.logRawTxTData(nameText, itemText, ts)

    # Parsing
    parseName(nameText)
    parseItemData(itemText)

    # TODO continue process path by parsing the txt data into proper chunks


def parseName(nameText):
    nameText = nameText.splitlines()
    ItemData.person = nameText[0]
    print("Parsed Name:", nameText[0])


def parseItemData(itemText):
    priceTag = "price"
    itemText = itemText.splitlines()
    index = 0
    print("Item Text is:", itemText)
    for line in itemText:
        line.lower()
        line.strip()
        if priceTag in line:
            if parsePriceNumbers(line, itemText[index+1]):
                parseItemNameAndQuantity(itemText[index-1])  # Name is above
                return  # Breaking loop, because we got the data
        index += 1


def parsePriceNumbers(line, nextLine):
    # TODO Extract number
    # TODO check number value with next line that should also be a price but with words
    number = re.sub(r'[^a-zA-Z0-9]', "", line)
    print(number)

    # return true if number was extracted
    return False


def parseItemNameAndQuantity():
    # TODO extract name and quantity of exists
    return


""" The way Im gona parrse the data is
1:Will Look for the word "price"
2:Check if its followed by a number
3:If not will look for the next one
4: If True will parse the price data
5 The line above is the name so will parse that
6 will check the line below price to confirm value
"""
