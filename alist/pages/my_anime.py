from tkinter import ttk, RIGHT, BOTH, LEFT, StringVar, SUNKEN, filedialog

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame


class MyAnime(RightPage):
    def __init__(self, main):
        super(MyAnime, self).__init__(main)
        title = ttk.Label(self, text="Mes Animes", font="-size 22 -weight bold")
        title.pack(pady=15)

        top_frame = ttk.Frame(self)

        self.search = StringVar(self)
        search_entry = ttk.Entry(top_frame, textvariable=self.search, width=30)
        search_entry.pack(side=LEFT, padx=10)
        valid_search = ttk.Button(top_frame, text="Rechercher", width=20, command=self.validate_search)
        valid_search.pack(side=LEFT, padx=(10, 30))

        self.etat = StringVar(self)
        self.etat.set("Tous")
        etat_select = ttk.OptionMenu(top_frame, self.etat, "Tous", "Tous", "A voir", "En visionnement", "Fini",
                                     "Abandonné")
        etat_select["width"] = 30
        etat_select.pack(side=LEFT, padx=(30, 10))
        valid_etat = ttk.Button(top_frame, text="Afficher", width=20, command=self.validate_state)
        valid_etat.pack(side=LEFT, padx=10)

        top_frame.pack(pady=10)

        bottom_frame = ttk.Frame(self)

        self.exp_imp = StringVar(self)
        self.exp_imp.set("MyAnimeList")
        exp_imp = ttk.OptionMenu(bottom_frame, self.exp_imp, "MyAnimeList")
        exp_imp["width"] = 30
        exp_imp.pack(side=LEFT, padx=20)
        import_ = ttk.Button(bottom_frame, text="Import", width=20, command=self.import_)
        import_.pack(side=LEFT, padx=10)
        export = ttk.Button(bottom_frame, text="Export", width=20, command=self.export_)
        export.pack(side=LEFT, padx=10)

        bottom_frame.pack(pady=10)

        self.result_frame = ScrollFrame(self, width=1080, height=800)
        self.result_frame.pack_propagate(False)
        self.result_frame.grid_propagate(False)
        self.result_frame.pack(pady=(10, 0))

        self.validate_state()

        self.pack(side=RIGHT, fill=BOTH)

    def import_(self):
        if self.exp_imp.get() == "MyAnimeList":
            file = filedialog.askopenfilename(parent=self, title="AList - Import MAL",
                                              filetypes=(("Fichier MAL", ".xml"),), multiple=False)
            if file:
                self.main.mal_import.import_("anime", file)
                self.main.show_page("reload")

    def export_(self):
        if self.exp_imp.get() == "MyAnimeList":
            file = filedialog.asksaveasfilename(parent=self, title="AList - Export MAL",
                                                filetypes=(("Fichier MAL", ".xml"),))
            if file:
                self.main.mal_export.export("anime", file)

    def validate_search(self):
        self.reload_results(self.main.myanime.search(self.search.get()))

    def validate_state(self):
        if self.etat.get() == "Tous":
            self.reload_results(self.main.myanime.get_all())
        else:
            self.reload_results(self.main.myanime.get_all_state(self.etat.get()))

    def reload_results(self, results):
        self.result_frame.destroy()

        self.result_frame = ScrollFrame(self, width=1080, height=800)
        self.result_frame.pack_propagate(False)
        self.result_frame.grid_propagate(False)

        for i, anime in enumerate(results):
            temp = ttk.Frame(self.result_frame.viewport, relief=SUNKEN)
            temp.pack_propagate(False)
            temp.config(width=400, height=220)

            title = ttk.Label(temp, text=anime["name"], font="-size 13")
            title.pack(pady=15)
            status = ttk.Label(temp, text="Statut : "+anime["status"])
            status.pack(pady=5)
            ep = ttk.Label(temp, text="Episodes : "+str(anime["ep"])+"/"+str(anime["max_ep"]))
            ep.pack(pady=10)

            buttons = ttk.Frame(temp)

            delete = ttk.Button(buttons, text="Supprimer", width=10,
                                command=lambda a=anime: self.delete_anime(a["id"]))
            delete.pack(side=LEFT, padx=10)
            more_info = ttk.Button(buttons, text="Plus d'info", width=10,
                                   command=lambda a=anime: self.main.show_page("anime "+str(a["id"])))
            more_info.pack(side=RIGHT, padx=10)
            modify = ttk.Button(buttons, text="Modifier", width=10,
                                command=lambda a=anime: self.main.show_page("modifanime "+str(a["id"])))
            modify.pack(padx=10)

            buttons.pack(pady=(15, 3))

            buttons2 = ttk.Frame(temp)
            down = ttk.Button(buttons2, text="-1", width=3, command=lambda a=anime: self.modify_ep(a, a["ep"] - 1))
            down.pack(side=LEFT, padx=10)
            up = ttk.Button(buttons2, text="+1", width=3, command=lambda a=anime: self.modify_ep(a, a["ep"] + 1))
            up.pack(side=RIGHT, padx=10)
            buttons2.pack(pady=(3, 15))

            temp.grid(row=i // 2, column=i % 2, pady=20)

        self.result_frame.viewport.columnconfigure(0, weight=1)
        self.result_frame.viewport.columnconfigure(1, weight=1)
        self.result_frame.pack(pady=(10, 0))

    def modify_ep(self, anime, nb):
        if nb > anime["max_ep"]:
            self.main.myanime.modify(anime["id"], ep=anime["max_ep"])
        elif nb < 0:
            self.main.myanime.modify(anime["id"], ep=0)
        else:
            self.main.myanime.modify(anime["id"], ep=nb)
        self.main.show_page("reload")

    def delete_anime(self, mal_id):
        self.main.myanime.delete(mal_id)
        self.main.show_page("reload")
