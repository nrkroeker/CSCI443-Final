try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from table import Multicolumn_Listbox
from pages.viewEmployee import ViewEmployeePage

class EmployeesPage(Frame):
    def __init__(self, view):
        Frame.__init__(self)
        self.view = view
        Button(self, text="<--", command = lambda: self.view.switcher(0)).grid(row=0, column=0)
        Label(self, text = "Employees Page", bg = "#FFFFFF", relief = "groove").grid(row = 0, column = 3)

        self.table = Multicolumn_Listbox(self, ["Name","Position", "Start Date"], [["Joe Rosenberg", "Front Desk Employee", "10/10/2017"], ["Susan Strong", "Manager", "01/01/2017"], ["Jake Dog", "Dog", "None"]], stripped_rows = ("white","#f2f2f2"), command=self.on_select, cell_anchor="center")
        self.table.interior.grid(row=1, column=0, columnspan=5)

        row = self.view.db.execute("SELECT * FROM Sailor")
        data = row.fetchall()

    def on_select(self, data):
        view = ViewEmployeePage(self, data)
        self.grid_remove()
        view.grid(row=0, column=0)
