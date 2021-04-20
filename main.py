import main_gui
import app_variables

from ParseTools import screen_scanner
from DebugTools import debug_display

app_variables.appRunning = True
gui = main_gui.MasterGui()
debugDisplayWindow = None
debugDisplayWindowName = "Debug Display"


def __closeDebugWindow():
    if debugDisplayWindow is not None:
        debugDisplayWindow.destroy()


while app_variables.appRunning:
    gui.mainWindow.update_idletasks()
    gui.mainWindow.update()

    if app_variables.gatherDataOn:
        # Starts gathering data from screen/monitor
        data = screen_scanner.getImage()
        if app_variables.isDebugWindowOn():
            # Displays image in real time with boundary boxes on 2nd screen
            if debugDisplayWindow is None:
                debugDisplayWindow = debug_display.Display(debugDisplayWindowName)
            # TODO draw around name box too
            debugDisplayWindow.display(data.get("rawImage"), data.get("targetRec"))
        else:
            __closeDebugWindow()
    else:
        __closeDebugWindow()

    # What do we do when main gui is closed
    if not app_variables.mainGuiRunning:
        __closeDebugWindow()
        # TODO Close all resources and do any config/data saves
        break
