from tkinter import *
from tkinter.messagebox import showerror
from random import randint

class rManga(Frame):
    def __init__(self, main, jikan):
        super(rManga, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, text = "Rechercher un manga", font="-size 25 -weight bold")
        self.lTitre.pack(pady = 30)
        
        self.eSearch = Entry(self, font = "-size 15")
        self.eSearch.pack(pady = 10)
        self.bEntry = Button(self, text = "Rechercher", font = "-size 15", command = self.searchEntry)
        self.bEntry.pack(pady = 10)
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
            self.result = self.jikan.search("manga", self.eSearch.get())
            for i in range(5):
                if len(self.result["results"][i]["title"]) < 20:
                    self.bResult = Button(self.fResult, font="-size 15", width = 20, text = self.result["results"][i]["title"], command = lambda x=self.result["results"][i]["mal_id"]: self.openManga(x))
                else:
                    self.bResult = Button(self.fResult, font="-size 15", width = 20, text = self.result["results"][i]["title"][:17]+"...", command = lambda x=self.result["results"][i]["mal_id"]: self.openManga(x))
                self.bResult.pack(pady = 10)
            
    def openManga(self, malId):
        self.main.showPage("manga|"+str(malId))
