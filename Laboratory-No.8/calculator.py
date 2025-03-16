from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='First number', fg='white', bg='orange')
        self.lbl2 = Label(win, text='Second number', fg='white', bg='orange')
        self.lbl3 = Label(win, text='Result', fg='white', bg='orange')

        self.t1 = Entry(bd=10, fg='white', bg='orange')
        self.t2 = Entry(bd=10, fg='white', bg='orange')
        self.t3 = Entry(bd=10, fg='white', bg='orange')

        self.btn1 = Button(win, text='Add', command=self.add, bg='orange', fg='white')
        self.btn2 = Button(win, text='Subtract', command=self.sub, bg='orange', fg='white')
        self.btn3 = Button(win, text='Multiply', command=self.mul, bg='orange', fg='white')
        self.btn4 = Button(win, text='Divide', command=self.div, bg='orange', fg='white')
        self.btn5 = Button(win, text='Clear', command=self.clr, bg='red', fg='white')

        self.btn2.bind('<Button-1>', self.sub)
        self.btn3.bind('<Button-1>', self.mul)
        self.btn4.bind('<Button-1>', self.div)
        self.btn5.bind('<Button-1>', self.clr)

        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=100)
        self.lbl3.place(x=100, y=150)
        self.t1.place(x=200, y=50)
        self.t2.place(x=200, y=100)
        self.t3.place(x=200, y=150)
        self.btn1.place(x=50, y=210)
        self.btn2.place(x=110, y=210)
        self.btn3.place(x=200, y=210)
        self.btn4.place(x=300, y=210)
        self.btn5.place(x=175, y= 275)


    def add(self):
        self.t3.delete(0, 'end')
        num1 = float(self.t1.get())
        num2 = float(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = float(self.t1.get())
        num2 = float(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def mul(self, event):
        self.t3.delete(0, 'end')
        num1 = float(self.t1.get())
        num2 = float(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def div(self, event):
        self.t3.delete(0, 'end')
        num1 = float(self.t1.get())
        num2 = float(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))

    def clr(self, event):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')


window=Tk()
mywin=MyWindow(window)
window.title('Along Malapitan Calculator')
window.geometry("400x350+10+10")
window.configure(bg='light green')
window.mainloop()
