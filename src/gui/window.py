import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 800)
        self.setWindowTitle("BetterPortfolio ^v^v")
        self.labels = dict()
        self.buttons = dict()
        self.init_ui()

    def init_ui(self):
        pass

    def update(self):
        for _, l in self.labels:
            l:QtWidgets.QLabel
            l.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

