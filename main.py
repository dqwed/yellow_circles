import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class DrawYellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        number = random.randint(1, 10)
        for i in range(number):
            r, g, b = self.select_color()
            qp.setPen(QPen(QColor(r, g, b)))
            qp.setBrush(QBrush(QColor(r, g, b), Qt.SolidPattern))
            diameter = random.randint(10, 200)
            qp.drawEllipse(random.randint(0, 800 - diameter), random.randint(0, 800 - diameter),
                           diameter, diameter)

    def select_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return red, green, blue


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dyc = DrawYellowCircles()
    dyc.show()
    sys.exit(app.exec())
