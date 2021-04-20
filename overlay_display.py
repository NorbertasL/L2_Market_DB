import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from CONSTANTS import Point, Rectangle


class Overlay(QMainWindow):
    def __init__(self):
        print("init Overlay")
        self.app = QApplication(sys.argv)
        super(Overlay, self).__init__()
        # Create the main window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)  # Click Trough
        # Makes Window stay on top
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.X11BypassWindowManagerHint)

        # Defining an empty rec
        self.itemBoarder = Rectangle(Point(0, 0), Point(0, 0))

        # Run the application
        self.showFullScreen()

    def update(self, rec: Rectangle = Rectangle(Point(0, 0), Point(0, 0))):
        self.app.processEvents()
        self.itemBoarder = rec

    def paintEvent(self, event=None):
        def drawBoarders():
            # drawing the boarder clock wise ->
            rec = self.itemBoarder
            painter.drawLine(rec.topLeft.x, rec.topLeft.y, rec.botRight.x, rec.topLeft.y)
            painter.drawLine(rec.botRight.x, rec.topLeft.y, rec.botRight.x, rec.botRight.y)
            painter.drawLine(rec.botRight.x, rec.botRight.y, rec.topLeft.x, rec.botRight.y)
            painter.drawLine(rec.topLeft.x, rec.botRight.y, rec.topLeft.x, rec.topLeft.y)

        painter = QPainter(self)

        # Paining a white rectangle of white colour but making setting it's Opacity to 0 to make it trough
        painter.setOpacity(0.0)
        painter.setBrush(Qt.white)
        painter.setPen(QPen(Qt.white))
        painter.drawRect(self.rect())

        # Painting Item Boarder
        painter.setOpacity(1)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        drawBoarders()

        # Overlay Active Warning
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.setFont(QFont('Decorative', 50))
        painter.drawText(event.rect(), Qt.AlignLeft, "Overlay ACTIVE")



    def destroy(self):
        # TODO
        return
