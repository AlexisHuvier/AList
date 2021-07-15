from tkinter import ttk, RIGHT, BOTH, LEFT

from alist.pages.right_page import RightPage
from alist.utils import utils


class Manga(RightPage):
    def __init__(self, main, mal_id):
        super(Manga, self).__init__(main)
        self.mal_id = mal_id
        self.manga = self.main.mal.manga(mal_id)

        title = ttk.Label(self, text=self.manga["title"], font="-size 20 -weight bold")
        title.pack(pady=(15, 10))

        add_list = ttk.Button(self, text="Ajouter à ma liste", width=20, command=self.add_to_list)
        add_list.pack(pady=(5, 15))

        manga = ttk.Frame(self)

        image = ttk.Label(manga)
        self.main.imager.apply_image_on_label("manga_" + str(self.manga["mal_id"]) + ".jpg",
                                              self.manga["image_url"],
                                              image)
        image.grid(row=0, column=1, rowspan=9)

        type_ = ttk.Label(manga, text="Type : Manga")
        type_.grid(row=1, column=0)
        en_title = ttk.Label(manga, text="Titre Anglais : "+self.manga["title_english"])
        en_title.grid(row=2, column=0)
        jap_title = ttk.Label(manga, text="Titre Japonais : "+self.manga["title_japanese"])
        jap_title.grid(row=2, column=0)
        author = ttk.Label(manga, text="Auteurs : "+", ".join((i["name"].split(", ")[1]+" "+i["name"].split(", ")[0]
                                                               for i in self.manga["authors"])))
        author.grid(row=3, column=0)

        genres = "Genres : " + \
                 ", ".join((self.main.translator.genre_translate(i["name"]) for i in self.manga["genres"]))
        genre = ttk.Label(manga, text="".join(genres), justify="center")
        genre.grid(row=4, column=0)

        if self.manga["status"].startswith("Finished"):
            status = ttk.Label(manga, text="Statut : Fini")
        elif self.manga["status"] == "Publishing":
            status = ttk.Label(manga, text="Statut : En cours en publication")
        elif self.manga["status"] == "Not yet aired":
            status = ttk.Label(manga, text="Statut : A Venir")
        else:
            status = ttk.Label(manga, text="Statut : Inconnu")
        status.grid(row=5, column=0)

        if self.manga["volumes"]:
            if self.manga["chapters"]:
                vol_chap = ttk.Label(manga, text="Nombre de Volumes : " + str(self.manga["volumes"]) +
                                                 "    Nombre de Chapitres : "+str(self.manga["chapters"]))
            else:
                vol_chap = ttk.Label(manga, text="Nombre de Volumes : " + str(self.manga["volumes"]) +
                                                 "    Nombre de Chapitres : 0")
        else:
            if self.manga["chapters"]:
                vol_chap = ttk.Label(manga, text="Nombre de Volumes : 0    Nombre de Chapitres : " +
                                                 str(self.manga["chapters"]))
            else:
                vol_chap = ttk.Label(manga, text="Nombre de Volumes : 0    Nombre de Chapitres : 0")
        vol_chap.grid(row=6, column=0)

        stats_list = []
        if self.manga["rank"]:
            stats_list.append("Top : "+str(self.manga["rank"]))
        else:
            stats_list.append("Top : Inconnu")
        if self.manga["score"]:
            stats_list.append("    Score : "+str(self.manga["score"]))
        else:
            stats_list.append("    Score : Inconnu")
        if self.manga["popularity"]:
            stats_list.append("    Popularité : "+str(self.manga["popularity"]))
        else:
            stats_list.append("    Popularité : Inconnue")
        stats_list.append("    Favoris : "+str(self.manga["favorites"]))
        stats = ttk.Label(manga, text="".join(stats_list))
        stats.grid(row=7, column=0)

        for i in range(9):
            manga.rowconfigure(i, weight=1)
        for i in range(2):
            manga.columnconfigure(i, weight=1)

        manga.pack(fill="x")

        synopsis_label = ttk.Label(self, text="Synopsis :")
        synopsis_label.pack(pady=(20, 5))
        if self.manga["synopsis"]:
            synopsis = ttk.Label(self, text="", justify="center")
            self.main.translator.translate(synopsis, self.manga["synopsis"])
        else:
            synopsis = ttk.Label(self, text="Aucun", justify="center")
        synopsis.pack(pady=(5, 20))

        btn = ttk.Frame(self)

        news = ttk.Button(btn, text="News", width=20,
                          command=lambda: self.main.show_page("news " + str(self.manga["mal_id"]) + " m_" +
                                                              self.manga["title"]))
        news.pack(side=LEFT, padx=20)
        videos = ttk.Button(btn, text="Vidéos", width=20)
        videos.pack(side=RIGHT, padx=20)
        images = ttk.Button(btn, text="Images", width=20)
        images.pack(padx=20)

        btn.pack(pady=10)

        btn2 = ttk.Frame(self)
        characters = ttk.Button(btn2, text="Personnages", width=20)
        characters.pack(side=LEFT, padx=20)
        stats = ttk.Button(btn2, text="Statistiques", width=20,
                           command=lambda: self.main.show_page("stats " + str(self.manga["mal_id"]) + " m_" +
                                                               self.manga["title"]))
        stats.pack(side=LEFT, padx=20)
        lien = ttk.Button(btn2, text="Lien MAL", width=20,
                          command=lambda: utils.open_url(self.manga["url"]))
        lien.pack(side=RIGHT, padx=20)
        reviews = ttk.Button(btn2, text="Avis", width=20)
        reviews.pack(side=RIGHT, padx=20)

        btn2.pack(pady=10)

        self.pack(side=RIGHT, fill=BOTH)

    def add_to_list(self):
        if self.manga["chapters"]:
            if self.manga["volumes"]:
                self.main.mymanga.add(self.manga["mal_id"], self.manga["title"], self.manga["volumes"],
                                      self.manga["chapters"], self.manga["type"])
            else:
                self.main.mymanga.add(self.manga["mal_id"], self.manga["title"], 0, self.manga["chapters"],
                                      self.manga["type"])
        else:
            if self.manga["volumes"]:
                self.main.mymanga.add(self.manga["mal_id"], self.manga["title"], self.manga["volumes"], 0,
                                      self.manga["type"])
            else:
                self.main.mymanga.add(self.manga["mal_id"], self.manga["title"], 0, 0, self.manga["type"])
