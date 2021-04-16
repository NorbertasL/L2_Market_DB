import tkinter



mainWindow = tkinter.Tk()

def openMainWindow():

    mainWindow.title("L2Reborn Market Data")
    mainWindow.geometry("1100x400")

    # Top Menu Bar
    my_menu = tkinter.Menu(mainWindow)
    mainWindow.config(menu=my_menu)
    add_menu = tkinter.Menu(my_menu)
    my_menu.add_cascade(label="Add", menu=add_menu)
    add_menu.add_command(label="Item List", command=openItemGui)
    #self.add_menu.add_command(label="Item List", command=self.mainClass.openItemNameListWindow)

def openItemGui():
    itemListWindow = tkinter.Toplevel()
    itemListWindow.title("Item Window")
    itemListWindow.geometry("500x100")

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

    def addNewItem():
        return
