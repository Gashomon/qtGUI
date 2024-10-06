import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI,self).__init__()
        loader.load("main.ui",self)

app=QApplication(sys.argv)
mainwindow=MyGUI()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(768)
widget.setFixedWidth(1024)
widget.show()
sys.exit(app.exec_())