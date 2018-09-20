from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from lxml import etree
import glob

class lManga(Frame):
    """Page qui liste ses mangas"""
    def __init__(self, main, jikan):
        super(lManga, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.lTitre = Label(self, bg="#9f9f9f", text = "Liste de mes mangas", font="-size 22 -weight bold")
        self.lTitre.pack(pady = 10)
        self.bLeft = Button(self, text = "<", command = self.showLeftPage)
        self.bLeft.pack(side = LEFT, padx = 10)
        self.bRight = Button(self, text = ">", command= self.showRightPage)
        self.bRight.pack(side = RIGHT, padx = 10)
        self.fMangas = Frame(self, bg="#9f9f9f")
        self.fMangas.pack(pady = 5)
        self.fButtons = Frame(self, bg="#9f9f9f")
        self.fButtons.pack(pady = 5)
        self.bImport = Button(self.fButtons, text = "Importer MAL", command = self.importMAL)
        self.bImport.pack(side = LEFT, padx = 10)
        self.bExport = Button(self.fButtons, text = "Exporter MAL", command = self.exportMALFen)
        self.bExport.pack(side = RIGHT, padx = 10)
        self.page = 0
        self.pageMax = len(glob.glob("./files/manga/*.txt"))//6
                
        self.LMWatching, self.LMToWatch, self.LMDropped, self.LMFinish = [], [], [], []
        for i in glob.glob("./files/manga/*.txt"):
            with open(i, "r") as fichier:
                infos = fichier.read().split("\n")
            if infos[2].split(" : ")[1] == "En visionnement":
                self.LMWatching.append(i)
            elif infos[2].split(" : ")[1] == "Fini":
                self.LMFinish.append(i)
            elif infos[2].split(" : ")[1] == "A voir":
                self.LMToWatch.append(i)
            else:
                self.LMDropped.append(i)
        self.listeMangas = self.LMWatching + self.LMToWatch + self.LMFinish + self.LMDropped

        self.createPage()
                
        self.pack(side=RIGHT)
    
    def showRightPage(self):
        """Affiche la page suivante"""
        if self.page == self.pageMax:
            self.page = 0
        else:
            self.page += 1
        self.createPage()
    
    def showLeftPage(self):
        """Affiche la page précédente"""
        if self.page == 0:
            self.page = self.pageMax
        else:
            self.page -= 1
        self.createPage()
        
    def createPage(self):
        """Créer la page à afficher puis l'affiche"""
        self.fMangas.destroy()
        self.fButtons.destroy()
        self.fMangas = Frame(self, bg="#9f9f9f")
        self.fMangas.pack(pady = 5)
        self.fButtons = Frame(self, bg="#9f9f9f")
        self.fButtons.pack(pady = 5)
        self.bImport = Button(self.fButtons, text = "Importer MAL", command = self.importMAL)
        self.bImport.pack(side = LEFT, padx = 10)
        self.bExport = Button(self.fButtons, text = "Exporter MAL", command = self.exportMALFen)
        self.bExport.pack(side = RIGHT, padx = 10)
        if len(self.listeMangas) > 0:
            self.fList = Frame(self.fMangas, bg="#9f9f9f")
            self.fList.pack(side = LEFT, padx =10)
        if len(self.listeMangas)-6*self.page > 3:
            self.fList2 = Frame(self.fMangas, bg="#9f9f9f")
            self.fList2.pack(side = RIGHT, padx =10)
        for i in range(6):
            contenu = ""
            try:
                with open(self.listeMangas[i+6*self.page], "r") as fichier:
                    contenu += fichier.read()
            except:
                break
            infos = contenu.split("\n")
            if i < 3:
                self.fManga = Frame(self.fList, bg="#9f9f9f", relief = "ridge", borderwidth = 5)
            else:
                self.fManga = Frame(self.fList2, bg="#9f9f9f", relief = "ridge", borderwidth = 5)
            self.fManga.pack_propagate(False)
            self.fManga.config(width=300, height=150)
            if len(infos[1].split(" : ")[1]) < 30:
                self.lAName = Label(self.fManga, bg="#9f9f9f", text = infos[1].split(" : ")[1], font = "-size 13")
            else:
                self.lAName = Label(self.fManga, bg="#9f9f9f", text = infos[1].split(" : ")[1][:27]+"...", font = "-size 13")
            self.lAName.pack(pady=5)
            self.lAStatus = Label(self.fManga, bg="#9f9f9f", text = "Status : "+infos[2].split(" : ")[1], font = "-size 11")
            self.lAStatus.pack(pady=0)
            self.lAVol = Label(self.fManga, bg="#9f9f9f", text = "Volumes : "+infos[3].split(" : ")[1]+" / "+infos[4].split(" : ")[1], font = "-size 11")
            self.lAVol.pack(pady =0)
            self.lAEp = Label(self.fManga, bg="#9f9f9f", text = "Chapitres : "+infos[5].split(" : ")[1]+" / "+infos[6].split(" : ")[1], font = "-size 11")
            self.lAEp.pack(pady =0)
            self.fButtonsManga = Frame(self.fManga, bg = "#9f9f9f")
            self.bInfo = Button(self.fButtonsManga, text = "Plus d'info", command = lambda x=infos[0].split(" : ")[1]: self.openManga(x))
            self.bInfo.pack(side = RIGHT, padx = 5)
            self.bModif = Button(self.fButtonsManga, text = "Modifier", command = lambda x=infos[0].split(" : ")[1]: self.modifyManga(x))
            self.bModif.pack(side = LEFT, padx = 5)
            self.fButtonsManga.pack(pady = 5)
            self.fManga.pack(pady = 5)
    
    def openManga(self, malId):
        """Ouvre une page présentant le manga dont l'id MAL est <malId>"""
        self.main.showPage("manga|"+str(malId))
    
    def modifyManga(self, malId):
        """Ouvre une page pour modifier les infos enregistrés pour le manga ayant comme id MAL <malId>"""
        self.main.showPage("mangaM|"+str(malId))
    
    def importMAL(self):
        """Import un .xml exporté de MyAnimeList"""
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
                    tempText += "Volumes : "+manga[5].text+"\nVolumes Max : "+manga[2].text
                    tempText += "\nChapitres : "+manga[6].text+"\nChapitres Max : "+manga[3].text
                    tempText += "\nType : Manga"
                    with open("files/manga/"+manga[0].text+".txt", "w") as fichier:
                        fichier.write(tempText)
                showinfo("Import réussi", "Tous les mangas ont été importés")
                self.main.showPage("reload")
            except:
                showerror("Erreur", "Sélectionnez un fichier valide")
        else:
            showerror("Erreur", "Sélectionnez un fichier valide")
    
    def exportMALFen(self):
        """Ouvre une fenêtre pour récupérer les informations utiles à l'export pour MAL"""
        self.fen=Toplevel(self.main)
        self.e1=Entry(self.fen)
        self.e1.insert(0, "Pseudo")
        self.e1.pack(pady = 10)
        self.e2 = Entry(self.fen)
        self.e2.insert(0, "ID MAL")
        self.e2.pack(pady = 10)
        self.bValid = Button(self.fen, text = "Valider", command = self.exportMAL)
        self.bValid.pack(pady = 10)
        self.bQuit = Button(self.fen, text = "Annuler", command = self.fen.destroy)
        self.bQuit.pack(pady = 10)
    
    def exportMAL(self):
        """Export la liste dans .xml pour MAL"""
        if self.e1.get() in ["Pseudo", ""] or self.e2.get() in ["ID MAL", ""]:
            showerror("Erreur", "Entrez des valeurs valides") 
        else:
            showerror("Erreur", "L'export de manga pour MAL est actuellement indisponible.\nMAL a désactivé son import pour les mangas.")
            """try:
                pseudo = self.e1.get()
                idMAL = int(self.e2.get())
            except:
                showerror("Erreur", "Votre id n'est pas un nombre")
            else:
                self.fen.destroy()
                
                totalmanga = 0
                watchingmanga = 0
                completemanga = 0
                onholdmanga = 0
                droppedmanga = 0
                plantowatchmanga = 0
                for i in glob.glob("./files/manga/*.txt"):
                    totalmanga += 1
                    with open(i, "r") as fichier:
                        contenu = fichier.read()
                        if contenu.split("\n")[2].split(" : ")[1] == "En visionnement":
                            watchingmanga += 1
                        elif contenu.split("\n")[2].split(" : ")[1] == "Fini":
                            completemanga += 1
                        elif contenu.split("\n")[2].split(" : ")[1] == "A voir":
                            plantowatchmanga += 1
                        else:
                            droppedmanga += 1
                            
                mal = etree.Element("myanimelist")
                    
                myinfo = etree.SubElement(mal, "myinfo")
                userid = etree.SubElement(myinfo, "user_id")
                userid.text = str(idMAL)
                username = etree.SubElement(myinfo, "user_name")
                username.text = pseudo
                userexport = etree.SubElement(myinfo, "user_export_type")
                userexport.text = "2"
                usertotal = etree.SubElement(myinfo, "user_total_manga")
                usertotal.text = str(totalmanga)
                userwatching = etree.SubElement(myinfo, "user_total_watching")
                userwatching.text = str(watchingmanga)
                usercomplete = etree.SubElement(myinfo, "user_total_completed")
                usercomplete.text = str(completemanga)
                useronhold = etree.SubElement(myinfo, "user_total_onhold")
                useronhold.text = str(onholdmanga)
                userdropped = etree.SubElement(myinfo, "user_total_dropped")
                userdropped.text = str(droppedmanga)
                userplantowatch = etree.SubElement(myinfo, "user_total_plantowatch")
                userplantowatch.text = str(plantowatchmanga)
                
                for i in glob.glob("./files/manga/*.txt"):
                    with open(i, "r") as fichier:
                        contenu = fichier.read()
                    infos = contenu.split("\n")
                    
                    manga = etree.SubElement(mal, "manga")
                    mangaid = etree.SubElement(manga, "series_mangadb_id")
                    mangaid.text = infos[0].split(" : ")[1]
                    mangatitle = etree.SubElement(manga, "series_title")
                    mangatitle.text = "<![CDATA["+infos[1].split(" : ")[1]+"]]>"
                    mangatype = etree.SubElement(manga, "series_volumes")
                    mangatype.text = infos[4].split(" : ")[1]
                    mangaep = etree.SubElement(manga, "series_chapters")
                    mangaep.text = infos[6].split(" : ")[1]
                    mangamyid = etree.SubElement(manga, "my_id")
                    mangamyid.text = "0"
                    mangawatchvol = etree.SubElement(manga, "my_read_volumes")
                    mangawatchvol.text = infos[3].split(" : ")[1]
                    mangawatchep = etree.SubElement(manga, "my_read_chapters")
                    mangawatchep.text = infos[5].split(" : ")[1]
                    mangastart = etree.SubElement(manga, "my_start_date")
                    mangastart.text = "0000-00-00"
                    mangaend = etree.SubElement(manga, "my_finish_date")
                    mangaend.text = "0000-00-00"
                    mangarated = etree.SubElement(manga, "my_scanalation_group")
                    mangarated.text = "<![CDATA[]]>"
                    mangascore = etree.SubElement(manga, "my_score")
                    mangascore.text = "0"
                    mangastorage = etree.SubElement(manga, "my_storage")
                    mangastatus = etree.SubElement(manga, "my_status")
                    if infos[2].split(" : ")[1] == "En visionnement":
                        mangastatus.text = "Reading"
                    elif infos[2].split(" : ")[1] == "Fini":
                        mangastatus.text = "Completed"
                    elif infos[2].split(" : ")[1] == "A voir":
                        mangastatus.text = "Plan to Watch"
                    else:
                        mangastatus.text = "Dropped"
                    mangacomments = etree.SubElement(manga, "my_comments")
                    mangacomments.text = "<![CDATA[]]>"
                    mangatimes = etree.SubElement(manga, "my_times_read")
                    mangatimes.text = "0"
                    mangarewatch = etree.SubElement(manga, "my_reread_value")
                    mangatags = etree.SubElement(manga, "my_tags")
                    mangatags.text = "<![CDATA[]]>"
                    mangaupdate = etree.SubElement(manga, "update_on_import")
                    mangaupdate.text = "1"
                    
                self.xmlMAL = asksaveasfilename(defaultextension='.xml', title = "Choisissez votre fichier pour MyAnimeList")
                if self.xmlMAL != "":
                    try:
                        with open(self.xmlMAL, "w") as fichier:
                            fichier.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
                            fichier.write(etree.tostring(mal, pretty_print=True).decode('utf-8'))
                        showinfo("Export réussi", "Tous les mangas ont été exportés")
                    except:
                        showerror("Erreur", "L'écriture du fichier n'a pas pu être faite.")
                else:
                    showerror("Erreur", "Sélectionnez un fichier valide")"""
        


