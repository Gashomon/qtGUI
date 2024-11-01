import MyGUI
import sys
n = 10
blah = ''
m = [10]
hello = MyGUI.GUI
hello.widget.show()

def func1(p):
    out = p + 30
    return out
def func2():
    hello.status.label_2.setText(str(n))

def func3(p):
    p[0] = p[0] + 30

def func4():
    hello.status.label_2.setText(str(m[0]))

def func5(nonsense, p):
    out = p + 30    
    lol = nonsense
    return out


hello.control.pushButton_2.clicked.connect(lambda: func1(n))
hello.control.pushButton_5.clicked.connect(lambda: func2())
# hello.control.pushButton_2.clicked.connect(lambda: func3(m))
# hello.control.pushButton_5.clicked.connect(lambda: func4())
hello.control.pushButton_2.clicked.connect(lambda: func5(n))

hello.control.pushButton_3.clicked.connect(lambda: func1(n))
hello.control.pushButton_6.clicked.connect(lambda: func2())
# hello.control.pushButton_3.clicked.connect(lambda: func3(m))
# hello.control.pushButton_6.clicked.connect(lambda: func4())
hello.control.pushButton_3.clicked.connect(lambda: func5(n))

hello.control.pushButton_4.clicked.connect(lambda: func1(n))
hello.control.pushButton_7.clicked.connect(lambda: func2())
# hello.control.pushButton_4.clicked.connect(lambda: func3(m))
# hello.control.pushButton_7.clicked.connect(lambda: func4())
hello.control.pushButton_4.clicked.connect(lambda: func5(n))

print(n)
# n = func1(n)
func5(blah, n)
print(n)
sys.exit(hello.app.exec())