from tkinter import ttk
from tkinter import *
from tkinter.messagebox import askquestion


class Menu(ttk.Frame):
    def __init__(self, main):
        super(Menu, self).__init__(main, relief=GROOVE)
        self.grid_propagate(False)
        self["padding"] = 30
        self.config(width=300, height=800)
        self.main = main

        self.home = ttk.Button(self, width=25, text="Accueil")
        self.home.grid(row=1)
        self.animes = ttk.Button(self, width=25, text="Liste Animes")
        self.animes.grid(row=2)
        self.mangas = ttk.Button(self, width=25, text="Liste Mangas")
        self.mangas.grid(row=3)
        self.lanimes = ttk.Button(self, width=25, text="Mes Animes")
        self.lanimes.grid(row=4)
        self.lmangas = ttk.Button(self, width=25, text="Mes Mangas")
        self.lmangas.grid(row=5)
        self.lmangas = ttk.Button(self, width=25, text="Paramètres")
        self.lmangas.grid(row=6)
        self.exit = ttk.Button(self, width=25, command=self.quit, text="Quitter")
        self.exit.grid(row=7)

        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=2)
        self.columnconfigure(0, weight=1)

        self.pack(side=LEFT, fill=BOTH)

    def quit(self):
        if askquestion("AList - Quitter", "Êtes-vous dûr de quitter ?") == "yes":
            self.main.destroy()
