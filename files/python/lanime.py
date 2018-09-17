from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from lxml import etree
import glob

class lAnime(Frame):
    """Page qui liste ses animés"""
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
        """Ouvre une page présentant l'anime dont l'id MAL est <malId>"""
        self.main.showPage("anime|"+str(malId))
    
    def modifyAnime(self, malId):
        """Ouvre une page pour modifier les infos enregistrés pour l'anime ayant comme id MAL <malId>"""
        self.main.showPage("animeM|"+str(malId))
    
    def importMAL(self):
        """Import un .xml exporté de MyAnimeList"""
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
            try:
                pseudo = self.e1.get()
                idMAL = int(self.e2.get())
            except:
                showerror("Erreur", "Votre id n'est pas un nombre")
            else:
                self.fen.destroy()
                
                totalanime = 0
                watchinganime = 0
                completeanime = 0
                onholdanime = 0
                droppedanime = 0
                plantowatchanime = 0
                for i in glob.glob("./files/anime/*.txt"):
                    totalanime += 1
                    with open(i, "r") as fichier:
                        contenu = fichier.read()
                        if contenu.split("\n")[2].split(" : ")[1] == "En visionnement":
                            watchinganime += 1
                        elif contenu.split("\n")[2].split(" : ")[1] == "Fini":
                            completeanime += 1
                        elif contenu.split("\n")[2].split(" : ")[1] == "A voir":
                            plantowatchanime += 1
                        else:
                            droppedanime += 1
                            
                mal = etree.Element("myanimelist")
                    
                myinfo = etree.SubElement(mal, "myinfo")
                userid = etree.SubElement(myinfo, "user_id")
                userid.text = str(idMAL)
                username = etree.SubElement(myinfo, "user_name")
                username.text = pseudo
                userexport = etree.SubElement(myinfo, "user_export_type")
                userexport.text = "1"
                usertotal = etree.SubElement(myinfo, "user_total_anime")
                usertotal.text = str(totalanime)
                userwatching = etree.SubElement(myinfo, "user_total_watching")
                userwatching.text = str(watchinganime)
                usercomplete = etree.SubElement(myinfo, "user_total_completed")
                usercomplete.text = str(completeanime)
                useronhold = etree.SubElement(myinfo, "user_total_onhold")
                useronhold.text = str(onholdanime)
                userdropped = etree.SubElement(myinfo, "user_total_dropped")
                userdropped.text = str(droppedanime)
                userplantowatch = etree.SubElement(myinfo, "user_total_plantowatch")
                userplantowatch.text = str(plantowatchanime)
                
                for i in glob.glob("./files/anime/*.txt"):
                    with open(i, "r") as fichier:
                        contenu = fichier.read()
                    infos = contenu.split("\n")
                    
                    anime = etree.SubElement(mal, "anime")
                    animeid = etree.SubElement(anime, "series_animedb_id")
                    animeid.text = infos[0].split(" : ")[1]
                    animetitle = etree.SubElement(anime, "series_title")
                    animetitle.text = "<![CDATA["+infos[1].split(" : ")[1]+"]]>"
                    animetype = etree.SubElement(anime, "series_type")
                    animetype.text = infos[5].split(" : ")[1]
                    animeep = etree.SubElement(anime, "series_episodes")
                    animeep.text = infos[4].split(" : ")[1]
                    animemyid = etree.SubElement(anime, "my_id")
                    animemyid.text = "0"
                    animewatchep = etree.SubElement(anime, "my_watched_episodes")
                    animewatchep.text = infos[3].split(" : ")[1]
                    animestart = etree.SubElement(anime, "my_start_date")
                    animestart.text = "0000-00-00"
                    animeend = etree.SubElement(anime, "my_finish_date")
                    animeend.text = "0000-00-00"
                    animerated = etree.SubElement(anime, "my_rated")
                    animescore = etree.SubElement(anime, "my_score")
                    animescore.text = "0"
                    animedvd = etree.SubElement(anime, "my_dvd")
                    animestorage = etree.SubElement(anime, "my_storage")
                    animestatus = etree.SubElement(anime, "my_status")
                    if infos[2].split(" : ")[1] == "En visionnement":
                        animestatus.text = "Watching"
                    elif infos[2].split(" : ")[1] == "Fini":
                        animestatus.text = "Completed"
                    elif infos[2].split(" : ")[1] == "A voir":
                        animestatus.text = "Plan to Watch"
                    else:
                        animestatus.text = "Dropped"
                    animecomments = etree.SubElement(anime, "my_comments")
                    animecomments.text = "<![CDATA[]]>"
                    animetimes = etree.SubElement(anime, "my_times_watched")
                    animetimes.text = "0"
                    animerewatch = etree.SubElement(anime, "my_rewatch_value")
                    animetags = etree.SubElement(anime, "my_tags")
                    animetags.text = "<![CDATA[]]>"
                    animerewatching = etree.SubElement(anime, "my_rewatching")
                    animerewatching.text = "0"
                    animerewatchingep = etree.SubElement(anime, "my_rewatching_ep")
                    animerewatchingep.text = "0"
                    animeupdate = etree.SubElement(anime, "update_on_import")
                    animeupdate.text = "1"
                    
                self.xmlMAL = asksaveasfilename(defaultextension='.xml', title = "Choisissez votre fichier pour MyAnimeList")
                if self.xmlMAL != "":
                    try:
                        with open(self.xmlMAL, "w") as fichier:
                            fichier.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
                            fichier.write(etree.tostring(mal, pretty_print=True).decode('utf-8'))
                        showinfo("Export réussi", "Tous les animes ont été exportés")
                    except:
                        showerror("Erreur", "L'écriture du fichier n'a pas pu être faite.")
                else:
                    showerror("Erreur", "Sélectionnez un fichier valide")
        

