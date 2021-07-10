from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage


class Manga(RightPage):
    def __init__(self, main, mal_id):
        super(Manga, self).__init__(main)
        self.mal_id = mal_id

        title = ttk.Label(self, text="Manga : "+str(self.mal_id), font="-size 22 -weight bold")
        title.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
