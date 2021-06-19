#  Tool to parse decrypted l2 .dat(.txt) file into DBs
import db_conn


def __parseItemNameLine(line: str) -> [int, str]:
    s = line.split("\t")
    return int(s[0]), s[1]

def parseItemsToDB(itemFilePath):
    with open(itemFilePath, "r") as itemFile:
        for line in itemFile:
            try:
                item = __parseItemNameLine(line)
            except ValueError:
                # Skipping bad lines
                continue
            db_conn.addNewItemName(item[1], item[0])

def makeWordList(itemFilePath, outFilePath):
    with open(itemFilePath, "r") as itemFile:
        for line in itemFile:
            try:
                item = __parseItemNameLine(line)
            except ValueError:
                # Skipping bad lines
                continue
            with open(outFilePath, "a") as outFile:
                outFile.write(item[1]+"\n")
                print(item[1] + " added...")




