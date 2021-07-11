from tkinter import ttk, RIGHT, BOTH, LEFT, StringVar, SUNKEN

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

        top_frame.pack(pady=20)

        self.result_frame = ScrollFrame(self, width=1080, height=800)
        self.result_frame.pack_propagate(False)
        self.result_frame.grid_propagate(False)
        self.result_frame.pack(pady=(20, 0))

        self.validate_state()

        self.pack(side=RIGHT, fill=BOTH)

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
            title.pack(pady=22)
            status = ttk.Label(temp, text="Statut : "+anime["status"])
            status.pack(pady=5)
            ep = ttk.Label(temp, text="Episodes : "+str(anime["ep"])+"/"+str(anime["max_ep"]))
            ep.pack(pady=15)

            buttons = ttk.Frame(temp)

            modify = ttk.Button(buttons, text="Modifier")
            modify.pack(side=LEFT, padx=10)
            more_info = ttk.Button(buttons, text="Plus d'info",
                                   command=lambda a=anime: self.main.show_page("anime "+str(a["id"])))
            more_info.pack(side=RIGHT, padx=10)

            buttons.pack(pady=20)

            temp.grid(row=i // 2, column=i % 2, pady=20)

        self.result_frame.viewport.columnconfigure(0, weight=1)
        self.result_frame.viewport.columnconfigure(1, weight=1)
        self.result_frame.pack(pady=(20, 0))
