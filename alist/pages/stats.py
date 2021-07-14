from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage


# TEMP
def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))
# TEMP


class Stats(RightPage):
    def __init__(self, main, mal_id, title):
        super(Stats, self).__init__(main)
        self.stats = self.main.mal.anime_stats(mal_id)

        title = ttk.Label(self, text=title, font="-size 22 -weight bold")
        title.pack(pady=15)

        pretty(self.stats)

        self.pack(side=RIGHT, fill=BOTH)
