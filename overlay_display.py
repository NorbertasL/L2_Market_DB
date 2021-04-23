import sys

import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
        self.recLines = None

        # Run the application
        self.showFullScreen()

    def updatePaint(self, points):
        self.recLines = points
        self.app.processEvents()
        self.update()

    def paintEvent(self, event=None):
        painter = QPainter(self)
        # Overlay Active Warning
        painter.setOpacity(1)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.setFont(QFont('Decorative', 50))
        painter.drawText(event.rect(), Qt.AlignLeft, "Overlay ACTIVE")

        if self.recLines is not None:

            painter.setPen(QPen(Qt.green, 1, Qt.SolidLine))
            print("RecLines:", self.recLines)
            print("RecArea:", cv2.contourArea(self.recLines))
            print("Array", self.recLines[3][0][0])
            painter.drawLine(self.recLines[0][0][0], self.recLines[0][0][1], self.recLines[1][0][0], self.recLines[1][0][1])
            painter.drawLine(self.recLines[1][0][0], self.recLines[1][0][1], self.recLines[2][0][0], self.recLines[2][0][1])
            painter.drawLine(self.recLines[2][0][0], self.recLines[2][0][1], self.recLines[3][0][0], self.recLines[3][0][1])
            painter.drawLine(self.recLines[3][0][0], self.recLines[3][0][1], self.recLines[0][0][0], self.recLines[0][0][1])








