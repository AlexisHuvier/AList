from tkinter import *
from tkinter.messagebox import showerror
from datetime import datetime
from random import randint

class Tops(Frame):
    def __init__(self, main, jikan):
        super(Tops, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, text = "Tops", font="-size 25 -weight bold")
        self.lTitre.pack(pady = 10)
        self.idDuJour = 10+datetime.now().year//datetime.now().month*datetime.now().day

        self.fTop = Frame(self)
        self.vTop = StringVar(self)
        self.vTop.set("Choisissez un top") # default value
        self.menuTop = OptionMenu(self.fTop, self.vTop, "Choisissez un top", "Anime depuis toujours", "Manga depuis toujours", "Anime du jour", "Manga du jour", "Anime au hasard", "Manga au hasard")
        self.menuTop["width"] = 20
        self.menuTop.pack(side = LEFT, padx = 100, pady = 5)
        self.bValide = Button(self.fTop, width = 20, text = "Valider", command = self.valide)
        self.bValide.pack(side = RIGHT, padx = 100, pady = 5)
        self.fTop.pack(pady = 5)

        self.fTops = Frame(self)
        self.fTops.pack()

        self.pack(side=RIGHT)
    
    def valide(self):
        self.fTops.destroy()
        if self.vTop.get() == "Anime depuis toujours":
            self.tAnime = self.jikan.top(type='anime')
            self.fTops = Frame(self)
            self.fTops.pack_propagate(False)
            self.fTops.config(width=600, height=480)
            self.lTitreTA = Label(self.fTops, text = "Top 10 Anime", font= "-size 20")
            self.lTitreTA.pack(pady = 10)
            for i in range(10):
                if len(self.tAnime["top"][i]["title"]) < 40:
                    self.lTitreA = Button(self.fTops, text = str(i+1) + ". "+self.tAnime["top"][i]["title"], width = 40, font = "-size 13", command = lambda x=self.tAnime["top"][i]["mal_id"]: self.openAnime(x))
                else:
                    self.lTitreA = Button(self.fTops, text = str(i+1) + ". "+self.tAnime["top"][i]["title"][:37]+"...", width = 40, font = "-size 13", command = lambda x=self.tAnime["top"][i]["mal_id"]: self.openAnime(x))
                self.lTitreA.pack(pady=3)
            self.fTops.pack()
        elif self.vTop.get() == "Manga depuis toujours":
            self.tManga = self.jikan.top(type='manga')

            self.fTops = Frame(self)
            self.fTops.pack_propagate(False)
            self.fTops.config(width=600, height=480)
            self.lTitreTM = Label(self.fTops, text = "Top 10 Manga", font= "-size 20")
            self.lTitreTM.pack(pady = 10)
            for i in range(10):
                if len(self.tManga["top"][i]["title"]) < 40:
                    self.lTitreM = Button(self.fTops, text = str(i+1) + ". "+self.tManga["top"][i]["title"], font = "-size 13", width = 40, command = lambda x=self.tManga["top"][i]["mal_id"]: self.openManga(x))
                else:
                    self.lTitreM = Button(self.fTops, text = str(i+1) + ". "+self.tManga["top"][i]["title"][:37]+"...", width = 40, font = "-size 13", command = lambda x=self.tManga["top"][i]["mal_id"]: self.openManga(x))
                self.lTitreM.pack(pady=3)
            self.fTops.pack()
        elif self.vTop.get() == "Anime du jour":
            self.animeAlea = {"error" : "test"}
            boucle = 0
            while True:
                try:
                    if self.animeAlea["error"]:
                        try:
                            self.animeAlea = self.jikan.anime(self.idDuJour+boucle)
                        except:
                            boucle += 1
                            self.animeAlea = {"error" : "test"}
                except:
                    break
            self.fTops = Frame(self)
            self.fTops.pack_propagate(False)
            self.fTops.config(width=600, height=480)
            self.lTitreTM = Label(self.fTops, text = "Anime du jour", font= "-size 20")
            self.lTitreTM.pack(pady = 10)
            if len(self.animeAlea["title"]) < 40:
                self.lTitreM = Button(self.fTops, text = self.animeAlea["title"], font = "-size 13", width = 40, command = lambda x=self.animeAlea["mal_id"]: self.openAnime(x))
            else:
                self.lTitreM = Button(self.fTops, text = self.animeAlea["title"][:37]+"...", width = 40, font = "-size 13", command = lambda x=self.animeAlea["mal_id"]: self.openAnime(x))
            self.lTitreM.pack(pady=3)
            self.fTops.pack()
        elif self.vTop.get() == "Manga du jour":
            self.mangaAlea = {"error" : "test"}
            boucle = 0
            while True:
                try:
                    if self.mangaAlea["error"]:
                        try:
                            self.mangaAlea = self.jikan.manga(self.idDuJour+boucle)
                        except:
                            boucle += 1
                            self.mangaAlea = {"error" : "test"}
                except:
                    break
            self.fTops = Frame(self)
            self.fTops.pack_propagate(False)
            self.fTops.config(width=600, height=480)
            self.lTitreTM = Label(self.fTops, text = "Manga du jour", font= "-size 20")
            self.lTitreTM.pack(pady = 10)
            if len(self.mangaAlea["title"]) < 40:
                self.lTitreM = Button(self.fTops, text = self.mangaAlea["title"], font = "-size 13", width = 40, command = lambda x=self.mangaAlea["mal_id"]: self.openManga(x))
            else:
                self.lTitreM = Button(self.fTops, text = self.mangaAlea["title"][:37]+"...", width = 40, font = "-size 13", command = lambda x=self.mangaAlea["mal_id"]: self.openManga(x))
            self.lTitreM.pack(pady=3)
            self.fTops.pack()
        elif self.vTop.get() == "Anime au hasard":
            self.animeAlea = {"error" : "test"}
            while True:
                try:
                    if self.animeAlea["error"]:
                        try:
                            self.animeAlea = self.jikan.anime(randint(1, 50000))
                        except:
                            self.animeAlea = {"error" : "test"}
                except:
                    break
            self.fTops = Frame(self)
            self.fTops.pack_propagate(False)
            self.fTops.config(width=600, height=480)
            self.lTitreTM = Label(self.fTops, text = "Anime du jour", font= "-size 20")
            self.lTitreTM.pack(pady = 10)
            if len(self.animeAlea["title"]) < 40:
                self.lTitreM = Button(self.fTops, text = self.animeAlea["title"], font = "-size 13", width = 40, command = lambda x=self.animeAlea["mal_id"]: self.openAnime(x))
            else:
                self.lTitreM = Button(self.fTops, text = self.animeAlea["title"][:37]+"...", width = 40, font = "-size 13", command = lambda x=self.animeAlea["mal_id"]: self.openAnime(x))
            self.lTitreM.pack(pady=3)
            self.fTops.pack()
        elif self.vTop.get() == "Manga au hasard":
            self.mangaAlea = {"error" : "test"}
            while True:
                try:
                    if self.mangaAlea["error"]:
                        try:
                            self.mangaAlea = self.jikan.manga(randint(1, 50000))
                        except:
                            self.mangaAlea = {"error" : "test"}
                except:
                    break
            self.fTops = Frame(self)
            self.fTops.pack_propagate(False)
            self.fTops.config(width=600, height=480)
            self.lTitreTM = Label(self.fTops, text = "Manga du jour", font= "-size 20")
            self.lTitreTM.pack(pady = 10)
            if len(self.mangaAlea["title"]) < 40:
                self.lTitreM = Button(self.fTops, text = self.mangaAlea["title"], font = "-size 13", width = 40, command = lambda x=self.mangaAlea["mal_id"]: self.openManga(x))
            else:
                self.lTitreM = Button(self.fTops, text = self.mangaAlea["title"][:37]+"...", width = 40, font = "-size 13", command = lambda x=self.mangaAlea["mal_id"]: self.openManga(x))
            self.lTitreM.pack(pady=3)
            self.fTops.pack()
        elif self.vTop.get() == "Choisissez un top":
            showerror("Erreur", "Selectionnez un top.")
        else:
            showerror("Erreur", "Ce top n'est pas encore disponible")
            self.fTops = Frame(self)
            self.fTops.pack()
    
    def openManga(self, malId):
        self.main.showPage("manga|"+str(malId))
    
    def openAnime(self, malId):
        self.main.showPage("anime|"+str(malId))