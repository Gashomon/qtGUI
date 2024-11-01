import MyGUI
import sys

n = 10

m = [10]

blah, o = '', 10

class trial():
    n = 90
    # def p(self):
        
x = trial()

hello = MyGUI.GUI
hello.widget.show()



# common code, not passing
def func1(p):
    out = p + 30
    return out

def func2():
    hello.status.label_2.setText(str(n))

# pass as list, passing
def func3(p):
    p[0] = p[0] + 30

def func4():
    hello.status.label_2.setText(str(m[0]))

# pass as tuple, not passing
def func5(nonsense, p):
    nonsense = 'pop'
    p = p + 30 
    return nonsense, p

def func6():
    hello.status.label_2.setText(str(o))

# pass as class, passing
def func7(cl):
    cl.n = cl.n + 20

def func8(cl):
    hello.status.label_2.setText(str(cl.n))


# hello.control.pushButton_2.clicked.connect(lambda: func1(n))
# hello.control.pushButton_5.clicked.connect(lambda: func2())
# hello.control.pushButton_2.clicked.connect(lambda: func3(m))
# hello.control.pushButton_5.clicked.connect(lambda: func4())
# hello.control.pushButton_2.clicked.connect(lambda: func5(blah, o))
# hello.control.pushButton_5.clicked.connect(lambda: func6())
hello.control.pushButton_2.clicked.connect(lambda: func7(x))
hello.control.pushButton_5.clicked.connect(lambda: func8(x))

# hello.control.pushButton_3.clicked.connect(lambda: func1(n))
# hello.control.pushButton_6.clicked.connect(lambda: func2())
# hello.control.pushButton_3.clicked.connect(lambda: func3(m))
# hello.control.pushButton_6.clicked.connect(lambda: func4())
# hello.control.pushButton_3.clicked.connect(lambda: func5(blah, o))
# hello.control.pushButton_6.clicked.connect(lambda: func6())
hello.control.pushButton_3.clicked.connect(lambda: func7(x))
hello.control.pushButton_6.clicked.connect(lambda: func8(x))

# hello.control.pushButton_4.clicked.connect(lambda: func1(n))
# hello.control.pushButton_7.clicked.connect(lambda: func2())
# hello.control.pushButton_4.clicked.connect(lambda: func3(m))
# hello.control.pushButton_7.clicked.connect(lambda: func4())
# hello.control.pushButton_4.clicked.connect(lambda: func5(blah, o))
# hello.control.pushButton_7.clicked.connect(lambda: func6())
hello.control.pushButton_4.clicked.connect(lambda: func7(x))
hello.control.pushButton_7.clicked.connect(lambda: func8(x))

print(n)
# n = func1(n)
# l = func5(blah, o)
# print(l)
sys.exit(hello.app.exec())