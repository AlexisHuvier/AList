from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage


class ModifManga(RightPage):
    def __init__(self, main, mal_id):
        super(ModifManga, self).__init__(main)
        self.manga = self.main.mymanga.get(mal_id)

        title = ttk.Label(self, text="MODIF MANGA", font="-size 22 -weight bold")
        title.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
