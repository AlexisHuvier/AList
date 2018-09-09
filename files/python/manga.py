from tkinter import *

class Manga(Frame):
    def __init__(self, main, jikan, malId):
        super(Manga, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.manga = self.jikan.manga(malId)
        if len(self.manga["title"]) < 15:
            self.lTitre = Label(self, text = self.manga["title"], font="-size 25 -weight bold")
        elif len(self.manga["title"]) < 25:
            self.lTitre = Label(self, text = self.manga["title"], font="-size 23 -weight bold")
        else:
            self.lTitre = Label(self, text = self.manga["title"], font="-size 21 -weight bold")
        self.lTitre.pack(pady = 10)
        self.pack(side=RIGHT)
