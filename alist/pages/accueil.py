from tkinter import ttk, TkVersion, TclVersion, RIGHT, BOTH

from alist.pages.right_page import RightPage
from alist.utils import utils
from alist import __version_num__, __version__


class Accueil(RightPage):
    def __init__(self, main):
        super(Accueil, self).__init__(main)
        title = ttk.Label(self, text="Accueil", font="-size 22 -weight bold")
        title.pack(pady=15)

        infos = ttk.Label(self, font="-size 16", text="Ce logiciel est un gestionnaire de manga / anime.\n"
                                                      "Mais il propose d'autres fonctionnalités.\n\n"
                                                      "Il a été créé par LavaPower avec LycosNovation\n"
                                                      "Version AList : " + __version__ + " (" + __version_num__ +
                                                      ")\nVersion Tkinter : " + str(TkVersion) +
                                                      "\nVersion Tcl : " + str(TclVersion), justify="center")
        infos.pack(pady=30)

        github = ttk.Button(self, width=10, text="GitHub",
                            command=lambda: utils.open_url("https://github.com/AlexisHuvier/AList"))
        github.pack(pady=15)

        discord = ttk.Button(self, width=10, text="Discord",
                             command=lambda: utils.open_url("https://discord.gg/UtpsTKTsTM"))
        discord.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
