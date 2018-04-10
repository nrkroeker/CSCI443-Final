from tkinter import *
from pages.homePage import HomePage
from pages.employeesPage import EmployeesPage

class View:
    root = Tk()
    currentPage = None

    def __init__(self):
        self.root.title("Animal Rescue")
        self.switcher(0)
        self.root.mainloop()

    def switcher(self, page):
        if (self.currentPage != None):
            self.currentPage.grid_remove()
        pages = {
            0: HomePage,
            1: EmployeesPage
        }
        self.currentPage = pages.get(page, "Invalid page")
        try:
            self.currentPage = self.currentPage(self)
            self.currentPage.grid(row = 0, column = 0)
        except TypeError:
            print(currentPage)
            self.root.destroy()

    def quit(self):
        self.root.destroy()
