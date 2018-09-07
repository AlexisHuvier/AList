from tkinter import *

class lAnime(Frame):
    def __init__(self, main, jikan):
        super(lAnime, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, text = "Liste de mes animes", font="-size 25 -weight bold")
        self.lTitre.pack(pady = 10)
        self.pack(side=RIGHT)