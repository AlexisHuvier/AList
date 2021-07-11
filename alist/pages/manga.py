from tkinter import ttk, RIGHT, BOTH, LEFT

from alist.pages.right_page import RightPage
from alist.utils import utils


class Manga(RightPage):
    def __init__(self, main, mal_id):
        super(Manga, self).__init__(main)
        self.mal_id = mal_id
        self.manga = self.main.mal.manga(mal_id)

        title = ttk.Label(self, text=self.manga["title"], font="-size 20 -weight bold")
        title.pack(pady=15)

        manga = ttk.Frame(self)

        image = ttk.Label(manga)
        self.main.imager.apply_image_on_label("manga_" + str(self.manga["mal_id"]) + ".jpg",
                                              self.manga["image_url"],
                                              image)
        image.pack(side=RIGHT, padx=50)

        type_ = ttk.Label(manga, text="Type : Manga")
        type_.pack(pady=5)
        if self.manga["title_english"]:
            en_title = ttk.Label(manga, text="Titre Anglais : "+self.manga["title_english"])
        else:
            en_title = ttk.Label(manga, text="Titre Anglais : Aucun")
        en_title.pack(pady=5)
        if len(self.manga["authors"][0]["name"].split(", ")) == 2:
            author = ttk.Label(manga, text="Auteur principal : "+self.manga["authors"][0]["name"].split(", ")[1]+" " +
                                           self.manga["authors"][0]["name"].split(", ")[0])
        else:
            author = ttk.Label(manga, text="Auteur pricipal : "+self.manga["authors"][0]["name"])
        author.pack(pady=5)

        genres = ["Genres : "]
        for k, v in enumerate(self.manga["genres"]):
            if k != 0:
                if k % 7 == 0: # Retour à ligne tous les 5 genres
                    genres.append(", \n")
                else:
                    genres.append(", ")
            genres.append(self.main.translator.manuel_translate(v["name"]))
        genre = ttk.Label(manga, text="".join(genres), justify="center")
        genre.pack(pady=5)

        if self.manga["status"].startswith("Finished"):
            status = ttk.Label(manga, text="Statut : Fini")
        elif self.manga["status"] == "Publishing":
            status = ttk.Label(manga, text="Statut : En cours en publication")
        elif self.manga["status"] == "Not yet aired":
            status = ttk.Label(manga, text="Statut : A Venir")
        else:
            status = ttk.Label(manga, text="Statut : Inconnu")
        status.pack(pady=5)

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
        vol_chap.pack(pady=5)

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
        stats = ttk.Label(manga, text="".join(stats_list))
        stats.pack(pady=5)

        synopsis_list = ["Synopsis :\n"]
        if self.manga["synopsis"]:
            mots = self.main.translator.translate(self.manga["synopsis"]).split(" ")
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
        synopsis = ttk.Label(manga, text="".join(synopsis_list), justify="center")
        synopsis.pack(pady=20)

        manga.pack()

        buttons = ttk.Frame(self)

        lien = ttk.Button(buttons, text="Lien MAL", width=20,
                          command=lambda: utils.open_url(self.manga["url"]))
        lien.pack(side=LEFT, padx=20)
        add_list = ttk.Button(buttons, text="Ajouter à ma liste", width=20, command=self.add_to_list)
        add_list.pack(side=RIGHT, padx=20)

        buttons.pack(pady=10)

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
