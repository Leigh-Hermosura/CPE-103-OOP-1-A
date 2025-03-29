import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Combobox')
window.geometry('400x350')

def choice(event):
    month = monthCombobox.get()
    date = dateCombobox.get()
    year = yearCombobox.get()
    print("Your birth month", month)
    print("Your birth date", date)
    print("Your birth year", year)

    if month == " February":
        dateCombobox['values'] = (' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10',
                                  ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20',
                                  ' 21', ' 22', ' 23', ' 24', ' 25', ' 26', ' 27', ' 28', ' 29')
    else:
        dateCombobox['values'] = (' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10',
                                  ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20',
                                  ' 21', ' 22', ' 23', ' 24', ' 25', ' 26', ' 27', ' 28', ' 29', ' 30', ' 31')

def showButton(month, date, year):
    showinfo(
        title="Selection",
        message=f'You selected {month} {date}, {year}'
    )


# label text for title
ttk.Label(window, text="Choose Your Birthdate",
          background='light yellow', foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=1)

# Set label
ttk.Label(window, text="Select the month of your birth :",
          font=("Times New Roman", 12)).grid(column=0, row=5, padx=5, pady=25)

ttk.Label(window, text="Select the date of your birth :",
          font=("Times New Roman", 12)).grid(column=0, row=6, padx=5, pady=25)

ttk.Label(window, text="Select the year of your birth :",
          font=("Times New Roman", 12)).grid(column=0, row=7, padx=5, pady=25)

# Create Combobox
nDate = tk.StringVar()
nMonth = tk.StringVar()
nYear = tk.StringVar()

monthCombobox = ttk.Combobox(window, width=27, textvariable=nMonth)
dateCombobox = ttk.Combobox(window, width=27, textvariable=nDate)
yearCombobox = ttk.Combobox(window, width=27, textvariable=nYear)

# Adding combobox drop down list
monthCombobox['values'] = (' January', ' February', ' March', ' April', ' May', ' June',
                   ' July', ' August', ' September', ' October', ' November', ' December')

dateCombobox['values'] = (' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10',
                   ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20',
                  ' 21', ' 22', ' 23', ' 24', ' 25', ' 26', ' 27', ' 28', ' 29', ' 30', ' 31')

yearCombobox['values'] = [str(i) for i in reversed(range(1800, 2026))]

monthCombobox.grid(column=1, row=5)
dateCombobox.grid(column=1, row=6)
yearCombobox.grid(column=1, row=7)

monthCombobox.current(0)
dateCombobox.current(0)
yearCombobox.current(0)

monthCombobox.bind("<<ComboboxSelected>>", choice)
dateCombobox.bind("<<ComboboxSelected>>", choice)
yearCombobox.bind("<<ComboboxSelected>>", choice)

ttk.Button(window, text="Ok",
           command=lambda: showButton(monthCombobox.get(), dateCombobox.get(),
                                      yearCombobox.get())).grid(column=1,
                                                                row=8,
                                                                padx=5,
                                                                pady=25)

window.mainloop()
