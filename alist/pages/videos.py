from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame, open_url


class Videos(RightPage):
    def __init__(self, main, mal_id, title):
        super(Videos, self).__init__(main)
        self.videos = self.main.mal.anime(mal_id, "videos")

        title = ttk.Label(self, text=title, font="-size 22 -weight bold")
        title.pack(pady=15)

        scroll = ScrollFrame(self, width=1080, height=630)
        scroll.pack_propagate(False)

        for i, video in enumerate(self.videos["promo"]):
            temp = ttk.Frame(scroll.viewport)

            ttitle = ttk.Label(temp, text=video["title"], font="-weight bold")
            self.main.translator.translate(ttitle, video["title"])
            ttitle.pack(pady=10)

            image = ttk.Label(temp)
            self.main.imager.apply_image_on_label("anime_" + str(mal_id) + "_vid" + str(i) + ".jpg", video["image_url"],
                                                  image)
            image.pack(pady=(10, 5))

            url = ttk.Button(temp, text="Lien", command=lambda a=video: open_url(a["video_url"]))
            url.pack(pady=(0, 10))

            temp.grid(row=i // 2, column=i % 2, pady=10, padx=5)

        for i in range(2):
            scroll.viewport.columnconfigure(i, weight=1)

        scroll.pack(pady=10)

        back = ttk.Button(self, text="Retour", command=lambda: self.main.show_page("anime "+str(mal_id)))
        back.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
