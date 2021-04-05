# L2 Market DB(Local)

A python app the scan L2(Linage 2 Classic) screen and finds items that are being 
sold. Adds item info to a local database(in future a cloud one too) with 
details on items name, price, sell location, quantity and seller name. 
This app will be used to track price change trends and just as a general 
tool to be able to see previous item prices.

## Dependencies
* [Sqlite3](https://www.sqlite.org/index.html) 
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* Win32gui
* PIL - ImageGrab
* cv2
* numpy
* ~~pynput.keyboard~~ 
  * Switched to [keyboard](https://github.com/boppreh/keyboard)
  * Will probably need to develop my own low lvl key listener.
* [Tesseract OCR](https://github.com/tesseract-ocr/)

## Know Issues
* Focus window and key events.
    * When focused on the game window, the app does not see key events, because
    l2 client suppresses them.
      
## Future Features
* Optimise screen capture size my scanning for in-game object-(corners).
    * This will reduce the amount of data the OCR has to goe trough and thus
    speeding it up.
      
* Reduce the need to press capture keybinding for each item.
    * The screen will be constantly recorded and when a new item is detected it
    will scan its data.
      
* Better GUI
    * Current one is very basic, and an eyesore.
    
* Online DB integration.
* Graphs.
    * Everyone like graphs of price fluctuation.