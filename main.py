import main_gui
import app_variables

app_variables.appRunning = True
gui = main_gui.MasterGui()
while app_variables.appRunning:
    gui.mainWindow.update_idletasks()
    gui.mainWindow.update()

    # What do we do when main gui is closed
    if not app_variables.mainGuiRunning:
        # TODO Close all resources and do any config/data saves
        break
