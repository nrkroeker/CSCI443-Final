try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class ViewEmployeePage(Frame):
    def __init__(self, parent, employee):
        Frame.__init__(self)
        self.parent = parent
        Button(self, text="<--", command = lambda: self.back()).grid(row=0, column=0)
        Label(self, text="Employee").grid(row=0, column=1)

    def back(self):
        self.grid_remove()
        self.parent.grid(row=0, column=0)
