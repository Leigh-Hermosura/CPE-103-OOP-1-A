from tkinter import *
import math

# notes for calculator:
# trigonometric equations should always end with ")" to work properly, else "Error"
# example: sin(30), cos(60), and so on.

# same goes for the square root function
# example: √25), √9), and so on.

def updateDisp(value):
    global expression
    expression += str(value)
    display.delete(0, END)
    display.insert(0, expression)

def clearDisp():
    global expression
    expression = ""
    display.delete(0, END)

def deleteDisp():
    global expression
    expression = expression[:-1]
    display.delete(0, END)
    display.insert(0, expression)

def evalExp():
    global expression
    try:
        expr = expression
        expr = expr.replace('sin(', 'math.sin(math.radians(')
        expr = expr.replace('cos(', 'math.cos(math.radians(')
        expr = expr.replace('tan(', 'math.tan(math.radians(')
        expr = expr.replace('√', 'math.sqrt(')
        expr = expr.replace('^', '**')
        expr = expr.replace('%', '/100')

        open_parens = expr.count('(')
        close_parens = expr.count(')')
        if open_parens > close_parens:
            expr += ')' * (open_parens - close_parens)

        result = eval(expr)

        display.delete(0, END)
        display.insert(0, str(result))
        expression = str(result)

    except Exception as e:
        display.delete(0, END)
        display.insert(0, "Error")
        expression = ""


root = Tk()
root.title('Calculator')
root.geometry('500x700')
frame = Frame(root,bg='lightblue')
frame.pack(fill=BOTH, expand=True, padx=10)

expression = ""

row1Frame = Frame(frame, bg='#A3CAE9')
row1Frame.grid(row=1, column=0, columnspan=4, sticky='nsew', pady=5)
row5Frame = Frame(frame, bg='#A3CAE9')
row5Frame.grid(row=5, column=0, columnspan=4, sticky='nsew', pady=5)

# button row 0
display = Entry(frame, font=("Arial", 30), justify='right', bg='lightblue', bd=20,)
display.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=3, padx=10)
display.configure(bg='#C2EFF1')

# button row 1
btnC = Button(row1Frame, text="CLR", font=("Arial", 30, 'bold'), command=clearDisp)
btnC.grid(column=0, row=0, sticky='nsew', pady=3)
btnDel = Button(row1Frame, text="DEL", font=("Arial", 30, 'bold'), command=deleteDisp)
btnDel.grid(column=1, row=0, sticky='nsew', pady=3)

# button row 2
btn7 = Button(frame, text="7", font=("Arial", 30, 'bold'), command=lambda: updateDisp(7))
btn7.grid(column=0, row=2, sticky='nsew', pady=5)
btn8 = Button(frame, text="8", font=("Arial", 30, 'bold'), command=lambda: updateDisp(8))
btn8.grid(column=1, row=2, sticky='nsew', pady=5)
btn9 = Button(frame, text="9", font=("Arial", 30, 'bold'), command=lambda: updateDisp(9))
btn9.grid(column=2, row=2, sticky='nsew', pady=5)
btnDiv = Button(frame, text="/", font=("Arial", 30, 'bold'), command=lambda: updateDisp("/"))
btnDiv.grid(column=3, row=2, sticky='nsew', pady=5)

# button row 3
btn4 = Button(frame, text="4", font=("Arial", 30, 'bold'), command=lambda: updateDisp(4))
btn4.grid(column=0, row=3, sticky='nsew', pady=5)
btn5 = Button(frame, text="5", font=("Arial", 30, 'bold'), command=lambda: updateDisp(5))
btn5.grid(column=1, row=3, sticky='nsew', pady=5)
btn6 = Button(frame, text="6", font=("Arial", 30, 'bold'), command=lambda: updateDisp(6))
btn6.grid(column=2, row=3, sticky='nsew', pady=5)
btnMulti = Button(frame, text="*", font=("Arial", 30, 'bold'), command=lambda: updateDisp("*"))
btnMulti.grid(column=3, row=3, sticky='nsew', pady=5)

# button row 4
btn1 = Button(frame, text="1", font=("Arial", 30, 'bold'), command=lambda: updateDisp(1))
btn1.grid(column=0, row=4, sticky='nsew', pady=5)
btn2 = Button(frame, text="2", font=("Arial", 30, 'bold'), command=lambda: updateDisp(2))
btn2.grid(column=1, row=4, sticky='nsew', pady=5)
btn3 = Button(frame, text="3", font=("Arial", 30, 'bold'), command=lambda: updateDisp(3))
btn3.grid(column=2, row=4, sticky='nsew', pady=5)
btnMinus = Button(frame, text="-", font=("Arial", 30, 'bold'), command=lambda: updateDisp("-"))
btnMinus.grid(column=3, row=4, sticky='nsew', pady=5)


# button row 5
btn0 = Button(row5Frame, text="0", font=("Arial", 30, 'bold'), command=lambda: updateDisp("0"))
btn0.grid(column=0, row=0, sticky='nsew', pady=5)
btnPoint = Button(row5Frame, text=".", font=("Arial", 30, 'bold'), command=lambda: updateDisp("."))
btnPoint.grid(column=1, row=0, sticky='nsew', pady=5)
btnAdd = Button(row5Frame, text="+", font=("Arial", 30, 'bold'), command=lambda: updateDisp("+"))
btnAdd.grid(column=2, row=0, sticky='nsew', pady=5)

# button row 6
btnLeftParentheses = Button(frame, text="(", font=("Arial", 30, 'bold'), command=lambda: updateDisp('('))
btnLeftParentheses.grid(column=0, row=6, sticky='nsew', pady=5)
btnRightParentheses = Button(frame, text=")", font=("Arial", 30, 'bold'), command=lambda: updateDisp(')'))
btnRightParentheses.grid(column=1, row=6, sticky='nsew', pady=5)
btnSqrt = Button(frame, text="√", font=("Arial", 30, 'bold'), command=lambda: updateDisp('√'))
btnSqrt.grid(column=2, row=6, sticky='nsew', pady=5)
btnModulus = Button(frame, text="%", font=("Arial", 30, 'bold'), command=lambda: updateDisp('%'))
btnModulus.grid(column=3, row=6, sticky='nsew', pady=5)

# button row 7
btnSin = Button(frame, text="sin(", font=("Arial", 30, 'bold'), command=lambda: updateDisp('sin('))
btnSin.grid(column=0, row=7, sticky='nsew', pady=5)
btnCos = Button(frame, text="cos(", font=("Arial", 30, 'bold'), command=lambda: updateDisp('cos('))
btnCos.grid(column=1, row=7, sticky='nsew', pady=5)
btnTan = Button(frame, text="tan(", font=("Arial", 30, 'bold'), command=lambda: updateDisp('tan('))
btnTan.grid(column=2, row=7, sticky='nsew', pady=5)
btnExp = Button(frame, text="Exp", font=("Arial", 30, 'bold'), command=lambda: updateDisp('^'))
btnExp.grid(column=3, row=7, sticky='nsew', pady=5)

# button row 8
btnEqual = Button(frame, text="=", font=("Arial", 30, 'bold'), command=evalExp)
btnEqual.grid(column=0, row=8, columnspan=4, sticky='nsew', pady=5)

# button configurations
for i in range(2):
    row1Frame.grid_columnconfigure(i, weight=1)
for i in range(3):
    row5Frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(9):
    frame.grid_rowconfigure(i, weight=1)

root.mainloop()
