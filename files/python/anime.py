from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import urllib.request
import os
import webbrowser

class Anime(Frame):
    """Page présentant un animé (peut prendre un temps à s'ouvrir)"""
    def __init__(self, main, jikan, malId):
        super(Anime, self).__init__(main, bg="#9f9f9f", relief = GROOVE)
        self.pack_propagate(False)
        self.config(width=800, height=600)
        self.main = main
        self.jikan = jikan
        self.anime = self.jikan.anime(malId)
        
        urllib.request.urlretrieve(self.anime["image_url"], "files/temp.jpg")
        image = Image.open("files/temp.jpg") 
        photo = ImageTk.PhotoImage(image) 
        
        self.lImage = Label(self, image=photo)
        self.lImage.image = photo 
        self.lImage.pack(side = RIGHT, padx = 20)
        
        os.remove("files/temp.jpg")
        
        if len(self.anime["title"]) < 15:
            self.lTitre = Label(self, text = self.anime["title"], font="-size 23 -weight bold")
        elif len(self.anime["title"]) < 25:
            self.lTitre = Label(self, text = self.anime["title"], font="-size 21 -weight bold")
        elif len(self.anime["title"]) < 35:
            self.lTitre = Label(self, text = self.anime["title"], font="-size 19 -weight bold")
        else:
            self.lTitre = Label(self, text = self.anime["title"][:33]+"...", font="-size 19 -weight bold")
        self.lTitre.pack(pady = 30)
        
        self.lType = Label(self, text = "Type : Anime", font="-size 11")
        self.lType.pack(pady = 5)
        if self.anime["title_english"]:
            self.lTitleEN = Label(self, text = "Titre Anglais : "+self.anime["title_english"], font = "-size 11")
        else:
            self.lTitleEN = Label(self, text = "Titre Anglais : Aucun", font = "-size 11")
        self.lTitleEN.pack(pady = 5)
        self.lAuteur = Label(self, text = "Studio principal : "+self.anime["studios"][0]["name"], font = "-size 11")
        self.lAuteur.pack(pady = 5)
        textGenre = "Genres : "
        nb = 5
        for i in self.anime["genres"]:
            if i == self.anime["genres"][0]:
                textGenre += i["name"]
            else:
                if nb == 0:
                    textGenre += ", \n"+i["name"]
                    nb = 5
                else:
                    textGenre += ", "+i["name"]
            nb -= 1
        self.lGenre = Label(self, text = textGenre, font = "-size 11")
        self.lGenre.pack(pady=5)
        if self.anime["status"] == "Finished" or self.anime["status"] == "Finished Airing":
            self.lStatus = Label(self, text = "Status : Fini", font = "-size 11")
            self.lStatus.pack(pady = 5)
        elif self.anime["status"] == "Publishing":
            self.lStatus = Label(self, text = "Status : En cours de publication", font = "-size 11")
            self.lStatus.pack(pady = 5)
        elif self.anime["status"] == "Not yet aired":
            self.lStatus = Label(self, text = "Status : Non débuté", font = "-size 11")
            self.lStatus.pack(pady = 5)
        else:
            self.lStatus = Label(self, text = "Status : Inconnu", font = "-size 11")
            self.lStatus.pack(pady = 5)
        if self.anime["episodes"]:
            self.lVolumesChapitres = Label(self, text = "Episodes : "+str(self.anime["episodes"]), font = "-size 11")
        else:
            self.lVolumesChapitres = Label(self, text = "Episodes : 0", font = "-size 11")
        self.lVolumesChapitres.pack(pady=5)
        
        textR = ""
        if self.anime["rank"]:
            textR += "Top : "+str(self.anime["rank"])
        else:
            textR += "Top : Inconnu"
        if self.anime["score"]:
            textR += "    Score : "+str(self.anime["score"])
        else:
            textR += "    Score : Inconnu"
        if self.anime["popularity"]:
            textR += "    Popularité : "+str(self.anime["popularity"])
        else:
            textR += "    Popularité : Inconnue"
        self.lRank = Label(self, text = textR, font = "-size 11")
        self.lRank.pack(pady=5)
        
        textSynopsis = "Synopsis (en anglais) :\n"
        if self.anime["synopsis"]:
            mots = self.anime["synopsis"].split(" ")
            nb = 50
            lignes = 0
            for i in mots:
                if nb - len(i) <= 0:
                    nb = 50 - len(i)
                    lignes += 1
                    if lignes == 7:
                        textSynopsis += "..."
                        break
                    else:
                        textSynopsis += "\n"+i + " "
                else:
                    textSynopsis += i + " "
                    nb -= len(i)
        else:
            textSynopsis += "Aucun"
        self.lSynopsis = Label(self, text = textSynopsis, font = "-size 11")
        self.lSynopsis.pack(pady=20)
        
        self.bLien = Button(self, command= lambda: self.openWeb(self.anime["url"]), text = "Lien MAL")
        self.bLien.pack(side = RIGHT, padx = 20, pady = 10)
        self.bTrailer = Button(self, command = lambda: self.openWeb(self.anime["trailer_url"]), text = "Trailer")
        self.bTrailer.pack(side = RIGHT, padx = 20, pady = 10)
        self.bAddList = Button(self, text = "Ajouter à ma liste", command = self.addToList)
        self.bAddList.pack(side = RIGHT, padx = 20, pady = 10)
        
        self.pack(side=RIGHT)
    
    def openWeb(self, url):
        """Ouvre une page internet avec comme url <url>"""
        webbrowser.open(url)
    
    def addToList(self):
        """Ajoute l'animé à sa liste d'animé"""
        with open("files/anime/"+str(self.anime["mal_id"])+".txt", "w") as fichier:
            if self.anime["episodes"]:
                fichier.write("ID : "+str(self.anime["mal_id"])+"\nNom : "+self.anime["title"]+"\nStatus : A voir\nEpisodes : 0\nEpisodes Max : "+str(self.anime["episodes"])+"\nType : "+str(self.anime["type"]))
            else:
                fichier.write("ID : "+str(self.anime["mal_id"])+"\nNom : "+self.anime["title"]+"\nStatus : A voir\nEpisodes : 0\nEpisodes Max : 0\nType : "+str(self.anime["type"]))
        showinfo("Anime ajouté", "L'anime a été ajouté à votre liste")
                
