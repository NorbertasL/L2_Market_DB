# Py libraries
import tkinter
from tkinter import ttk
from datetime import datetime

# Personal libraries
from tkinter.messagebox import askyesno

import app_variables
import db_conn
from DebugTools.debug_log import logGreyImgData
from keyboard_helper import KeyListener


class MasterGui:
    def __init__(self):
        def onClose():
            # Closing the gui properly
            app_variables.mainGuiRunning = False
            self.keyListener.stop()
            self.mainWindow.destroy()
            return

        app_variables.mainGuiRunning = True

        # Initialising key listener
        self.keyListener = KeyListener()

        # Initial window settings
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("L2Reborn Market Data")
        self.mainWindow.geometry("1100x400")
        self.mainWindow.protocol("WM_DELETE_WINDOW", onClose)

        # Tree view
        self.myTree = ttk.Treeview(self.mainWindow)

        # Calling window setup methods
        self._setUpMainWindow(self.mainWindow, self.myTree)

    @staticmethod   # static for now
    def _setUpMainWindow(mainWindow, myTree):
        def updateList():
            myTree.delete(*myTree.get_children())
            data = getListData()
            count = 0
            for record in data:
                myTree.insert(parent='', index='end', iid=count, text='', values=(record[0],  # id(invisible)
                                                                                  record[1],  # name
                                                                                  record[2],  # seenAs
                                                                                  f'{record[3]:,}',  # price
                                                                                  f'{record[4]:,}',  # quantity
                                                                                  datetime.fromtimestamp(
                                                                                      int(record[5])),  # date
                                                                                  record[6],  # location
                                                                                  record[7]))  # person
                count += 1

        def getListData():
            data = db_conn.getAll(db_conn.SEEN_PRICE_TABLE_NAME)
            data.reverse()
            return data
        # Top Menu
        my_menu = tkinter.Menu(mainWindow)
        mainWindow.config(menu=my_menu)
        add_menu = tkinter.Menu(my_menu)
        my_menu.add_cascade(label="Add", menu=add_menu)
        add_menu.add_command(label="Item List", command=lambda: ItemListGui())

        # New item entry widgets
        itemNameText = tkinter.StringVar()
        itemNameLabel = tkinter.Label(mainWindow, text="Name:", font=('bold', 14))
        itemNameLabel.grid(row=0, column=0, sticky='W', padx=(50, 0))
        itemNameEntry = tkinter.Entry(mainWindow, textvariable=itemNameText)
        itemNameEntry.grid(row=0, column=1, sticky='W', padx=20)

        seenAsText = tkinter.StringVar(value="Sell")
        seenAsLabel = tkinter.Label(mainWindow, text="Seen As:", font=('bold', 14))
        seenAsLabel.grid(row=0, column=2, sticky="W")
        seenAsEntry = tkinter.Entry(mainWindow, textvariable=seenAsText)
        seenAsEntry.grid(row=0, column=3, sticky="W", padx=20)

        locationText = tkinter.StringVar(value="Giran")
        locationLabel = tkinter.Label(mainWindow, text="Loc:", font=('bold', 14), )
        locationLabel.grid(row=0, column=4, sticky="W", )
        locationEntry = tkinter.Entry(mainWindow, textvariable=locationText)
        locationEntry.grid(row=0, column=5, sticky="W")

        priceNameText = tkinter.IntVar(value=-1)
        priceNameLabel = tkinter.Label(mainWindow, text="Price:", font=('bold', 14))
        priceNameLabel.grid(row=1, column=0, sticky='W', padx=(50, 0))
        priceNameEntry = tkinter.Entry(mainWindow, textvariable=priceNameText)
        priceNameEntry.grid(row=1, column=1, sticky='W', padx=20)

        quanText = tkinter.IntVar(value=1)
        quanLabel = tkinter.Label(mainWindow, text="Quantity:", font=('bold', 14))
        quanLabel.grid(row=1, column=2, sticky="W")
        quanEntry = tkinter.Entry(mainWindow, textvariable=quanText)
        quanEntry.grid(row=1, column=3, sticky="W", padx=20)

        personText = tkinter.StringVar()
        personLabel = tkinter.Label(mainWindow, text="Person:", font=('bold', 14))
        personLabel.grid(row=1, column=4, sticky="W")
        personEntry = tkinter.Entry(mainWindow, textvariable=personText)
        personEntry.grid(row=1, column=5, sticky="W")

        # Add data to DB btn
        def addNewPrice(name, seenAs, price, loc, quan, person):
            if not name:
                processLabel.config(text="Name is empty", fg="red")
                return
            if not seenAs:
                processLabel.config(text="Seen as is empty", fg="red")
                return
            if price <= 0:
                processLabel.config(text="Bad Price", fg="red")
                return

            # TODO add a same item check
            returnValue = db_conn.addSeenItem(name, seenAs, price, quan, loc, person)
            processLabel.config(text=returnValue, fg="green")
            updateList()

        addBtn = tkinter.Button(mainWindow, text="Add", height=1, width=80,
                                command=lambda: addNewPrice(itemNameText.get(), seenAsText.get(), priceNameText.get(),
                                                            locationText.get(), quanText.get(), personText.get()))
        addBtn.grid(row=3, column=1, columnspan=6)

        # Add record btn
        def keyListenToggle():
            btnStates = ["Start Key Listen", "Recording..."]
            if keyListenBtn['text'] == btnStates[0]:
                app_variables.gatherDataOn = True
                keyListenBtn.config(text=btnStates[1], fg="red")
            else:
                app_variables.gatherDataOn = False
                keyListenBtn.config(text=btnStates[0], fg="black")

        keyListenBtn = tkinter.Button(mainWindow, text="Start Key Listen", height=1, width=15, command=keyListenToggle)
        keyListenBtn.grid(row=3, column=0, columnspan=1)

        processLabel = tkinter.Label(mainWindow)
        processLabel.grid(row=4, column=2, columnspan=2)

        # Tree view for display DB data
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

        # Tree manipulation via mouse

        # Deleting data
        def treeRightClick(event):
            column = myTree.identify_column(event.x)
            row = myTree.identify_row(event.y)
            print("Right Click on Column:", column, " Row:", row)
            # Only deleting item if i click the same focused row with a right click
            if myTree.focus() == row:
                # TODO add some kind of confirmation window
                itemId = myTree.item(myTree.focus())['values'][0]
                db_conn.deleteSeenItem(itemId)
                updateList()

        def treeLeftClick(event):
            # This will probably not be used
            column = myTree.identify_column(event.x)
            row = myTree.identify_row(event.y)
            print("Left Click on Column:", column, " Row:", row)
            if row == "":
                print("Header click")

        def treeDoubleLeftClick(event):
            # should open a detailed item window where i can edit item parameters.
            column = myTree.identify_column(event.x)
            row = myTree.identify_row(event.y)
            print("2x Left Click on Column:", column, " Row:", row)

        myTree.bind("<Button-3>", treeRightClick)
        myTree.bind("<Button-1>", treeLeftClick)
        myTree.bind("<Double-1>", treeDoubleLeftClick)

        # calling updateList() after window setup to populate the list view
        updateList()

    @staticmethod
    def openIsThisNewItemWindow(itemData, croppedImgs):
        window = tkinter.Toplevel()
        window.wm_attributes("-topmost", 1)
        window.title("Is This New?")
        window.geometry("500x500")

        itemNameText = tkinter.StringVar()
        name_label = tkinter.Label(window, text="Name:", font=('bold', 14), pady=20)
        name_label.grid(row=0, column=0, sticky='W')
        name_entry = tkinter.Entry(window, textvariable=itemNameText)
        itemNameText.set(itemData[1])
        name_entry.grid(row=0, column=1, sticky='W', padx=20)

        sellerNameText = tkinter.StringVar()
        seller_label = tkinter.Label(window, text="Seller Name:", font=('bold', 14), pady=20)
        seller_label.grid(row=1, column=0, sticky='W')
        seller_entry = tkinter.Entry(window, textvariable=sellerNameText)
        sellerNameText.set(itemData[0])
        seller_entry.grid(row=1, column=1, sticky='W', padx=20)

        seenAsText = tkinter.StringVar()
        seenAs_label = tkinter.Label(window, text="Seen As:", font=('bold', 14), pady=20)
        seenAs_label.grid(row=1, column=2, sticky='W')
        seenAs_entry = tkinter.Entry(window, textvariable=seenAsText)
        seenAsText.set(itemData[4])
        seenAs_entry.grid(row=1, column=3, sticky='W', padx=20)

        priceText = tkinter.StringVar()
        price_label = tkinter.Label(window, text="price:", font=('bold', 14), pady=20)
        price_label.grid(row=2, column=0, sticky='W')
        price_entry = tkinter.Entry(window, textvariable=priceText)
        priceText.set(itemData[3])
        price_entry.grid(row=2, column=1, sticky='W', padx=20)

        quantityText = tkinter.StringVar()
        quantity_label = tkinter.Label(window, text="Quantity:", font=('bold', 14), pady=20)
        quantity_label.grid(row=2, column=2, sticky='W')
        quantity_entry = tkinter.Entry(window, textvariable=quantityText)
        quantityText.set(itemData[2])
        quantity_entry.grid(row=2, column=3, sticky='W', padx=20)

        addBtn = tkinter.Button(window, text="Add New Item",
                                command=lambda: addNewItem(itemNameText.get()))
        addBtn.grid(row=3, column=0)

        addBtn = tkinter.Button(window, text="Save Debug",
                                command=lambda: saveDebug())
        addBtn.grid(row=3, column=1)

        def saveDebug():
            logGreyImgData(croppedImgs[0], croppedImgs[1], force=True)







