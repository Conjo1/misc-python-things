"""QT5 python app to test a home made PIU pad (if it's based on a keyboard)"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from sys import exit, argv

class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.setFixedSize(476, 482)
        self.setWindowTitle("PIU Custom Pad Tester")
        self.setStyleSheet("background: rgb(0, 0, 0)")

        self.upleft = QLabel(self)
        self.upleft.setPixmap(QPixmap("images/upleft.png"))
        self.upleft.setScaledContents(True)
        self.upleft.setFixedSize(156,188)
        self.upleft.move(4,2)
        self.upleft.hide()

        self.upright = QLabel(self)
        self.upright.setPixmap(QPixmap("images/upright.png"))
        self.upright.setScaledContents(True)
        self.upright.setFixedSize(156,188)
        self.upright.move(316,2)
        self.upright.hide()

        self.center = QLabel(self)
        self.center.setPixmap(QPixmap("images/center.png"))
        self.center.setScaledContents(True)
        self.center.setFixedSize(156,156)
        self.center.move(160,162)
        self.center.hide()

        self.downleft = QLabel(self)
        self.downleft.setPixmap(QPixmap("images/downleft.png"))
        self.downleft.setScaledContents(True)
        self.downleft.setFixedSize(156,188)
        self.downleft.move(4,290)
        self.downleft.hide()

        self.downright = QLabel(self)
        self.downright.setPixmap(QPixmap("images/downright.png"))
        self.downright.setScaledContents(True)
        self.downright.setFixedSize(156,188)
        self.downright.move(316,290)
        self.downright.hide()
    
    def set_arrows(self, *args):
        self.arrows = [ord(i) for i in args]

    def keyPressEvent(self, e):
        if e.key() == self.arrows[0]:
            self.upleft.show()
        if e.key() == self.arrows[1]:
            self.upright.show()
        if e.key() == self.arrows[2]:
            self.center.show()
        if e.key() == self.arrows[3]:
            self.downleft.show()
        if e.key() == self.arrows[4]:
            self.downright.show()
    
    def keyReleaseEvent(self, e):
        if e.key() == self.arrows[0]:
            self.upleft.hide()
        if e.key() == self.arrows[1]:
            self.upright.hide()
        if e.key() == self.arrows[2]:
            self.center.hide()
        if e.key() == self.arrows[3]:
            self.downleft.hide()
        if e.key() == self.arrows[4]:
            self.downright.hide()
        

if __name__ == '__main__':
    arrows = argv[1:6]
    if not len(arrows):
        arrows = ["V","R","D","M","U"]
    app = QApplication([])
    window = MainWindow()
    window.set_arrows(*arrows)
    window.show()
    e = app.exec_()
    exit(e)