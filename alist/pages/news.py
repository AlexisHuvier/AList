from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage


class News(RightPage):
    def __init__(self, main, mal_id, title):
        super(News, self).__init__(main)
        if title.startswith("a_"):
            self.news = self.main.mal.anime(mal_id, "news")
            type_ = "anime"
        else:
            self.news = self.main.mal.manga(mal_id, "news")
            type_ = "manga"
        title = title[2:]

        title = ttk.Label(self, text=title, font="-size 22 -weight bold")
        title.pack(pady=15)

        back = ttk.Button(self, text="Retour", command=lambda: self.main.show_page(type_+" "+str(mal_id)))
        back.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
