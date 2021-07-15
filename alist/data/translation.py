import threading

from alist.utils import GoogleTranslator

GENRE_TRANSLATION = {
    "Action": "Action",
    "Adventure": "Aventure",
    "Cars": "Voiture",
    "Comedy": "Comédie",
    "Dementia": "Intrigue Complexe",
    "Demons": "Démons",
    "Drama": "Drame",
    "Ecchi": "Ecchi",
    "Fantasy": "Fantaisie",
    "Game": "Jeu",
    "Harem": "Harem",
    "Hentai": "Hentai",
    "Historical": "Histoire",
    "Horror": "Horreur",
    "Josei": "Josei",
    "Kids": "Enfants",
    "Magic": "Magie",
    "Martial Arts": "Arts Martiaux",
    "Mecha": "Mecha",
    "Military": "Militaire",
    "Music": "Musique",
    "Mystery": "Mystère",
    "Parody": "Parodie",
    "Police": "Police",
    "Psychological": "Psychologie",
    "Romance": "Romance",
    "Samurai": "Samurai",
    "School": "Ecole",
    "Sci-Fi": "Sci-Fi",
    "Seinen": "Seinen",
    "Shoujo": "Shoujo",
    "Shoujo Ai": "Shoujo Ai",
    "Shounen": "Shounen",
    "Shounen Ai": "Shounen",
    "Slice of Life": "Train de Vie",
    "Space": "Espace",
    "Sports": "Sport",
    "Super Power": "Super Pouvoir",
    "Supernatural": "Surnaturel",
    "Thriller": "Polar",
    "Vampire": "Vampire",
    "Yaoi": "Yaoi",
    "Yuri": "Yuri"
}


class Translate(threading.Thread):
    def __init__(self, main, translator, src, dest, text, label, length, lines):
        super(Translate, self).__init__()
        self.main = main
        self.translator = translator
        self.src = src
        self.dest = dest
        self.text = text
        self.label = label
        self.length = length
        self.lines = lines

    def run(self):
        if self.main.config.get("translation", True):
            liste = []
            mots =  self.translator.translate(self.text, lang_src=self.src, lang_tgt=self.dest).split(" ")
            nb = self.length
            lignes = 0
            for i in mots:
                if nb - len(i) <= 0:
                    nb = self.length - len(i)
                    lignes += 1
                    if lignes == self.lines:
                        liste.append("...")
                        break
                    else:
                        liste.extend(("\n", i, " "))
                else:
                    liste.extend((i, " "))
                    nb -= len(i)
            self.label["text"] = "".join(liste)
        else:
            self.label["text"] = self.text


class TranslationProvider:
    def __init__(self, main):
        self.main = main
        self.translator = GoogleTranslator()

    def translate(self, label, text, length=150, lines=10, src="en", dest="fr"):
        label["text"] = text
        thread = Translate(self.main, self.translator, src, dest, text, label, length, lines)
        thread.start()

    def genre_translate(self, genre):
        if genre in GENRE_TRANSLATION.keys():
            return GENRE_TRANSLATION[genre]
        return genre
