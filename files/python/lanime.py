from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename
from lxml import etree
import glob

class lAnime(Frame):
    def __init__(self, main, jikan):
        super(lAnime, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, text = "Liste de mes animes", font="-size 22 -weight bold")
        self.lTitre.pack(pady = 10)
        
        self.bLeft = Button(self, text = "<", command = self.showLeftPage)
        self.bLeft.pack(side = LEFT, padx = 10)
        self.bRight = Button(self, text = ">", command= self.showRightPage)
        self.bRight.pack(side = RIGHT, padx = 10)
        self.fAnimes = Frame(self)
        self.fAnimes.pack(pady = 5)
        self.fButtons = Frame(self)
        self.fButtons.pack(pady = 5)
        self.bImport = Button(self.fButtons, text = "Importer MAL")
        self.bImport.pack(side = LEFT, padx = 10)
        self.bExport = Button(self.fButtons, text = "Exporter MAL")
        self.bExport.pack(side = RIGHT, padx = 10)
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
        self.fAnimes.destroy()
        self.fButtons.destroy()
        self.fAnimes = Frame(self)
        self.fAnimes.pack(pady = 5)
        self.fButtons = Frame(self)
        self.fButtons.pack(pady = 5)
        self.bImport = Button(self.fButtons, text = "Importer MAL", command = self.importMAL)
        self.bImport.pack(side = LEFT, padx = 10)
        self.bExport = Button(self.fButtons, text = "Exporter MAL", command = self.exportMALFen)
        self.bExport.pack(side = RIGHT, padx = 10)
        if len(glob.glob("./files/anime/*.txt")) > 0:
            self.fList = Frame(self.fAnimes)
            self.fList.pack(side = LEFT, padx =10)
        if len(glob.glob("./files/anime/*.txt"))-6*self.page > 3:
            self.fList2 = Frame(self.fAnimes)
            self.fList2.pack(side = RIGHT, padx =10)
        for i in range(6):
            contenu = ""
            try:
                with open(glob.glob("./files/anime/*.txt")[i+6*self.page], "r") as fichier:
                    contenu += fichier.read()
            except:
                break
            infos = contenu.split("\n")
            if i < 3:
                self.fAnime = Frame(self.fList)
            else:
                self.fAnime = Frame(self.fList2)
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
    
    def importMAL(self):
        self.xmlMAL = askopenfilename(defaultextension='.xml', title = "Choisissez votre fichier exporté de MyAnimeList")
        if self.xmlMAL != "":
            try:
                tree = etree.parse(self.xmlMAL)
                for anime in tree.xpath("/myanimelist/anime"):
                    tempText = "ID : "+anime[0].text+"\nNom : "+anime[1].text+"\n"
                    if anime[12].text == "Watching":
                        tempText += "Status : En visionnement\n"
                    elif anime[12].text == "Completed":
                        tempText += "Status : Fini\n"
                    elif anime[12].text == "Plan to Watch":
                        tempText += "Status : A voir\n"
                    else:
                        tempText += "Status : Abandonné\n"
                    tempText += "Episodes : "+anime[5].text+"\nEpisodes Max : "+anime[3].text
                    tempText += "\nType : "+anime[2].text
                    with open("files/anime/"+anime[0].text+".txt", "w") as fichier:
                        fichier.write(tempText)
                showinfo("Import réussi", "Tous les animés ont été importés")
                self.main.showPage("lAnime")
            except:
                showerror("Erreur", "Sélectionnez un fichier valide")
        else:
            showerror("Erreur", "Sélectionnez un fichier valide")
    
    def exportMALFen(self):
        self.fen=Toplevel(self.main)
        self.e1=Entry(self.fen)
        self.e1.insert(0, "Pseudo")
        self.e1.pack(pady = 10)
        self.e2 = Entry(self.fen)
        self.e2.insert(0, "ID MAL")
        self.e2.pack(pady = 10)
        self.bValid = Button(self.fen, text = "Valider", command = self.exportMAL)
        self.bValid.pack(pady = 10)
        self.bQuit = Button(self.fen, text = "Annuler", command = fen.destroy)
        self.bQuit.pack(pady = 10)
    
    def exportMAL(self):
        if self.e1.get() in ["Pseudo", ""] or self.e2.get() in ["ID MAL", ""]:
            showerror("Erreur", "Entrez des valeurs valides") 
        else:
            try:
                pseudo = self.e1.get()
                idMAL = int(self.e2.get())
            except:
                showerror("Erreur", "Votre id n'est pas un nombre")
            else:
                print(pseudo, idMAL)
                self.fen.destroy()
                
                mal = etree.Element("myanimelist")
                    
                myinfo = etree.SubElement(mal, "myinfo")
                userid = etree.SubElement(myinfo, "user_id")
                userid.text = idMAL
                username = etree.SubElement(myinfo, "user_name")
                username.text = pseudo
                userexport = etree.SubElement(myinfo, "user_export_type")
                userexport.text = 1
            
                print(etree.tostring(users, pretty_print=True))
                
                showinfo("Export réussi", "Tous les animes ont été exportés")
        

