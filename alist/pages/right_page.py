from tkinter import ttk
from tkinter import GROOVE


class RightPage(ttk.Frame):
    def __init__(self, main):
        super(RightPage, self).__init__(main, relief=GROOVE)
        self.pack_propagate(False)
        self.grid_propagate(False)
        self["padding"] = 5
        self.config(width=980, height=800)
        self.main = main
