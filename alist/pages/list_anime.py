from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage


class ListAnime(RightPage):
    def __init__(self, main):
        super(ListAnime, self).__init__(main)
        title = ttk.Label(self, text="Liste Animes", font="-size 22 -weight bold")
        title.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
