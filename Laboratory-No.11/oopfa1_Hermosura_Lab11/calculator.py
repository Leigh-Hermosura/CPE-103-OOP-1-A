from tkinter import *

def updateDisp(value):
    global expression
    expression += str(value)
    display.delete(0, END)
    display.insert(0, expression)

def clearDisp():
    global expression
    expression = ""
    display.delete(0, END)

def evalExp():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, END)
        display.insert(0, result)
        expression = result  # Allow chaining calculations
    except:
        display.delete(0, END)
        display.insert(0, "Error")
        expression = ""


root = Tk()
root.title('Calculator')
root.geometry('500x700')
frame = Frame(root,bg='lightblue')
frame.pack(fill=BOTH, expand=True, padx=10)

expression = ""

row5Frame = Frame(frame, bg='#A3CAE9')
row5Frame.grid(row=5, column=0, columnspan=4, sticky='nsew', pady=5)

# button row 0
display = Entry(frame, font=("Arial", 30), justify='right', bg='lightblue', bd=30,)
display.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=3, padx=10)
display.configure(bg='#C2EFF1')

# button row 1
btnC = Button(frame, text="C", font=("Arial", 30, 'bold'), command=clearDisp)
btnC.grid(column=0, row=1, columnspan=4, sticky='nsew', pady=3)

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
btnEqual = Button(frame, text="=", font=("Arial", 30, 'bold'), command=evalExp)
btnEqual.grid(column=0, row=6, columnspan=4, sticky='nsew', pady=5)

# button configurations
for i in range(3):
    row5Frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(7):
    frame.grid_rowconfigure(i, weight=1)

root.mainloop()
