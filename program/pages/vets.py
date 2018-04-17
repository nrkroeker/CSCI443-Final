try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class VetsPage(Frame):
    def __init__(self, view):
        Frame.__init__(self)
        self.view = view
        Button(self, text="<--", command = lambda: self.view.switcher(0)).grid(row=0, column=1)
        Label(self, text = "Vets Page", bg = "#FFFFFF", relief = "groove").grid(row = 0, column = 3, padx=50)

        row = self.view.db.execute("SELECT * FROM Sailor")
        data = row.fetchall()
        print(data)
