from tkinter import *

class EmployeesPage(Frame):
    def __init__(self, view):
        Frame.__init__(self)
        self.view = view
        Label(self, text = "Employees Page!", bg = "#FFFFFF", relief = "groove").grid(row = 1, column = 1)
        Button(self, text="Home", command = lambda: self.view.switcher(0)).grid(row=2, column=1)
