from tkinter import *
import webbrowser

class Accueil(Frame):
    """Page d'accueil du logiciel"""
    def __init__(self, main, jikan):
        super(Accueil, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, text = "Accueil", font="-size 25 -weight bold")
        self.lTitre.pack(pady = 30)
        
        self.lInfos = Label(self, font = "-size 18", text = "Ce logiciel est un gestionnaire de manga / anime.\nMais il propose d'autres fonctionnalités :\n - Top d'anime/manga\n- Import de liste venant de MyAnimeList\n- Export de sa liste d'anime pour MyAnimeList\n\nIl a été créé par LavaPower\nVersion : 0.2.0 - Tops Update")
        self.lInfos.pack(pady=30)

        self.bGithub = Button(self, width = 10, font = "-size 18", text = "Github", command = lambda: self.openWeb("https://github.com/LavaPower/AList"))
        self.bGithub.pack(pady = 10)

        self.bWiki = Button(self, width = 10, font = "-size 18", text = "Wiki", command = lambda: self.openWeb("https://github.com/LavaPower/AList/wiki"))
        self.bWiki.pack(pady=10)

        self.bDiscord = Button(self, width = 10, font = "-size 18", text = "Discord", command = lambda: self.openWeb("https://discord.gg/kxdK7BZ"))
        self.bDiscord.pack(pady=10)

        self.pack(side=RIGHT)
    
    def openWeb(self, url):
        """Ouvre une page internet avec comme url <url>"""
        webbrowser.open(url)
