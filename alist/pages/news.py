from tkinter import ttk, RIGHT, BOTH
from datetime import datetime

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame, open_url


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

        scroll = ScrollFrame(self, width=1080, height=800)
        scroll.pack_propagate(False)

        for article in self.news["articles"]:
            date = datetime.strptime(article["date"], "%Y-%m-%dT%H:%M:%S+00:00")
            temp = ttk.Frame(scroll.viewport)

            date = ttk.Label(temp, text=str(date.day)+"/"+str(date.month)+"/"+str(date.year))
            date.grid(row=0, column=0, pady=10, padx=(10, 0), sticky="w")
            title = ttk.Label(temp, text=article["title"], font="-weight bold")
            self.main.translator.translate(title, article["title"])
            title.grid(row=0, column=1, pady=10)
            author = ttk.Label(temp, text=article["author_name"])
            author.grid(row=0, column=2, pady=10, padx=(0, 10), sticky="e")

            intro = ttk.Label(temp,
                              text=article["intro"] if len(article["intro"]) < 130 else article["intro"][:127]+"..."
            )
            self.main.translator.translate(intro, article["intro"], 130, 1)
            intro.grid(row=1, column=0, columnspan=3, pady=10)

            url = ttk.Button(temp, text="Lien", command=lambda a=article: open_url(a["url"]))
            url.grid(row=2, column=0, columnspan=3, pady=10)

            for i in range(3):
                temp.columnconfigure(i, weight=1)

            temp.pack(pady=10, fill="x")

        scroll.pack(pady=15)

        back = ttk.Button(self, text="Retour", command=lambda: self.main.show_page(type_+" "+str(mal_id)))
        back.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
