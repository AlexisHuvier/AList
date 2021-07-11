from tkinter import ttk, RIGHT, BOTH, StringVar

from alist.pages.right_page import RightPage


class ModifAnime(RightPage):
    def __init__(self, main, mal_id):
        super(ModifAnime, self).__init__(main)
        self.anime = self.main.myanime.get(mal_id)

        title = ttk.Label(self, text=self.anime["name"], font="-size 22 -weight bold")
        title.pack(pady=20)

        status = ttk.Label(self, text="Statut :")
        status.pack(pady=(15, 10))
        self.status = StringVar(self)
        self.status.set(self.anime["status"])
        temp = ["A voir", "En visionnement", "Fini", "Abandonné"]
        temp.remove(self.anime["status"])
        stat = ttk.OptionMenu(self, self.status, self.anime["status"], self.anime["status"], *temp)
        stat["width"] = 20
        stat.pack(pady=(0, 15))

        ep = ttk.Label(self, text="Nombre d'épisodes vus (/"+str(self.anime["max_ep"])+"):")
        ep.pack(pady=(15, 0))
        self.ep = ttk.Spinbox(self, from_=0., to=self.anime["max_ep"], width=20)
        self.ep.set(self.anime["ep"])
        self.ep.pack(pady=15)

        valid = ttk.Button(self, text="Valider", width=20, command=self.validate)
        valid.pack(pady=20)

        self.pack(side=RIGHT, fill=BOTH)

    def validate(self):
        self.main.myanime.modify(self.anime["id"], status=self.status.get(), ep=int(self.ep.get()))
