from tkinter import *
from homePage import HomePage

class View:
    root = Tk()
    currentPage = None

    def __init__(self):
        self.root.title("Animal Rescue")
        self.switcher(0)
        self.root.mainloop()

    def switcher(self, page):
        pages = {
            0: HomePage
        }
        currentPage = pages.get(page, "Invalid page")
        try:
            currentPage().grid(row = 0, column = 0)
        except TypeError:
            print(currentPage)
            self.root.destroy()

    def quit(self):
        self.root.destroy()
