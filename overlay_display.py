import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from CONSTANTS import Point, Rectangle


class Overlay(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(Overlay, self).__init__()  # This has to be after QApplication(sys.argv)

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

    def updatePaint(self, points):
        def pointsToRec() -> Rectangle:
            if points is not None:
                print(points[0])
                print(points[2])
                return Rectangle(Point(points[0][0][0], points[0][0][1]), Point(points[2][0][0], points[2][0][1]))
            return Rectangle(Point(0, 0), Point(0, 0))

        self.itemBoarder = pointsToRec()
        self.app.processEvents()
        self.update()


    def paintEvent(self, event=None):
        def drawBoarders():
            # drawing the boarder clock wise ->
            rec = self.itemBoarder
            print("Boarder Rec: ", rec)
            painter.drawLine(rec.topLeft.x, rec.topLeft.y, rec.botRight.x, rec.topLeft.y)
            painter.drawLine(rec.botRight.x, rec.topLeft.y, rec.botRight.x, rec.botRight.y)
            painter.drawLine(rec.botRight.x, rec.botRight.y, rec.topLeft.x, rec.botRight.y)
            painter.drawLine(rec.topLeft.x, rec.botRight.y, rec.topLeft.x, rec.topLeft.y)
        print("PaintEvent")
        painter = QPainter(self)
        # Overlay Active Warning
        painter.setOpacity(1)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.setFont(QFont('Decorative', 50))
        painter.drawText(event.rect(), Qt.AlignLeft, "Overlay ACTIVE")

        drawBoarders()

        painter.drawLine(0, 0, 500, 500)





