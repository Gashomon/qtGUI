import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("main.ui",self)
        self.pushButton.clicked.connect(self.some)
    
    def some(self):
        widget.setCurrentIndex(1)

class MyGUI2(QMainWindow):
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("control.ui",self)
        self.pushButton.clicked.connect(self.some)
    
    def some(self):
        widget.setCurrentIndex(1)

app=QApplication(sys.argv)
mainwindow=MyGUI()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(mainwindow)
widget.setFixedHeight(768)
widget.setFixedWidth(1024)
widget.show()
sys.exit(app.exec())