import main_gui
import app_variables
import overlay_display
from CONSTANTS import Rectangle, Point

from ParseTools import screen_scanner
from DebugTools import debug_display

app_variables.appRunning = True
gui = main_gui.MasterGui()
debugDisplayWindow = None
debugDisplayWindowName = "Debug Display"

# Test rectangle for overlay

overlay = None


def __closeDebugWindow():
    if debugDisplayWindow is not None:
        debugDisplayWindow.destroy()
def __closeApp():
    __closeDebugWindow()


while app_variables.appRunning:
    gui.mainWindow.update_idletasks()
    gui.mainWindow.update()

    if app_variables.gatherDataOn:
        # Starts gathering data from screen/monitor
        data = screen_scanner.getImage()

        if app_variables.isOverlayOn():
            if overlay is None:
                overlay = overlay_display.Overlay()
            overlay.updatePaint(data.get("targetRec"))

        if app_variables.isDebugWindowOn():
            # Displays image in real time with boundary boxes on 2nd screen
            if debugDisplayWindow is None:
                debugDisplayWindow = debug_display.Display(debugDisplayWindowName)
            # TODO draw around name box too
            debugDisplayWindow.display(data.get("rawImage"), data.get("targetRec"))
    else:
        __closeApp()

    # What do we do when main gui is closed
    if not app_variables.mainGuiRunning:
        __closeApp()
        # TODO Close all resources and do any config/data saves
        break
