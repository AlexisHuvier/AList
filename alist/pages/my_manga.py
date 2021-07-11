from tkinter import ttk, RIGHT, BOTH, StringVar, LEFT, SUNKEN

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

        top_frame.pack(pady=20)

        self.result_frame = ScrollFrame(self, width=1080, height=800)
        self.result_frame.pack_propagate(False)
        self.result_frame.grid_propagate(False)
        self.result_frame.pack(pady=(20, 0))

        self.validate_state()

        self.pack(side=RIGHT, fill=BOTH)

    def validate_search(self):
        self.reload_results(self.main.mymanga.search(self.search.get()))

    def validate_state(self):
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
            title.pack(pady=20)
            status = ttk.Label(temp, text="Statut : "+manga["status"])
            status.pack(pady=5)
            ep = ttk.Label(temp, text="Volumes : "+str(manga["vol"])+"/"+str(manga["max_vol"]))
            ep.pack(pady=5)
            ep = ttk.Label(temp, text="Chapitres : "+str(manga["chap"])+"/"+str(manga["max_chap"]))
            ep.pack(pady=5)

            buttons = ttk.Frame(temp)

            modify = ttk.Button(buttons, text="Modifier",
                                command=lambda a=manga: self.main.show_page("modifmanga "+str(a["id"])))
            modify.pack(side=LEFT, padx=10)
            more_info = ttk.Button(buttons, text="Plus d'info",
                                   command=lambda a=manga: self.main.show_page("manga "+str(a["id"])))
            more_info.pack(side=RIGHT, padx=10)

            buttons.pack(pady=20)

            temp.grid(row=i // 2, column=i % 2, pady=20)

        self.result_frame.viewport.columnconfigure(0, weight=1)
        self.result_frame.viewport.columnconfigure(1, weight=1)
        self.result_frame.pack(pady=(20, 0))

