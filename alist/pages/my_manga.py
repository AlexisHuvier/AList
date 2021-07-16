from tkinter import ttk, RIGHT, BOTH, StringVar, LEFT, SUNKEN, filedialog

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame


class MyManga(RightPage):
    def __init__(self, main):
        super(MyManga, self).__init__(main)
        title = ttk.Label(self, text="Mes Mangas", font="-size 22 -weight bold")
        title.pack(pady=15)

        top_frame = ttk.Frame(self)

        self.search = StringVar(self)
        search_entry = ttk.Entry(top_frame, textvariable=self.search, width=30)
        search_entry.bind("<Return>", self.validate_search)
        search_entry.pack(side=LEFT, padx=30)

        self.etat = StringVar(self)
        self.etat.set("Tous")
        etat_select = ttk.OptionMenu(top_frame, self.etat, "Tous", "Tous", "A voir", "En visionnement", "Fini",
                                     "Abandonné")
        etat_select["width"] = 30
        etat_select.pack(side=LEFT, padx=30)

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

        self.etat.trace("w", self.validate_state)
        self.validate_state()

    def import_(self):
        if self.exp_imp.get() == "MyAnimeList":
            file = filedialog.askopenfilename(parent=self, title="AList - Import MAL",
                                              filetypes=(("Fichier MAL", ".xml"),), multiple=False)
            if file:
                self.main.mal_import.import_("manga", file)
                self.main.show_page("reload")

    def export_(self):
        if self.exp_imp.get() == "MyAnimeList":
            file = filedialog.asksaveasfilename(parent=self, title="AList - Export MAL",
                                                filetypes=(("Fichier MAL", ".xml"),))
            if file:
                self.main.mal_export.export("manga", file)

    def validate_search(self, *ignore):
        self.reload_results(self.main.mymanga.search(self.search.get()))

    def validate_state(self, *ignore):
        if self.etat.get() == "Tous":
            self.reload_results(self.main.mymanga.get_all())
        else:
            self.reload_results(self.main.mymanga.get_all_state(self.etat.get()))

    def reload_results(self, results):
        self.result_frame.destroy()

        self.result_frame = ScrollFrame(self, width=1080, height=800)
        self.result_frame.pack_propagate(False)
        self.result_frame.grid_propagate(False)

        for i, manga in enumerate(results):
            temp = ttk.Frame(self.result_frame.viewport, relief=SUNKEN)
            temp.pack_propagate(False)
            temp.config(width=400, height=220)

            title = ttk.Label(temp, text=manga["name"], font="-size 13")
            title.pack(pady=10)
            status = ttk.Label(temp, text="Statut : "+manga["status"])
            status.pack(pady=5)
            ep = ttk.Label(temp, text="Volumes : "+str(manga["vol"])+"/"+str(manga["max_vol"]))
            ep.pack(pady=5)
            ep = ttk.Label(temp, text="Chapitres : "+str(manga["chap"])+"/"+str(manga["max_chap"]))
            ep.pack(pady=5)

            buttons = ttk.Frame(temp)

            delete = ttk.Button(buttons, text="Supprimer", width=10,
                                command=lambda a=manga: self.delete_manga(a["id"]))
            delete.pack(side=LEFT, padx=10)
            more_info = ttk.Button(buttons, text="Plus d'info",
                                   command=lambda a=manga: self.main.show_page("manga "+str(a["id"])))
            more_info.pack(side=RIGHT, padx=10)
            modify = ttk.Button(buttons, text="Modifier",
                                command=lambda a=manga: self.main.show_page("modifmanga "+str(a["id"])))
            modify.pack(padx=10)

            buttons.pack(pady=(15, 3))

            buttons2 = ttk.Frame(temp)
            down_vol = ttk.Button(buttons2, text="-1 Vol", width=8,
                                  command=lambda a=manga: self.modify_vol_chap(a, "vol", a["vol"] - 1))
            down_vol.pack(side=LEFT, padx=10)
            down_chap = ttk.Button(buttons2, text="-1 Chap", width=8,
                                   command=lambda a=manga: self.modify_vol_chap(a, "chap", a["chap"] - 1))
            down_chap.pack(side=LEFT, padx=10)
            up_vol = ttk.Button(buttons2, text="+1 Vol", width=8,
                                command=lambda a=manga: self.modify_vol_chap(a, "vol", a["vol"] + 1))
            up_vol.pack(side=RIGHT, padx=10)
            up_chap = ttk.Button(buttons2, text="+1 Chap", width=8,
                                 command=lambda a=manga: self.modify_vol_chap(a, "chap", a["chap"] + 1))
            up_chap.pack(side=RIGHT, padx=10)
            buttons2.pack(pady=(3, 15))

            temp.grid(row=i // 2, column=i % 2, pady=20)

        self.result_frame.viewport.columnconfigure(0, weight=1)
        self.result_frame.viewport.columnconfigure(1, weight=1)
        self.result_frame.pack(pady=(10, 0))

    def modify_vol_chap(self, manga, type_, nb):
        if nb > manga["max_"+type_]:
            eval("self.main.mymanga.modify(manga[\"id\"], "+type_+"=manga[\"max_\""+type_+"])")
        elif nb < 0:
            eval("self.main.mymanga.modify(manga[\"id\"], "+type_+"=0)")
        else:
            eval("self.main.mymanga.modify(manga[\"id\"], "+type_+"=nb)")
        self.main.show_page("reload")

    def delete_manga(self, mal_id):
        self.main.mymanga.delete(mal_id)
        self.main.show_page("reload")

