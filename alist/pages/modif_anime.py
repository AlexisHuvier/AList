from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage


class ModifAnime(RightPage):
    def __init__(self, main, mal_id):
        super(ModifAnime, self).__init__(main)
        self.anime = self.main.myanime.get(mal_id)

        title = ttk.Label(self, text="MODIF ANIME", font="-size 22 -weight bold")
        title.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
