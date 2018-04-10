from tkinter import *

class HomePage(Frame):
    def __init__(self):
        Frame.__init__(self)
        Label(self, text = "Home Page!", bg = "#FFFFFF", relief = "groove").grid(row = 1, column = 1, ipadx = 200, ipady = 100)
