from tkinter import ttk, BOTH, Frame, StringVar, RIGHT, LEFT

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame


class ListManga(RightPage):
    def __init__(self, main):
        super(ListManga, self).__init__(main)
        self.current_page = 1
        self.current_display = ""

        title = ttk.Label(self, text="Liste Manga", font="-size 22 -weight bold")
        title.pack(pady=15)

        top_frame = Frame(self)

        self.search = StringVar(self)
        search_entry = ttk.Entry(top_frame, textvariable=self.search, width=30)
        search_entry.pack(side=LEFT, padx=10)
        valid_entry = ttk.Button(top_frame, text="Rechercher", command=self.validate_search, width=20)
        valid_entry.pack(side=LEFT, padx=(10, 30))

        self.top = StringVar(self)
        self.top.set("Top Global")
        top_select = ttk.OptionMenu(top_frame, self.top, "Top Global", "Top Global", "Top Manga", "Top Novels",
                                    "Top Oneshots", "Top Doujin", "Top Manhwa", "Top Manhua", "Top Populaire",
                                    "Top Favoris")
        top_select["width"] = 30
        top_select.pack(side=LEFT, padx=(30, 10))
        valid_top = ttk.Button(top_frame, text="Afficher le top", command=self.validate_top, width=20)
        valid_top.pack(side=LEFT, padx=10)

        top_frame.pack(pady=20)

        bottom_frame = Frame(self)

        left_page = ttk.Button(bottom_frame, text="<-", width=20, command=self.previous_page)
        left_page.pack(side=LEFT, padx=20)
        self.num_page = ttk.Label(bottom_frame, text="Page 1")
        self.num_page.pack(side=LEFT, padx=20)
        right_page = ttk.Button(bottom_frame, text="->", width=20, command=self.next_page)
        right_page.pack(side=LEFT, padx=20)

        bottom_frame.pack(pady=10)

        self.result_frame = ScrollFrame(self, width=1080, height=600)
        self.result_frame.pack_propagate(False)
        self.result_frame.grid_propagate(False)
        self.result_frame.pack(pady=(20, 0))

        self.pack(side=RIGHT, fill=BOTH)

    def next_page(self):
        if self.current_display.startswith("search "):
            self.current_page += 1
            self.reload_results(
                self.main.mal.search("manga", " ".join(self.current_display.split(" ")[:1]), self.current_page)
            )
        else:
            temp = {
                "Top Global": None,
                "Top Manga": "manga",
                "Top Novels": "novels",
                "Top Oneshots": "oneshots",
                "Top Doujin": "doujin",
                "Top Manhwa": "manhwa",
                "Top Manhua": "manhua",
                "Top Populaire": "bypopularity",
                "Top Favoris": "favorite"
            }
            self.current_page += 1
            self.reload_results(self.main.mal.top("manga", self.current_page, temp[self.current_display]))
        self.num_page["text"] = "Page "+str(self.current_page)

    def previous_page(self):
        if self.current_page != 1:
            if self.current_display.startswith("search "):
                self.current_page -= 1
                self.reload_results(
                    self.main.mal.search("manga", " ".join(self.current_display.split(" ")[:1]), self.current_page)
                )
            else:
                temp = {
                    "Top Global": None,
                    "Top Manga": "manga",
                    "Top Novels": "novels",
                    "Top Oneshots": "oneshots",
                    "Top Doujin": "doujin",
                    "Top Manhwa": "manhwa",
                    "Top Manhua": "manhua",
                    "Top Populaire": "bypopularity",
                    "Top Favoris": "favorite"
                }
                self.current_page -= 1
                self.reload_results(self.main.mal.top("manga", self.current_page, temp[self.current_display]))
            self.num_page["text"] = "Page " + str(self.current_page)

    def validate_search(self):
        self.current_display = "search "+self.search.get()
        self.current_page = 1
        self.num_page["text"] = "Page "+str(self.current_page)
        self.reload_results(self.main.mal.search("manga", self.search.get()))

    def validate_top(self):
        temp = {
            "Top Global": None,
            "Top Manga": "manga",
            "Top Novels": "novels",
            "Top Oneshots": "oneshots",
            "Top Doujin": "doujin",
            "Top Manhwa": "manhwa",
            "Top Manhua": "manhua",
            "Top Populaire": "bypopularity",
            "Top Favoris": "favorite"
        }
        self.current_display = self.top.get()
        self.current_page = 1
        self.num_page["text"] = "Page "+str(self.current_page)
        self.reload_results(self.main.mal.top("manga", 1, temp[self.top.get()]))

    def reload_results(self, results):
        self.result_frame.destroy()

        self.result_frame = ScrollFrame(self, width=1080, height=600)
        self.result_frame.pack_propagate(False)
        self.result_frame.grid_propagate(False)

        for i, manga in enumerate(results):
            temp = ttk.Frame(self.result_frame.viewport)

            image = ttk.Label(temp)
            self.main.image.apply_image_on_label("manga_" + str(manga["mal_id"]) + ".jpg", manga["image_url"], image)
            image.pack()

            title = ttk.Button(temp, text=manga["title"])
            title.pack(pady=10)

            temp.grid(row=i // 2, column=i % 2, pady=20)

        self.result_frame.viewport.columnconfigure(0, weight=1)
        self.result_frame.viewport.columnconfigure(1, weight=1)
        self.result_frame.pack(pady=(20, 0))
