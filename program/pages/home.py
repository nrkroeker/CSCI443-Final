try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class HomePage(Frame):
    def __init__(self, view):
        Frame.__init__(self)
        self.view = view

        Label(self, text = "Home Page!", bg = "#FFFFFF", relief = "groove").grid(row = 0, column = 1, sticky=N)
        buttons = ['Employees', 'Pets', 'Supplies', 'Clients', 'Events', 'Vets']
        r = 1
        for index, label in enumerate(buttons):
            if (index%3 == 0):
                r += 1
            Button(self, text=label, command = lambda i=index + 1: self.view.switcher(i)).grid(row=r, column=index%3, sticky=N+S+E+W)
