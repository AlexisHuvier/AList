from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage


class Parameters(RightPage):
    def __init__(self, main):
        super(Parameters, self).__init__(main)
        title = ttk.Label(self, text="Paramètres", font="-size 22 -weight bold")
        title.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
