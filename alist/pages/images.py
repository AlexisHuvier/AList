from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame, open_url


class Images(RightPage):
    def __init__(self, main, mal_id, title):
        super(Images, self).__init__(main)
        if title.startswith("a_"):
            self.pictures = self.main.mal.anime(mal_id, "pictures")
            type_ = "anime"
        else:
            self.pictures = self.main.mal.manga(mal_id, "pictures")
            type_ = "manga"
        title = title[2:]

        title = ttk.Label(self, text=title, font="-size 22 -weight bold")
        title.pack(pady=15)

        scroll = ScrollFrame(self, width=1080, height=630)
        scroll.pack_propagate(False)

        for i, pic in enumerate(self.pictures["pictures"]):
            temp = ttk.Frame(scroll.viewport)

            image = ttk.Label(temp)
            self.main.imager.apply_image_on_label(type_+"_"+str(mal_id)+"_pic"+str(i)+".jpg", pic["small"], image)
            image.bind("<Button-1>", lambda _, url=pic["large"]: open_url(url))
            image.pack()

            temp.grid(row=i // 4, column=i % 4, pady=5, padx=5)

        for i in range(4):
            scroll.viewport.columnconfigure(i, weight=1)

        scroll.pack(pady=10)

        back = ttk.Button(self, text="Retour", command=lambda: self.main.show_page(type_+" "+str(mal_id)))
        back.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
