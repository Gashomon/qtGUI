## Sample GUI from Qt Designer

show sample UI we've made for a multi-page/screen layout of a Path-Following Robot.

files include:
- .py file - the main code of each window / screen. graphics depend on the respective .ui file and also contains the functions for buttons and other inputs
- .ui file - the interface that can easily be used / manipulate through the Qt designer.

it hase five screens (confirmation UI, controls UI, main UI, status UI, password UI). The MyGUI.py serves as the main window as well and utilizes **QStackedWidget()** to select which among the five screens is currently displayed. It also contains the functions that needs to work with other screem's objects.

#### PySide 6 - Dependency
```
pip install pyside6
```
#### Logic
1. Different screens layouts are made and compiled with their own python files (main, confirm, password, control, status)
2. different screen layouts are compiled in the MyGUI.py within a single GUI class, importing a sub-class for each screen and their own methods. Can also access the layout items from other screens.
3. GUI Class creates the actual window and StackedWidget. Each sub-class gets its own Widget page and can be called which is active at the moment.
4. This can keep all the other widgets / screens active and working with each of their computations. Make sure no heavy lifting is done in any screen that may block or slow the whole system. 

*Note: Adding loops will halt the display functionality, use PySide6's built-in functions to handle threading.*

#### How to Run
1. Make sure Pyside6 is installed. 
2. Run MyGUI.py
3. Select any option in the Control Window
4. The Password Window will show. Clear the text and enter '0000' to proceed back to the Control Window