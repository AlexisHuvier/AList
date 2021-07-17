from tkinter import ttk, RIGHT, BOTH, LEFT

from alist.pages.right_page import RightPage
from alist.utils import open_url


class Anime(RightPage):
    def __init__(self, main, mal_id):
        super(Anime, self).__init__(main)
        self.mal_id = mal_id
        self.anime = self.main.mal.anime(mal_id)

        title = ttk.Label(self, text=self.anime["title"], font="-size 20 -weight bold")
        title.pack(pady=(15, 10))

        add_list = ttk.Button(self, text="Ajouter à ma liste", width=20, command=self.add_to_list)
        if self.main.myanime.is_in(self.anime["mal_id"]):
            add_list["state"] = "disabled"
        add_list.pack(pady=(5, 15))

        top = ttk.Frame(self)

        image = ttk.Label(top)
        self.main.imager.apply_image_on_label("anime_" + str(self.anime["mal_id"]) + ".jpg",
                                              self.anime["image_url"],
                                              image)
        image.grid(row=0, column=1, rowspan=12)

        type_ = ttk.Label(top, text="Type : Anime")
        type_.grid(row=1, column=0)
        en_title = ttk.Label(top, text="Titre Anglais : "+self.anime["title_english"])
        en_title.grid(row=2, column=0)
        jap_title = ttk.Label(top, text="Titre Japonais : "+self.anime["title_japanese"])
        jap_title.grid(row=3, column=0)
        author = ttk.Label(top, text="Studios : "+", ".join((i["name"] for i in self.anime["studios"])))
        author.grid(row=4, column=0)
        producers = ttk.Label(top, text="Producteurs : "+", ".join((i["name"] for i in self.anime["producers"])))
        producers.grid(row=5, column=0)
        licensors = ttk.Label(top, text="Licenciers : "+", ".join((i["name"] for i in self.anime["licensors"])))
        licensors.grid(row=6, column=0)
        if self.anime["premiered"]:
            season = ttk.Label(top, text="")
            self.main.translator.translate(season, "Season : "+self.anime["premiered"])
        else:
            season = ttk.Label(top, text="Saison : Inconnue")
        season.grid(row=7, column=0)

        genres = "Genres : " + \
                 ", ".join((self.main.translator.genre_translate(i["name"]) for i in self.anime["genres"]))
        genre = ttk.Label(top, text="".join(genres), justify="center")
        genre.grid(row=8, column=0)

        if self.anime["status"].startswith("Finished"):
            status = ttk.Label(top, text="Statut : Fini")
        elif self.anime["status"] == "Publishing":
            status = ttk.Label(top, text="Statut : En cours en publication")
        elif self.anime["status"] == "Not yet aired":
            status = ttk.Label(top, text="Statut : A Venir")
        else:
            status = ttk.Label(top, text="Statut : Inconnu")
        status.grid(row=9, column=0)

        if self.anime["episodes"]:
            ep = ttk.Label(top, text="Nombre d'Episodes : "+str(self.anime["episodes"]))
        else:
            ep = ttk.Label(top, text="Nombre d'Episodes : 0")
        ep.grid(row=10, column=0)

        stats_list = []
        if self.anime["rank"]:
            stats_list.append("Top : "+str(self.anime["rank"]))
        else:
            stats_list.append("Top : Inconnu")
        if self.anime["score"]:
            stats_list.append("    Score : "+str(self.anime["score"]))
        else:
            stats_list.append("    Score : Inconnu")
        if self.anime["popularity"]:
            stats_list.append("    Popularité : "+str(self.anime["popularity"]))
        else:
            stats_list.append("    Popularité : Inconnue")
        stats_list.append("\nNote : "+self.anime["rating"])
        stats_list.append("    Favoris : "+str(self.anime["favorites"]))
        stats = ttk.Label(top, text="".join(stats_list), justify="center")
        stats.grid(row=11, column=0)

        for i in range(13):
            top.rowconfigure(i, weight=1)
        for i in range(2):
            top.columnconfigure(i, weight=1)

        top.pack(fill="x")

        synopsis_label = ttk.Label(self, text="Synopsis :")
        synopsis_label.pack(pady=(20, 5))
        if self.anime["synopsis"]:
            synopsis = ttk.Label(self, text="", justify="center")
            self.main.translator.translate(synopsis, self.anime["synopsis"])
        else:
            synopsis = ttk.Label(self, text="Aucun", justify="center")
        synopsis.pack(pady=(5, 20))

        btn = ttk.Frame(self)

        episodes = ttk.Button(btn, text="Episodes", width=20,
                              command=lambda: self.main.show_page("episodes " + str(self.anime["mal_id"]) + " 1_" +
                                                                  self.anime["title"]))
        episodes.pack(side=LEFT, padx=20)
        trailer = ttk.Button(btn, text="Trailer", width=20,
                             command=lambda: open_url(self.anime["trailer_url"]))
        trailer.pack(side=LEFT, padx=20)
        news = ttk.Button(btn, text="News", width=20,
                          command=lambda: self.main.show_page("news " + str(self.anime["mal_id"]) + " a_" +
                                                              self.anime["title"]))
        news.pack(side=LEFT, padx=20)
        videos = ttk.Button(btn, text="Vidéos", width=20,
                            command=lambda: self.main.show_page("videos " + str(self.anime["mal_id"]) + " " +
                                                                self.anime["title"]))
        videos.pack(side=RIGHT, padx=20)
        images = ttk.Button(btn, text="Images", width=20,
                            command=lambda: self.main.show_page("images " + str(self.anime["mal_id"]) + " a_" +
                                                                self.anime["title"]))
        images.pack(side=RIGHT, padx=20)

        btn.pack(pady=10)

        btn2 = ttk.Frame(self)
        characters = ttk.Button(btn2, text="Personnages", width=20,
                                command=lambda: self.main.show_page("characters " + str(self.anime["mal_id"]) + " a_" +
                                                              self.anime["title"]))
        characters.pack(side=LEFT, padx=20)
        stats = ttk.Button(btn2, text="Statistiques", width=20,
                           command=lambda: self.main.show_page("stats " + str(self.anime["mal_id"]) + " a_" +
                                                               self.anime["title"]))
        stats.pack(side=LEFT, padx=20)
        recommands = ttk.Button(btn2, text="Recommandations", width=20,
                                command=lambda: self.main.show_page("recommands " + str(self.anime["mal_id"]) + " a_" +
                                                                    self.anime["title"]))
        recommands.pack(side=LEFT, padx=20)
        lien = ttk.Button(btn2, text="Lien MAL", width=20,
                          command=lambda: open_url(self.anime["url"]))
        lien.pack(side=RIGHT, padx=20)
        reviews = ttk.Button(btn2, text="Avis", width=20,
                             command=lambda: self.main.show_page("reviews " + str(self.anime["mal_id"]) + " a_1_" +
                                                                 self.anime["title"]))
        reviews.pack(side=RIGHT, padx=20)

        btn2.pack(pady=10)

        self.pack(side=RIGHT, fill=BOTH)

    def add_to_list(self):
        if self.anime["episodes"]:
            self.main.myanime.add(self.anime["mal_id"], self.anime["title"], self.anime["episodes"], self.anime["type"])
        else:
            self.main.myanime.add(self.anime["mal_id"], self.anime["title"], 0, self.anime["type"])
