from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame, open_url


class Characters(RightPage):
    def __init__(self, main, mal_id, title):
        super(Characters, self).__init__(main)
        if title.startswith("a_"):
            self.characters = self.main.mal.anime(mal_id, "characters_staff")
            type_ = "anime"
        else:
            self.characters = self.main.mal.manga(mal_id, "characters")
            type_ = "manga"
        title = title[2:]

        title = ttk.Label(self, text=title, font="-size 22 -weight bold")
        title.pack(pady=15)

        scroll = ScrollFrame(self, width=1080, height=630)
        scroll.pack_propagate(False)

        for i, character in enumerate(self.characters["characters"]):
            temp = ttk.Frame(scroll.viewport)

            ttitle = ttk.Label(temp, text=character["name"], font="-weight bold")
            ttitle.pack(pady=10)

            image = ttk.Label(temp)
            self.main.imager.apply_image_on_label(type_+"_"+str(mal_id)+"_cha"+str(i)+".jpg", character["image_url"],
                                                  image)
            image.pack(pady=(10, 5))

            url = ttk.Button(temp, text="Lien", command=lambda a=character: open_url(a["url"]))
            url.pack(pady=(0, 10))

            temp.grid(row=i // 4, column=i % 4, pady=10, padx=5)

        for i in range(4):
            scroll.viewport.columnconfigure(i, weight=1)

        scroll.pack(pady=10)

        back = ttk.Button(self, text="Retour", command=lambda: self.main.show_page(type_ + " " + str(mal_id)))
        back.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
