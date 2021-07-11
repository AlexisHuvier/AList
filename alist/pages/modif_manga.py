from tkinter import ttk, RIGHT, BOTH, StringVar

from alist.pages.right_page import RightPage


class ModifManga(RightPage):
    def __init__(self, main, mal_id):
        super(ModifManga, self).__init__(main)
        self.manga = self.main.mymanga.get(mal_id)

        title = ttk.Label(self, text=self.manga["name"], font="-size 22 -weight bold")
        title.pack(pady=20)

        status = ttk.Label(self, text="Statut :")
        status.pack(pady=(15, 10))
        self.status = StringVar(self)
        self.status.set(self.manga["status"])
        temp = ["A voir", "En visionnement", "Fini", "Abandonné"]
        temp.remove(self.manga["status"])
        stat = ttk.OptionMenu(self, self.status, self.manga["status"], self.manga["status"], *temp)
        stat["width"] = 20
        stat.pack(pady=(0, 15))

        vol = ttk.Label(self, text="Nombre de volumes vus (/"+str(self.manga["max_vol"])+"):")
        vol.pack(pady=(15, 0))
        self.vol = ttk.Spinbox(self, from_=0., to=self.manga["max_vol"], width=20)
        self.vol.set(self.manga['vol'])
        self.vol.pack(pady=15)

        chap = ttk.Label(self, text="Nombre de chapitres vus (/"+str(self.manga["max_chap"])+"):")
        chap.pack(pady=(15, 0))
        self.chap = ttk.Spinbox(self, from_=0., to=self.manga["max_chap"], width=20)
        self.chap.set(self.manga['chap'])
        self.chap.pack(pady=15)

        valid = ttk.Button(self, text="Valider", width=20, command=self.validate)
        valid.pack(pady=20)

        self.pack(side=RIGHT, fill=BOTH)

    def validate(self):
        self.main.mymanga.modify(self.manga["id"], status=self.status.get(), vol=int(self.vol.get()),
                                chap=int(self.chap.get()))
