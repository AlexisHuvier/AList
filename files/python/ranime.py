from tkinter import *
from tkinter.messagebox import showerror
from random import randint

class rAnime(Frame):
    def __init__(self, main, jikan):
        super(rAnime, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, text = "Rechercher un anime", font="-size 25 -weight bold")
        self.lTitre.pack(pady = 30)
        
        self.eSearch = Entry(self, font = "-size 15")
        self.eSearch.pack(pady = 10)
        self.bEntry = Button(self, text = "Rechercher", font = "-size 15", command = self.searchEntry)
        self.bEntry.pack(pady = 10)
        self.bAlea = Button(self, text = "Au hasard", font = "-size 15", command = self.searchAlea)
        self.bAlea.pack(pady = 10)
        self.fResult = Frame(self)
        self.fResult.pack(pady=10)
        self.pack(side=RIGHT)
    
    def searchEntry(self):
        if self.eSearch.get() == "":
            showerror("Erreur", "Entrez quelque chose à rechercher")
        else:
            self.fResult.destroy()
            self.fResult = Frame(self)
            self.fResult.pack(pady=10)
            self.result = self.jikan.search("anime", self.eSearch.get())
            for i in range(5):
                if len(self.result["results"][i]["title"]) < 20:
                    self.bResult = Button(self.fResult, font="-size 15", width = 20, text = self.result["results"][i]["title"], command = lambda x=self.result["results"][i]["mal_id"]: self.openAnime(x))
                else:
                    self.bResult = Button(self.fResult, font="-size 15", width = 20, text = self.result["results"][i]["title"][:17]+"...", command = lambda x=self.result["results"][i]["mal_id"]: self.openAnime(x))
                self.bResult.pack(pady = 10)
            
    def searchAlea(self):
        self.fResult.destroy()
        self.fResult = Frame(self)
        self.fResult.pack(pady=10)
        self.animeAlea = {"error" : "test"}
        while True:
            try:
                if self.animeAlea["error"]:
                    try:
                        self.animeAlea = self.jikan.anime(randint(1, 38145))
                    except:
                        self.animeAlea = {"error" : "test"}
            except:
                break
        if len(self.animeAlea["title"]) < 20:
            self.bResult = Button(self.fResult, font="-size 15", width = 20, text = self.animeAlea["title"], command = lambda x=self.animeAlea["mal_id"]: self.openAnime(x))
        else:
            self.bResult = Button(self.fResult, font="-size 15", width = 20, text = self.animeAlea["title"][:17]+"...", command = lambda x=self.animeAlea["mal_id"]: self.openAnime(x))
        self.bResult.pack(pady = 10)
    
    def openAnime(self, malId):
        self.main.showPage("anime|"+str(malId))
