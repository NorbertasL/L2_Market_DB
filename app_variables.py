# Recording state
gatherDataOn = False

appRunning = False
mainGuiRunning = False

# User Settings
USER = "RedSpark"
TAKE_PIC_KEY = "c"

# Debug displaying
__isOverlayOn = False
def isOverlayOn():
    # I only want to display the overlay if we are gathering data or it will be blank and waist CPU power
    return __isOverlayOn and gatherDataOn


__isDebugWindowOn = True
def isDebugWindowOn():
    # I only want to display the window if we are gathering data or it will be blank
    return __isDebugWindowOn and gatherDataOn
