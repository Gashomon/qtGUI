import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader

from main import Ui_MainWindow as mainUi
from control import Ui_MainWindow as scrn2

loader = QUiLoader()

class MyGUI(QMainWindow, mainUi):
    def __init__(self):
        super(MyGUI,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gocmd)
    def gocmd(self):
        widget.setCurrentIndex(1)

class screen2(QMainWindow, scrn2):
    def __init__(self):
        super(screen2,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.gocmd)
    def gocmd(self):
        widget.setCurrentIndex(0)

app=QApplication(sys.argv)
mainwindow=MyGUI()
screen = screen2()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(screen)
widget.setFixedHeight(768)
widget.setFixedWidth(1024)
widget.show()
sys.exit(app.exec_())