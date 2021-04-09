import time
import tkinter as tk
from datetime import datetime
from tkinter import ttk
import db_conn
from keyboard_helper import KeyListener


window = tk.Tk("L2Reborn")
window.title("L2Reborn Market Data")
window.geometry("1100x400")

keyListener = KeyListener()
exitApp = False

def addNewItem(name, itemId=-1):
    db_conn.addNewItemName(name, itemId)


# Using this to time click interval to prevent spam clicking
lastTime = None


def addNewPrice(name, seenAs, price, loc, quan, person):
    timeNow = time.time()
    global lastTime
    global processLabel

    if not name:
        processLabel.config(text="Name is empty", fg="red")
        return
    if not seenAs:
        processLabel.config(text="Seen as is empty", fg="red")
        return
    if price <= 0:
        processLabel.config(text="Bad Price", fg="red")
        return

    if lastTime is None or timeNow - lastTime > 2:
        returnValue = db_conn.addSeenItem(name, seenAs, price, quan, loc, person)
        lastTime = timeNow
        processLabel.config(text=returnValue, fg="green")
        updateList()
    else:
        print("Don't spam")
        processLabel.config(text="Don't spam the button", fg="red")


def openItemNameListWindow():
    itemListWindow = tk.Toplevel()
    itemListWindow.title("Item Window")
    itemListWindow.geometry("500x100")

    itemNameText = tk.StringVar()
    mat_name_label = tk.Label(itemListWindow, text="Name:", font=('bold', 14), pady=20)
    mat_name_label.grid(row=0, column=0, sticky='W')
    mat_name_entry = tk.Entry(itemListWindow, textvariable=itemNameText)
    mat_name_entry.grid(row=0, column=1, sticky='W', padx=20)

    itemIdText = tk.IntVar(value=-1)
    mat_id_label = tk.Label(itemListWindow, text="Item ID:", font=('bold', 14))
    mat_id_label.grid(row=0, column=2, sticky='W')
    mat_id_entry = tk.Entry(itemListWindow, textvariable=itemIdText, )
    mat_id_entry.grid(row=0, column=3, sticky='W')

    addBtn = tk.Button(itemListWindow, text="Add",
                       command=lambda: addNewItem(itemNameText.get(), itemIdText.get()))
    addBtn.grid(row=1, column=0)


# Top Menu Bar
my_menu = tk.Menu(window)
window.config(menu=my_menu)
add_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Add", menu=add_menu)
add_menu.add_command(label="New Item", command=addNewItem)
add_menu.add_command(label="Item List", command=openItemNameListWindow)


# New item entry widgets
itemNameText = tk.StringVar()
itemNameLabel = tk.Label(window, text="Name:", font=('bold', 14))
itemNameLabel.grid(row=0, column=0, sticky='W', padx=(50, 0))
itemNameEntry = tk.Entry(window, textvariable=itemNameText)
itemNameEntry.grid(row=0, column=1, sticky='W', padx=20)

seenAsText = tk.StringVar(value="Sell")
seenAsLabel = tk.Label(window, text="Seen As:", font=('bold', 14))
seenAsLabel.grid(row=0, column=2, sticky="W")
seenAsEntry = tk.Entry(window, textvariable=seenAsText)
seenAsEntry.grid(row=0, column=3, sticky="W", padx=20)

locationText = tk.StringVar(value="Giran")
locationLabel = tk.Label(window, text="Loc:", font=('bold', 14), )
locationLabel.grid(row=0, column=4, sticky="W", )
locationEntry = tk.Entry(window, textvariable=locationText)
locationEntry.grid(row=0, column=5, sticky="W")

priceNameText = tk.IntVar(value=-1)
priceNameLabel = tk.Label(window, text="Price:", font=('bold', 14))
priceNameLabel.grid(row=1, column=0, sticky='W', padx=(50, 0))
priceNameEntry = tk.Entry(window, textvariable=priceNameText)
priceNameEntry.grid(row=1, column=1, sticky='W', padx=20)

quanText = tk.IntVar(value=1)
quanLabel = tk.Label(window, text="Quantity:", font=('bold', 14))
quanLabel.grid(row=1, column=2, sticky="W")
quanEntry = tk.Entry(window, textvariable=quanText)
quanEntry.grid(row=1, column=3, sticky="W", padx=20)

personText = tk.StringVar()
personLabel = tk.Label(window, text="Person:", font=('bold', 14))
personLabel.grid(row=1, column=4, sticky="W")
personEntry = tk.Entry(window, textvariable=personText)
personEntry.grid(row=1, column=5, sticky="W")

addBtn = tk.Button(window, text="Add", height=1, width=80,
                   command=lambda: addNewPrice(itemNameText.get(), seenAsText.get(), priceNameText.get(),
                                               locationText.get(), quanText.get(), personText.get()))
addBtn.grid(row=3, column=0, columnspan=6)

processLabel = tk.Label(window)
processLabel.grid(row=4, column=2, columnspan=2)

# Tree view
myTree = ttk.Treeview(window)

# Defining Columns
myTree['columns'] = ("ID", "Name", "Seen As", "Price", "Quantity", "Date", "Location", "Person")

# Formatting columns
myTree.column("#0", width=0, stretch="no")
myTree.column("ID", width=0, stretch="no")
myTree.column("Name", anchor="w")
myTree.column("Seen As", width=60, anchor="w")
myTree.column("Price", width=200, anchor="c")
myTree.column("Quantity", width=200, anchor="c")
myTree.column("Date", anchor="c")
myTree.column("Location", width=100, anchor="c")
myTree.column("Person", width=100, anchor="c")


# Headings
myTree.heading("#0", text="")
myTree.heading("ID", text="ID")
myTree.heading("Name", text="Name")
myTree.heading("Seen As", text="Seen As")
myTree.heading("Price", text="Price")
myTree.heading("Quantity", text="Quantity")
myTree.heading("Date", text="Date")
myTree.heading("Location", text="Location")
myTree.heading("Person", text="Person")

myTree.grid(row=5, column=0, columnspan=6, padx=(20, 0))

# using this to delete item from list and DB
def treeRightClick(event):
    column = myTree.identify_column(event.x)
    row = myTree.identify_row(event.y)
    print("Right Click on Column:", column, " Row:", row)
    itemId = myTree.item(myTree.focus())['values'][0]
    print("ID is: ", itemId)
    # TODO add some kind of confirmation window
    db_conn.deleteSeenItem(itemId)
    updateList()


def treeLeftClick(event):
    column = myTree.identify_column(event.x)
    row = myTree.identify_row(event.y)
    print("Left Click on Column:", column, " Row:", row)


myTree.bind("<Button-3>", treeRightClick)
myTree.bind("<Button-1>", treeLeftClick)

def updateList():
    myTree.delete(*myTree.get_children())
    data = getListData()
    count = 0
    for record in data:
        myTree.insert(parent='', index='end', iid=count, text='', values=(record[0],  # id(invisible)
                                                                          record[1],  # name
                                                                          record[2],  # seenAs
                                                                          record[3],  # price
                                                                          record[4],  # quantity
                                                                          datetime.fromtimestamp(int(record[5])),  # date
                                                                          record[6],  # location
                                                                          record[7]))   # person
        count += 1
def getListData():
    data = db_conn.getAll(db_conn.SEEN_PRICE_TABLE_NAME)
    data.reverse()
    return data
def onClose():
    global keyListener
    global exitApp
    keyListener.stop()
    exitApp = True


window.protocol("WM_DELETE_WINDOW", onClose)
updateList()
while not exitApp:
    window.update_idletasks()
    window.update()
