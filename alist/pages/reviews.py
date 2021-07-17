from tkinter import ttk, RIGHT, BOTH, LEFT
from datetime import datetime

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame, open_url


class Reviews(RightPage):
    def __init__(self, main, mal_id, title):
        super(Reviews, self).__init__(main)
        self.current_page = int(title[2:].split("_")[0])
        self.mal_id = mal_id
        self.reviews = None
        if title.startswith("a_"):
            self.type_ = "anime"
        else:
            self.type_ = "manga"
        title = "_".join(title[2:].split("_")[1:])

        title = ttk.Label(self, text=title, font="-size 22 -weight bold")
        title.pack(pady=15)

        bottom_frame = ttk.Frame(self)

        left_page = ttk.Button(bottom_frame, text="<-", width=20, command=self.previous_page)
        left_page.pack(side=LEFT, padx=20)
        self.num_page = ttk.Label(bottom_frame, text="Page "+str(self.current_page))
        self.num_page.pack(side=LEFT, padx=20)
        right_page = ttk.Button(bottom_frame, text="->", width=20, command=self.next_page)
        right_page.pack(side=LEFT, padx=20)

        bottom_frame.pack(pady=10)

        self.scroll = ScrollFrame(self, width=1080, height=600)
        self.scroll.pack_propagate(False)

        self.scroll.pack(pady=10)

        self.back = ttk.Button(self, text="Retour", command=lambda: self.main.show_page(self.type_+" "+str(mal_id)))
        self.back.pack(pady=10)

        self.pack(side=RIGHT, fill=BOTH)

        self.reload_results()

    def reload_results(self):
        if self.type_ == "anime":
            self.reviews = self.main.mal.anime(self.mal_id, "reviews", self.current_page)
        else:
            self.reviews = self.main.mal.manga(self.mal_id, "reviews", self.current_page)

        self.scroll.destroy()
        self.back.destroy()

        self.scroll = ScrollFrame(self, width=1080, height=580)
        self.scroll.pack_propagate(False)

        for review in self.reviews["reviews"]:
            date = datetime.strptime(review["date"], "%Y-%m-%dT%H:%M:%S+00:00")
            temp = ttk.Frame(self.scroll.viewport)

            author = ttk.Label(temp, text=review["reviewer"]["username"], font="-weight bold")
            author.grid(row=0, column=0, pady=10, padx=10)
            if self.type_ == "anime":
                rv_text = "Episodes vus : " + str(review["reviewer"]["episodes_seen"])
            else:
                rv_text = "Chapitres lus : " + str(review["reviewer"]["chapters_read"])
            read_view = ttk.Label(temp, text=rv_text)
            read_view.grid(row=0, column=1, pady=10, padx=10)
            notes = ttk.Label(temp, text="Note : " + str(round(sum(v for v in review["reviewer"]["scores"].values()) /
                                                               len(review["reviewer"]["scores"]), 2)) + "/10")
            notes.grid(row=0, column=2, pady=10, padx=10)
            date = ttk.Label(temp, text=str(date.day) + "/" + str(date.month) + "/" + str(date.year))
            date.grid(row=0, column=3, pady=10, padx=10)

            content = ttk.Label(temp, text="", justify="center")
            self.main.translator.translate(content, review["content"])
            content.grid(row=1, column=0, columnspan=4, pady=10)

            url = ttk.Button(temp, text="Lien", command=lambda a=review: open_url(a["url"]))
            url.grid(row=2, column=0, columnspan=4, pady=10)

            for i in range(4):
                temp.columnconfigure(i, weight=1)
            for i in range(3):
                temp.rowconfigure(i, weight=1)

            temp.pack(pady=10, fill="x")

        self.scroll.pack(pady=10)

        self.back = ttk.Button(self, text="Retour",
                               command=lambda: self.main.show_page(self.type_+" "+str(self.mal_id)))
        self.back.pack(pady=10)

    def next_page(self):
        self.current_page += 1
        self.reload_results()
        self.num_page["text"] = "Page "+str(self.current_page)

    def previous_page(self):
        if self.current_page != 1:
            self.current_page -= 1
            self.reload_results()
            self.num_page["text"] = "Page "+str(self.current_page)
