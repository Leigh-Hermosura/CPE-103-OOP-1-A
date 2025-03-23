import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow, QApplication, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QFont

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Account Register"
        self.x=200
        self.y=200
        self.width=400
        self.height=400
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.textboxttl = QLabel("Account Register", self)
        self.textboxttl.move(120, 15)
        self.labelFont(self.textboxttl, 16)

        self.textboxes = []
        for i in range(6):
            textbox = QLineEdit(self)
            textbox.move(180, 55 + (i * 40))
            textbox.resize(180, 30)
            self.textboxes.append(textbox)
            # self.textbox1.setText("Set this text value")

        label_texts = [
            "Enter First Name: ",
            "Enter Last Name: ",
            "Enter Username: ",
            "Enter Password: ",
            "Enter Email Address: ",
            "Enter Contact Number: "
        ]

        for i, label_text in enumerate(label_texts):
            label = QLabel(label_text, self)
            label.move(30, 65 + (i * 40))
            self.labelFont(label, 10)

        self.buttonsbmt = QPushButton('Submit', self)
        self.buttonsbmt.setToolTip("Submit your input")
        self.buttonsbmt.move(100, 330)
        self.buttonsbmt.clicked.connect(self.submit)

        self.buttonclr = QPushButton('Clear', self)
        self.buttonclr.setToolTip("Clear your input")
        self.buttonclr.move(220, 330)
        self.buttonclr.clicked.connect(self.clear)

        self.show()

    def labelFont(self, label, size):
        font = QFont()
        font.setPointSize(size)
        label.setFont(font)

    def clear(self):
        for textbox in self.textboxes:
            textbox.clear()

    def submit(self):
            print("Form submitted")
            QApplication.quit()
