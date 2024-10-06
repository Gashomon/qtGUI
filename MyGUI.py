import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader

from main import Ui_MainWindow as mainUi
from control import Ui_MainWindow as ctrl
from password import Ui_MainWindow as pss
from status import Ui_MainWindow as stat

loader = QUiLoader()

class MainUI(QMainWindow, mainUi):
    def __init__(self):
        super(MainUI,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gocmd)
    def gocmd(self):
        widget.setCurrentIndex(1)

class ControlUI(QMainWindow, ctrl):
    def __init__(self):
        super(ControlUI,self).__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.fetch)
        self.pushButton_2.clicked.connect(self.deliver)
        self.pushButton_2.clicked.connect(self.retrieve)
        self.pushButton_2.clicked.connect(self.runfec)
        self.pushButton_2.clicked.connect(self.rundel)
        self.pushButton_2.clicked.connect(self.runret)

    def fetch(self):
        widget.setCurrentIndex(0)
    def deliver(self):
        widget.setCurrentIndex(0)
    def retrieve(self):
        widget.setCurrentIndex(0)
    def runfec(self):
        widget.setCurrentIndex(0)
        self.comboBox_4
        self.comboBox_5
    def rundel(self):
        widget.setCurrentIndex(0)
        self.comboBox_6
        self.comboBox_7
    def runret(self):
        widget.setCurrentIndex(0)
        self.comboBox_8
        self.comboBox_9

class StatusUI(QMainWindow, stat):
    def __init__(self):
        super(StatusUI,self).__init__()
        self.setupUi(self)

class PasswordUI(QMainWindow, pss):
    def __init__(self):
        super(PasswordUI,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.gocmd)
    def gocmd(self):
        widget.setCurrentIndex(0)

app=QApplication(sys.argv)

mainwindow=MainUI()
screen = ControlUI()

widget=QtWidgets.QStackedWidget()

widget.addWidget(mainwindow)
widget.addWidget(screen)

widget.setFixedHeight(800)
widget.setFixedWidth(600)

widget.show()



sys.exit(app.exec_())