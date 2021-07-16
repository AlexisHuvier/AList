from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame, open_url


class Recommands(RightPage):
    def __init__(self, main, mal_id, title):
        super(Recommands, self).__init__(main)
        if title.startswith("a_"):
            self.recommandations = self.main.mal.anime(mal_id, "recommendations")
            type_ = "anime"
        else:
            self.recommandations = self.main.mal.manga(mal_id, "recommendations")
            type_ = "manga"
        title = title[2:]

        title = ttk.Label(self, text=title, font="-size 22 -weight bold")
        title.pack(pady=15)

        scroll = ScrollFrame(self, width=1080, height=630)
        scroll.pack_propagate(False)

        for i, recommandation in enumerate(self.recommandations["recommendations"]):
            temp = ttk.Frame(scroll.viewport)

            ttitle = ttk.Label(temp, text=recommandation["title"], font="-weight bold")
            ttitle.pack(pady=(10, 2))
            nr = ttk.Label(temp, text="Nombre recommandation : "+str(recommandation["recommendation_count"]))
            nr.pack(pady=(2, 10))

            image = ttk.Label(temp)
            self.main.imager.apply_image_on_label(type_+"_"+str(mal_id)+"_rec"+str(i)+".jpg", recommandation["image_url"],
                                                  image)
            image.pack(pady=(10, 5))

            url = ttk.Button(temp, text="Plus d'info",
                             command=lambda a=recommandation: self.main.show_page(type_+" "+str(a["mal_id"])))
            url.pack(pady=(0, 10))

            temp.grid(row=i // 3, column=i % 3, pady=10, padx=5)

        for i in range(3):
            scroll.viewport.columnconfigure(i, weight=1)

        scroll.pack(pady=10)

        back = ttk.Button(self, text="Retour", command=lambda: self.main.show_page(type_ + " " + str(mal_id)))
        back.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
