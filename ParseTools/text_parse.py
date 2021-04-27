from collections import namedtuple
import re

from pytesseract import pytesseract

from DebugTools import debug_log

ItemData = namedtuple('ItemData', ['itemName', 'seenAs', 'price', 'quantity', 'location', 'person'])


def parseDataFromImgs(nameImg, itemImg):
    # Tess extraction
    nameText = pytesseract.image_to_string(nameImg)
    itemText = pytesseract.image_to_string(itemImg)

    # Parsing
    name = parseName(nameText)
    itemName, itemQuantity, price = parseItemData(itemText)

    return name, itemName, itemQuantity, price

    # TODO continue process path by parsing the txt data into proper chunks


def parseName(nameText):
    nameText = nameText.splitlines()
    ItemData.person = nameText[0]
    return nameText[0]


def parseItemData(itemText):
    priceTag = "price"
    itemText = itemText.splitlines()
    index = 0
    for line in itemText:
        line = line.lower()
        line = line.strip()

        if priceTag in line:
            itemName, itemQuantity = parseItemNameAndQuantity(itemText[index-1])
            price = parsePriceNumbers(line)
            return itemName, itemQuantity, price
        index += 1

    '''
    for line in itemText:
        line.lower()
        line.strip()
        if priceTag in line:
            if parsePriceNumbers(line, itemText[index+1]):
                return parseItemNameAndQuantity(itemText[index-1]), parseItemNameAndQuantity(itemText[index]), parseItemNameAndQuantity(itemText[index+1])
                #return  # Breaking loop, because we got the data
        index += 1
        '''


def parsePriceNumbers(line):
    # Extracting just the number
    return re.sub(r'[^0-9]', "", line)


def parseItemNameAndQuantity(line):
    line = line.lower()
    line = line.strip()
    line = re.sub(r'[^ a-z0-9():\']', "", line)

    index = line.find("(")
    if index != -1:
        quantity = line[index:]
        quantity = re.sub(r'[^0-9]', "", quantity)
        name = line[:index]
    else:
        name = line
        quantity = -1

    return name, quantity


""" The way Im gona parrse the data is
1:Will Look for the word "price"
2:Check if its followed by a number
3:If not will look for the next one
4: If True will parse the price data
5 The line above is the name so will parse that
6 will check the line below price to confirm value
"""
