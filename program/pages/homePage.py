from tkinter import *

class HomePage(Frame):
    def __init__(self, view):
        Frame.__init__(self)
        self.view = view
        Label(self, text = "Home Page!", bg = "#FFFFFF", relief = "groove").grid(row = 1, column = 1)
        Button(self, text="Employees", command = lambda: self.view.switcher(1)).grid(row=2, column=1)
