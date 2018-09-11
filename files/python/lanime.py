from tkinter import *
from tkinter.messagebox import showerror
import glob

class lAnime(Frame):
    def __init__(self, main, jikan):
        super(lAnime, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, text = "Liste de mes animes", font="-size 25 -weight bold")
        self.lTitre.pack(pady = 10)
        
        self.bRight = Button(self, text = ">", command= self.showRightPage)
        self.bRight.pack(side = RIGHT, padx = 10)
        self.bLeft = Button(self, text = "<", command = self.showLeftPage)
        self.fAnimes2 = Frame(self)
        self.fAnimes2.pack(side = RIGHT, pady = 20, padx= 70)
        self.fAnimes = Frame(self)
        self.fAnimes.pack(pady = 25)
        self.bLeft.pack(side = LEFT, padx = 10)
        self.page = 0
        self.pageMax = len(glob.glob("./files/anime/*.txt"))//6
        
        self.createPage()
                
        self.pack(side=RIGHT)
    
    def showRightPage(self):
        if self.page == self.pageMax:
            self.page = 0
        else:
            self.page += 1
        self.createPage()
    
    def showLeftPage(self):
        if self.page == 0:
            self.page = self.pageMax
        else:
            self.page -= 1
        self.createPage()
        
    def createPage(self):
        self.fAnimes2.destroy()
        self.fAnimes.destroy()
        self.fAnimes2 = Frame(self)
        self.fAnimes2.pack(side = RIGHT, pady = 20, padx= 70)
        self.fAnimes = Frame(self)
        self.fAnimes.pack(pady = 25)
        for i in range(6):
            contenu = ""
            try:
                with open(glob.glob("./files/anime/*.txt")[i+6*self.page], "r") as fichier:
                    contenu += fichier.read()
            except:
                break
            infos = contenu.split("\n")
            if i < 3:
                self.fAnime = Frame(self.fAnimes)
            else:
                self.fAnime = Frame(self.fAnimes2)
            self.lAName = Label(self.fAnime, text = infos[1].split(" : ")[1], font = "-size 13")
            self.lAName.pack(pady=10)
            self.lAStatus = Label(self.fAnime, text = "Status : "+infos[2].split(" : ")[1], font = "-size 11")
            self.lAStatus.pack(pady=0)
            self.lAEp = Label(self.fAnime, text = "Episodes : "+infos[3].split(" : ")[1]+" / "+infos[4].split(" : ")[1], font = "-size 11")
            self.lAEp.pack(pady =5)
            self.bInfo = Button(self.fAnime, text = "Plus d'info", command = lambda x=infos[0].split(" : ")[1]: self.openAnime(x))
            self.bInfo.pack(side = RIGHT, pady =5, padx = 5)
            self.bModif = Button(self.fAnime, text = "Modifier", command = lambda x=infos[0].split(" : ")[1]: self.modifyAnime(x))
            self.bModif.pack(pady = 5, padx = 5)
            self.fAnime.pack(pady = 10)
    
    def openAnime(self, malId):
        self.main.showPage("anime|"+str(malId))
    
    def modifyAnime(self, malId):
        self.main.showPage("animeM|"+str(malId))