class ItemListGui:
    def __init__(self):
        print("item GUI")
        self.itemListWindow = tkinter.Toplevel()
        self.itemListWindow.title("Item Window")
        self.itemListWindow.geometry("500x100")
        self.__setUpItemGui(self.itemListWindow)

    @staticmethod  # static for now
    def __setUpItemGui(itemListWindow):

        itemNameText = tkinter.StringVar()
        mat_name_label = tkinter.Label(itemListWindow, text="Name:", font=('bold', 14), pady=20)
        mat_name_label.grid(row=0, column=0, sticky='W')
        mat_name_entry = tkinter.Entry(itemListWindow, textvariable=itemNameText)
        mat_name_entry.grid(row=0, column=1, sticky='W', padx=20)

        itemIdText = tkinter.IntVar(value=-1)
        mat_id_label = tkinter.Label(itemListWindow, text="Item ID:", font=('bold', 14))
        mat_id_label.grid(row=0, column=2, sticky='W')
        mat_id_entry = tkinter.Entry(itemListWindow, textvariable=itemIdText, )
        mat_id_entry.grid(row=0, column=3, sticky='W')

        addBtn = tkinter.Button(itemListWindow, text="Add",
                                command=lambda: addNewItem(itemNameText.get(), itemIdText.get()))
        addBtn.grid(row=1, column=0)

def addNewItem(name, itemId):
    db_conn.addNewItemName(name, itemId)
