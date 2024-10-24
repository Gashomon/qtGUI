import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader

from main import Ui_MainWindow as mainUi
from control import Ui_MainWindow as ctrlUi
from password import Ui_MainWindow as passUi
from status import Ui_MainWindow as statUi

loader = QUiLoader()

class MainUI(QMainWindow, mainUi):
    def __init__(self):
        super(MainUI,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gocmd)
        
    def gocmd(self):
        widget.setCurrentIndex(1)

class ControlUI(QMainWindow, ctrlUi):
    def __init__(self):
        super(ControlUI,self).__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.fetch)
        self.pushButton_3.clicked.connect(self.deliver)
        self.pushButton_4.clicked.connect(self.retrieve)
        self.pushButton_5.clicked.connect(self.rundel)
        self.pushButton_6.clicked.connect(self.runfec)
        self.pushButton_7.clicked.connect(self.runret)
        self.stackedWidget.hide()

    def fetch(self):
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.show()
    def deliver(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget.show()

    def retrieve(self):
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget.show()

    def runfec(self):
        status.display("FETCHING...")
        self.comboBox_4
        self.comboBox_5

    def rundel(self):
        status.display("DELIVERING...")
        self.comboBox_6
        self.comboBox_7

    def runret(self):
        status.display("RETRIEVING...")
        self.comboBox_8
        self.comboBox_9

class StatusUI(QMainWindow, statUi):
    def __init__(self):
        super(StatusUI,self).__init__()
        self.setupUi(self)
    def display(self, text):
        widget.setCurrentIndex(2)
        self.label_2.setText(text)

class PasswordUI(QMainWindow, passUi):

    passcode = '0000'
    def __init__(self):
        super(PasswordUI,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.addnum('1'))
        self.pushButton_2.clicked.connect(lambda: self.addnum('2'))
        self.pushButton_3.clicked.connect(lambda: self.addnum('3'))
        self.pushButton_4.clicked.connect(lambda: self.addnum('4'))
        self.pushButton_5.clicked.connect(lambda: self.addnum('5'))
        self.pushButton_6.clicked.connect(lambda: self.addnum('6'))
        self.pushButton_7.clicked.connect(lambda: self.addnum('7'))
        self.pushButton_8.clicked.connect(lambda: self.addnum('8'))
        self.pushButton_9.clicked.connect(lambda: self.addnum('9'))
        self.pushButton_10.clicked.connect(lambda: self.addnum('0'))

        self.pushButton_11.clicked.connect(self.verify)
        self.pushButton_12.clicked.connect(self.backspc)
        self.pushButton_13.clicked.connect(self.reset)

    def addnum(self, num):
        currText = self.label_3.text()
        self.label_3.setText(currText + num)

    def reset(self):
        self.label_3.setText('')
        
    def verify(self):
        input = self.label_3.text()
        if input == self.passcode:
            self.label_2.setText('Success')
        else:
            self.label_2.setText('Wrong Passcode. Try Again')
    
    def backspc(self):
        newText = self.label_3.text()[:-1]
        self.label_3.setText(newText)



app=QApplication(sys.argv)

main=MainUI()
control = ControlUI()
status = StatusUI()
password =PasswordUI()

widget=QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.addWidget(control)
widget.addWidget(status)
widget.addWidget(password)

widget.setFixedHeight(600)
widget.setFixedWidth(800)

widget.show()



sys.exit(app.exec_())