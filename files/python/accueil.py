from tkinter import *

class Accueil(Frame):
    def __init__(self, main, jikan):
        super(Accueil, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.tManga = self.jikan.top(type='manga')
        self.tAnime = self.jikan.top(type='anime')
        self.lTitre = Label(self, text = "Accueil", font="-size 25 -weight bold")
        self.lTitre.pack(pady = 10)
        
        self.topManga = Frame(self)
        self.topManga.pack_propagate(False)
        self.topManga.config(width=400, height=600)
        self.lTitreTM = Label(self.topManga, text = "Top 10 Manga", font= "-size 22")
        self.lTitreTM.pack(pady = 10)
        for i in range(10):
            if len(self.tManga["top"][i]["title"]) < 20:
                self.lTitreM = Button(self.topManga, text = str(i+1) + ". "+self.tManga["top"][i]["title"], font = "-size 15", width = 20, command = lambda x=self.tManga["top"][i]["mal_id"]: self.openManga(x))
            else:
                self.lTitreM = Button(self.topManga, text = str(i+1) + ". "+self.tManga["top"][i]["title"][:17]+"...", width = 20, font = "-size 15", command = lambda x=self.tManga["top"][i]["mal_id"]: self.openManga(x))
            self.lTitreM.pack(pady=5)
        self.topManga.pack(side=RIGHT)

        self.topAnime = Frame(self)
        self.topAnime.pack_propagate(False)
        self.topAnime.config(width=400, height=600)
        self.lTitreTA = Label(self.topAnime, text = "Top 10 Anime", font= "-size 22")
        self.lTitreTA.pack(pady = 10)
        for i in range(10):
            if len(self.tAnime["top"][i]["title"]) < 20:
                self.lTitreA = Button(self.topAnime, text = str(i+1) + ". "+self.tAnime["top"][i]["title"], width = 20, font = "-size 15", command = lambda x=self.tAnime["top"][i]["mal_id"]: self.openAnime(x))
            else:
                self.lTitreA = Button(self.topAnime, text = str(i+1) + ". "+self.tAnime["top"][i]["title"][:17]+"...", width = 20, font = "-size 15", command = lambda x=self.tAnime["top"][i]["mal_id"]: self.openAnime(x))
            self.lTitreA.pack(pady=5)
        self.topAnime.pack(side=LEFT)
        
        self.pack(side=RIGHT)
    
    def openManga(self, malId):
        self.main.showPage("manga|"+str(malId))
    
    def openAnime(self, malId):
        self.main.showPage("anime|"+str(malId))
