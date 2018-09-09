from tkinter import *

class Anime(Frame):
    def __init__(self, main, jikan, malId):
        super(Anime, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.anime = self.jikan.anime(malId)
        if len(self.anime["title"]) < 15:
            self.lTitre = Label(self, text = self.anime["title"], font="-size 25 -weight bold")
        elif len(self.anime["title"]) < 25:
            self.lTitre = Label(self, text = self.anime["title"], font="-size 23 -weight bold")
        else:
            self.lTitre = Label(self, text = self.anime["title"], font="-size 21 -weight bold")
        self.lTitre.pack(pady = 10)
        self.pack(side=RIGHT)
