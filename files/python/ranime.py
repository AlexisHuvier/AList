from tkinter import *
from tkinter.messagebox import showerror
from random import randint

class rAnime(Frame):
    """Page de recherche d'animé"""
    def __init__(self, main, jikan):
        super(rAnime, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, bg="#9f9f9f", text = "Rechercher un anime", font="-size 25 -weight bold")
        self.lTitre.pack(pady = 30)
        
        self.eSearch = Entry(self, font = "-size 15")
        self.eSearch.pack(pady = 10)
        self.bEntry = Button(self, text = "Rechercher", font = "-size 15", command = self.searchEntry)
        self.bEntry.pack(pady = 10)
        self.fResult = Frame(self, bg="#9f9f9f")
        self.fResult.pack(pady=10)
        self.pack(side=RIGHT)
    
    def searchEntry(self):
        """Valide la recherche"""
        if self.eSearch.get() == "":
            showerror("Erreur", "Entrez quelque chose à rechercher")
        else:
            self.fResult.destroy()
            self.fResult = Frame(self, bg="#9f9f9f")
            self.fResult.pack(pady=10)
            self.result = self.jikan.search("anime", self.eSearch.get())
            for i in range(5):
                if len(self.result["results"][i]["title"]) < 20:
                    self.bResult = Button(self.fResult, font="-size 15", width = 20, text = self.result["results"][i]["title"], command = lambda x=self.result["results"][i]["mal_id"]: self.openAnime(x))
                else:
                    self.bResult = Button(self.fResult, font="-size 15", width = 20, text = self.result["results"][i]["title"][:17]+"...", command = lambda x=self.result["results"][i]["mal_id"]: self.openAnime(x))
                self.bResult.pack(pady = 10)
    
    def openAnime(self, malId):
        """Ouvre la page présentant l'animé ayant l'id MAL <malId>"""
        self.main.showPage("anime|"+str(malId))
