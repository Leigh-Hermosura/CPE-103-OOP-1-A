#GUI Conversion of the Calculator:
import tkinter as tk
from PIL import Image, ImageTk

# Operation history tracker
opHistory = []

# Function for clearing inputs
def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result.set("")

# Functions for calculation
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
        saveHistory(f'Added: {num1} + {num2} = {num1 + num2}')
    except ValueError:
        result.set("Invalid input")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 - num2)
        saveHistory(f'Subtracted: {num1} - {num2} = {num1 - num2}')
    except ValueError:
        result.set("Invalid input")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
        saveHistory(f'Multiplied: {num1} * {num2} = {num1 * num2}')
    except ValueError:
        result.set("Invalid input")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            result.set(num1 / num2)
            saveHistory(f"Divided: {num1} / {num2} = {num1 / num2}")
        else:
            result.set("Error! Division by zero.")
    except ValueError:
        result.set("Invalid input")

# Save operation to history
def saveHistory(operation):
    opHistory.append(operation)
    if len(opHistory) > 10:
        opHistory.pop(0)

# Function for viewing history
def history():
    histWin = tk.Toplevel(root, bg='#FA9222')
    histWin.title("Operation History")

    histList = tk.Listbox(histWin, height=10, width=40, bg='#97E285', font=('Tahoma', 12))
    histList.pack(padx=10, pady=10)

    for operation in reversed(opHistory):
        histList.insert(tk.END, operation)

# Create the main window
root = tk.Tk()
root.title("Simple Along Malapitan Calculator")
root.geometry('700x550')
#root.configure(bg='#97E285')

# Background photo
bgImg = Image.open("C:\\Users\\ucc_e\\Downloads\\AM LOGO.jpg")
bgImg = bgImg.resize((800, 600), Image.Resampling.LANCZOS)
bgPht = ImageTk.PhotoImage(bgImg)


# Create label widget
bgLabel = tk.Label(root, image=bgPht)
bgLabel.place(relwidth=1, relheight=1)

# Create StringVar to hold the result
result = tk.StringVar()

# Create the layout
tk.Label(root, text="Enter first number:", bg='#97E285', font=('Tahoma', 12)).grid(row=0, column=0)
entry1 = tk.Entry(root, bg='#CFCFCF', fg='#D76C0D', font=('Tahoma', 12))
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:", bg='#97E285', font=('Tahoma', 12)).grid(row=1, column=0)
entry2 = tk.Entry(root, bg='#CFCFCF', fg='#218D0C', font=('Tahoma', 12))
entry2.grid(row=1, column=1)

# Buttons for operations
tk.Button(root, text="Add", command=add, bg='#FA9222', font=('Tahoma', 12)).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", command=subtract, bg='#FA9222', font=('Tahoma', 12)).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Multiply", command=multiply, bg='#FA9222', font=('Tahoma', 12)).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Divide", command=divide, bg='#FA9222', font=('Tahoma', 12)).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Clear", command=clear, bg='#FA9222', font=('Tahoma', 12)).grid(row=2, column=2, padx=10, pady=10)
tk.Button(root, text="History", command=history, bg='#FA9222', font=('Tahoma', 12)).grid(row=3, column=2, padx=10, pady=10)

# Label to show result
tk.Label(root, text="Result:", bg='#97E285', font=('Tahoma', 12)).grid(row=5, column=0)
result_label = tk.Label(root, textvariable=result, bg='#97E285', font=('Tahoma', 12))
result_label.grid(row=5, column=1)

# Start the main loop
root.mainloop()
