import sqlite3
import calendar
import time
import CONSTANTS

connection = sqlite3.connect("L2RebornMarket.db")
cursor = connection.cursor()

SEEN_PRICE_TABLE_NAME = "SeenItemPrices"
ITEM_NAME_LIST_TABLE_NAME = "ItemNameList"

seenItemPriceTable = """CREATE TABLE IF NOT EXISTS "%s" (
"_id"	INTEGER NOT NULL UNIQUE,
"name"	TEXT NOT NULL,
"seenAs"	TEXT NOT NULL,
"price"	INTEGER NOT NULL,
"quantity"	INTEGER NOT NULL,
"date"	TEXT NOT NULL,
"location"	TEXT,
"person"	TEXT,
"user" TEXT NOT NULL,
PRIMARY KEY("_id" AUTOINCREMENT)
);""" % SEEN_PRICE_TABLE_NAME

itemNameListTable = """
CREATE TABLE IF NOT EXISTS "%s" (
"_id"	INTEGER NOT NULL UNIQUE,
"name"	TEXT NOT NULL UNIQUE,
"itemId"	INTEGER,
PRIMARY KEY("_id" AUTOINCREMENT)
);
""" % ITEM_NAME_LIST_TABLE_NAME

cursor.execute(seenItemPriceTable)
cursor.execute(itemNameListTable)


def addNewItem(name, itemId=-1):
    try:
        command = """INSERT INTO %s (name, itemId)
        VALUES ('%s', %d)""" % (ITEM_NAME_LIST_TABLE_NAME, name, itemId)
        cursor.execute(command)
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(e)
        return e
    return name, " added"


def addSeenItem(name, seenAs, price, quantity, location, person, user=CONSTANTS.USER):
    ts = calendar.timegm(time.gmtime())
    try:
        command = "INSERT INTO %s VALUES (null, '%s', '%s', %d, %d, %d, '%s', '%s', 's')" \
                  % (SEEN_PRICE_TABLE_NAME, name, seenAs, price, quantity, ts, location, person, user)
        cursor.execute(command)
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(e)
        return e

    return name + " has been added, Price:"+str(price)

def deleteSeenItem(id):
    try:
        command = "DELETE from %s where _id  = %d" % (SEEN_PRICE_TABLE_NAME, id)
        cursor.execute(command)
        connection.commit()

    except sqlite3.IntegrityError as e:
        print(e)
        return e

def getAll(tableName):
    cursor.execute("SELECT _id, name, seenAs, price, quantity, date, location, person FROM "+tableName)
    return cursor.fetchall()
