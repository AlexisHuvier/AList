from tkinter import *
from tkinter.messagebox import askquestion

class Menu(Frame):
    def __init__(self, main):
        super(Menu, self).__init__(main, bg="#686868", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width = 200, height=600)
        self.main = main
        self.accueilButton = Button(self, command = lambda: self.showPage("accueil"), text = "Accueil")
        self.accueilButton.pack(padx=10,pady=35)
        self.rAnimeButton = Button(self, command = lambda: self.showPage("rAnime"), text = "Rechercher un Anime")
        self.rAnimeButton.pack(padx=10, pady=35)
        self.rMangaButton = Button(self, command = lambda: self.showPage("rManga"), text = "Rechercher un Manga")
        self.rMangaButton.pack(padx=10, pady=35)
        self.lAnimeButton = Button(self, command = lambda: self.showPage("lAnime"), text = "Liste de mes Animes")
        self.lAnimeButton.pack(padx=10, pady=35)
        self.lMangaButton = Button(self, command = lambda: self.showPage("lManga"), text = "Liste de mes Mangas")
        self.lMangaButton.pack(padx=10, pady=35)
        self.quitterButton = Button(self, command = self.quit, text = "Quitter")
        self.quitterButton.pack(padx=10, pady=35)
        self.pack(side = LEFT)
    
    def quit(self):
        if askquestion("Quitter", "Êtes-vous sûr de quitter ?") == "yes":
            self.main.destroy()
    
    def showPage(self, page):
        self.main.showPage(page)
        
        