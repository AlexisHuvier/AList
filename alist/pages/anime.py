from tkinter import ttk, RIGHT, BOTH, Frame, LEFT

from alist.pages.right_page import RightPage
from alist.utils import utils


class Anime(RightPage):
    def __init__(self, main, mal_id):
        super(Anime, self).__init__(main)
        self.mal_id = mal_id
        self.anime = self.main.mal.anime(mal_id)

        title = ttk.Label(self, text=self.anime["title"], font="-size 20 -weight bold")
        title.pack(pady=15)

        anime = Frame(self)

        image = ttk.Label(anime)
        self.main.imager.apply_image_on_label("anime_" + str(self.anime["mal_id"]) + ".jpg",
                                              self.anime["image_url"],
                                              image)
        image.pack(side=RIGHT, padx=50)

        type_ = ttk.Label(anime, text="Type : Anime")
        type_.pack(pady=5)
        if self.anime["title_english"]:
            en_title = ttk.Label(anime, text="Titre Anglais : "+self.anime["title_english"])
        else:
            en_title = ttk.Label(anime, text="Titre Anglais : Aucun")
        en_title.pack(pady=5)
        author = ttk.Label(anime, text="Studio Principal : "+self.anime["studios"][0]["name"])
        author.pack(pady=5)

        genres = ["Genres : "]
        for k, v in enumerate(self.anime["genres"]):
            if k != 0:
                if k % 7 == 0: # Retour à ligne tous les 5 genres
                    genres.append(", \n")
                else:
                    genres.append(", ")
            genres.append(self.main.translator.manuel_translate(v["name"]))
        genre = ttk.Label(anime, text="".join(genres), justify="center")
        genre.pack(pady=5)

        if self.anime["status"].startswith("Finished"):
            status = ttk.Label(anime, text="Statut : Fini")
        elif self.anime["status"] == "Publishing":
            status = ttk.Label(anime, text="Statut : En cours en publication")
        elif self.anime["status"] == "Not yet aired":
            status = ttk.Label(anime, text="Statut : A Venir")
        else:
            status = ttk.Label(anime, text="Statut : Inconnu")
        status.pack(pady=5)

        if self.anime["episodes"]:
            ep = ttk.Label(anime, text="Nombre d'Episodes : "+str(self.anime["episodes"]))
        else:
            ep = ttk.Label(anime, text="Nombre d'Episodes : 0")
        ep.pack(pady=5)

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
        stats = ttk.Label(anime, text="".join(stats_list))
        stats.pack(pady=5)

        synopsis_list = ["Synopsis :\n"]
        if self.anime["synopsis"]:
            mots = self.main.translator.translate(self.anime["synopsis"]).split(" ")
            nb = 80
            lignes = 0
            for i in mots:
                if nb - len(i) <= 0:
                    nb = 80 - len(i)
                    lignes += 1
                    if lignes == 20:
                        synopsis_list.append("...")
                        break
                    else:
                        synopsis_list.extend(("\n", i, " "))
                else:
                    synopsis_list.extend((i, " "))
                    nb -= len(i)
        else:
            synopsis_list.append("Aucun")
        synopsis = ttk.Label(anime, text="".join(synopsis_list), justify="center")
        synopsis.pack(pady=20)

        anime.pack()

        buttons = Frame(self)

        lien = ttk.Button(buttons, text="Lien MAL", width=20,
                          command=lambda: utils.open_url(self.anime["url"]))
        lien.pack(side=LEFT, padx=20)
        trailer = ttk.Button(buttons, text="Trailer", width=20,
                             command=lambda: utils.open_url(self.anime["trailer_url"]))
        trailer.pack(side=RIGHT, padx=20)
        add_list = ttk.Button(buttons, text="Ajouter à ma liste", width=20)
        add_list.pack(padx=20)

        buttons.pack(pady=10)

        self.pack(side=RIGHT, fill=BOTH)

