## Sample GUI from Qt Designer

show sample UI we've made for a multi-page/screen layout of a Path-Following Robot.

files include:
- .py file - the main code of each window / screen. graphics depend on the respective .ui file and also contains the functions for buttons and other inputs
- .ui file - the interface that can easily be used / manipulate through the Qt designer.

it hase five screens (confirmation UI, controls UI, main UI, status UI, password UI). The MyGUI.py serves as the main window as well and utilizes **QStackedWidget()** to select which among the five screens is currently displayed. It also contains the functions that needs to work with other screem's objects.

### Dependencies
#### PySide 6
```
pip install pyside6
```