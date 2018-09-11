from tkinter import *

class mManga(Frame):
    def __init__(self, main, jikan, malId):
        super(mManga, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        
        with open("./files/manga/"+malId+".txt", "r") as fichier:
            self.infos = fichier.read().split("\n")
        
        self.lTitre = Label(self, text = "Modification Manga\n"+self.infos[1].split(" : ")[1], font="-size 25 -weight bold")
        self.lTitre.pack(pady = 30)
        
        
        self.pack(side=RIGHT)
