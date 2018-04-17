try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from pages.home import HomePage
from pages.employees import EmployeesPage
from pages.pets import PetsPage
from pages.supplies import SuppliesPage
from pages.clients import ClientsPage
from pages.events import EventsPage
from pages.vets import VetsPage

class View:
    root = Tk()
    currentPage = None

    def __init__(self, db):
        self.db = db
        self.root.title("Animal Rescue")
        self.root.minsize(500, 300)
        self.switcher(0)
        self.root.mainloop()

    def switcher(self, page):
        if (self.currentPage != None):
            self.currentPage.destroy()
        pages = {
            0: HomePage,
            1: EmployeesPage,
            2: PetsPage,
            3: SuppliesPage,
            4: ClientsPage,
            5: EventsPage,
            6: VetsPage
        }
        self.currentPage = pages.get(page, "Invalid page")
        try:
            self.currentPage = self.currentPage(self)
            self.currentPage.grid(row = 0, column = 0)
        except TypeError:
            print(self.currentPage)
            self.root.destroy()
