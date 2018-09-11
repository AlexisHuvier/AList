from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename
from lxml import etree
import glob

class lManga(Frame):
    def __init__(self, main, jikan):
        super(lManga, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, text = "Liste de mes mangas", font="-size 25 -weight bold")
        self.lTitre.pack(pady = 10)
        self.bLeft = Button(self, text = "<", command = self.showLeftPage)
        self.bLeft.pack(side = LEFT, padx = 10)
        self.bRight = Button(self, text = ">", command= self.showRightPage)
        self.bRight.pack(side = RIGHT, padx = 10)
        self.fMangas = Frame(self)
        self.fMangas.pack(pady = 5)
        self.fButtons = Frame(self)
        self.fButtons.pack(pady = 5)
        self.bImport = Button(self.fButtons, text = "Importer MAL")
        self.bImport.pack(side = LEFT, padx = 10)
        self.bExport = Button(self.fButtons, text = "Exporter MAL")
        self.bExport.pack(side = RIGHT, padx = 10)
        self.page = 0
        self.pageMax = len(glob.glob("./files/manga/*.txt"))//6
        
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
        self.fMangas.destroy()
        self.fButtons.destroy()
        self.fMangas = Frame(self)
        self.fMangas.pack(pady = 5)
        self.fButtons = Frame(self)
        self.fButtons.pack(pady = 5)
        self.bImport = Button(self.fButtons, text = "Importer MAL", command = self.importMAL)
        self.bImport.pack(side = LEFT, padx = 10)
        self.bExport = Button(self.fButtons, text = "Exporter MAL")
        self.bExport.pack(side = RIGHT, padx = 10)
        if len(glob.glob("./files/manga/*.txt")) > 0:
            self.fList = Frame(self.fMangas)
            self.fList.pack(side = LEFT, padx =10)
        if len(glob.glob("./files/manga/*.txt"))-6*self.page > 3:
            self.fList2 = Frame(self.fMangas)
            self.fList2.pack(side = RIGHT, padx =10)
        for i in range(6):
            contenu = ""
            try:
                with open(glob.glob("./files/manga/*.txt")[i+6*self.page], "r") as fichier:
                    contenu += fichier.read()
            except:
                break
            infos = contenu.split("\n")
            if i < 3:
                self.fManga = Frame(self.fList)
            else:
                self.fManga = Frame(self.fList2)
            self.lAName = Label(self.fManga, text = infos[1].split(" : ")[1], font = "-size 13")
            self.lAName.pack(pady=10)
            self.lAStatus = Label(self.fManga, text = "Status : "+infos[2].split(" : ")[1], font = "-size 11")
            self.lAStatus.pack(pady=0)
            self.lAEp = Label(self.fManga, text = "Chapitres : "+infos[3].split(" : ")[1]+" / "+infos[4].split(" : ")[1], font = "-size 11")
            self.lAEp.pack(pady =5)
            self.bInfo = Button(self.fManga, text = "Plus d'info", command = lambda x=infos[0].split(" : ")[1]: self.openManga(x))
            self.bInfo.pack(side = RIGHT, pady =5, padx = 5)
            self.bModif = Button(self.fManga, text = "Modifier", command = lambda x=infos[0].split(" : ")[1]: self.modifyManga(x))
            self.bModif.pack(pady = 5, padx = 5)
            self.fManga.pack(pady = 10)
    
    def openManga(self, malId):
        self.main.showPage("manga|"+str(malId))
    
    def modifyManga(self, malId):
        self.main.showPage("mangaM|"+str(malId))
    
    def importMAL(self):
        self.xmlMAL = askopenfilename(defaultextension='.xml', title = "Choisissez votre fichier exporté de MyAnimeList")
        if self.xmlMAL != "":
            try:
                tree = etree.parse(self.xmlMAL)
                for manga in tree.xpath("/myanimelist/manga"):
                    tempText = "ID : "+manga[0].text+"\nNom : "+manga[1].text+"\n"
                    if manga[12].text == "Reading":
                        tempText += "Status : En visionnement\n"
                    elif manga[12].text == "Completed":
                        tempText += "Status : Fini\n"
                    elif manga[12].text == "Plan to Watch":
                        tempText += "Status : A voir\n"
                    else:
                        tempText += "Status : Abandonné\n"
                    tempText += "Chapitres : "+manga[6].text+"\nChapitres Max : "+manga[3].text
                    with open("files/manga/"+manga[0].text+".txt", "w") as fichier:
                        fichier.write(tempText)
                showinfo("Import réussi", "Tous les mangas ont été importés")
                self.main.showPage("lManga")
            except:
                showerror("Erreur", "Sélectionnez un fichier valide")
        else:
            showerror("Erreur", "Sélectionnez un fichier valide")
