from tkinter import *

win = Tk()
win.title("Using grid manager")
win.geometry("420x250")

txtfld1 = Entry(win,justify="center", bg='black', fg='white')
txtfld1.grid(column=0, row=0, padx=5)
txtfld1.insert(END, "BLACK")

txtfld2 = Entry(win,justify="center", bg='blue', fg='orange')
txtfld2.grid(column=1, row=0, padx=5)
txtfld2.insert(END, "BLUE")

txtfld3 = Entry(win,justify="center", bg='purple', fg='green')
txtfld3.grid(column=2, row=0, padx=5)
txtfld3.insert(END, "PURPLE")

txtfld4 = Entry(win,justify="center", bg='#09A876', fg='red')
txtfld4.grid(column=0, row=2, padx=5, pady=5)
txtfld4.insert(END, "BLUE GREEN")

txtfld5 = Entry(win,justify="center", bg='white', fg='black')
txtfld5.grid(column=0, row=1, padx=5)
txtfld5.insert(END, "WHITE")

txtfld6 = Entry(win,justify="center", bg='orange', fg='blue')
txtfld6.grid(column=1, row=1, padx=5)
txtfld6.insert(END, "ORANGE")

txtfld7 = Entry(win,justify="center", bg='green', fg='purple')
txtfld7.grid(column=2, row=1, padx=5)
txtfld7.insert(END, "GREEN")

txtfld8 = Entry(win,justify="center", bg='red', fg='#09A876')
txtfld8.grid(column=0, row=3, padx=5)
txtfld8.insert(END, "RED")

txtfld9 = Entry(win,justify="center", bg='indigo', fg='yellow')
txtfld9.grid(column=2, row=2, padx=5)
txtfld9.insert(END, "INDIGO")

txtfld10 = Entry(win,justify="center", bg='yellow', fg='indigo')
txtfld10.grid(column=2, row=3, padx=5)
txtfld10.insert(END, "YELLOW")

frame = Frame(win)
frame.grid(row=3, column=1, padx=5, pady=5)

lstbox = Listbox(frame)
lstbox.pack(side=LEFT, fill=BOTH, expand=True)

yscroll = Scrollbar(frame, orient=VERTICAL, command=lstbox.yview)
yscroll.pack(side=RIGHT, fill=Y)

lstbox.config(yscrollcommand=yscroll.set)

for x in range(51):
    lstbox.insert(END, x)

yscroll.config(command=lstbox.yview)
lstbox.config(yscrollcommand=yscroll.set)

win.mainloop()