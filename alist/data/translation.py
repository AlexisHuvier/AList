import threading

from alist.utils import GoogleTranslator, wrap_text

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
            self.label["text"] = wrap_text(self.translator.translate(self.text, lang_src=self.src, lang_tgt=self.dest),
                                           self.length, self.lines)
        else:
            self.label["text"] = wrap_text(self.text, self.length, self.lines)


class TranslationProvider:
    def __init__(self, main):
        self.main = main
        self.translator = GoogleTranslator()

    def translate(self, label, text, length=150, lines=10, src="en", dest="fr"):
        if len(text) >= 4500:
            text = text[:4500]
        label["text"] = wrap_text(text, length, lines)
        thread = Translate(self.main, self.translator, src, dest, text, label, length, lines)
        thread.start()

    def genre_translate(self, genre):
        if genre in GENRE_TRANSLATION.keys():
            return GENRE_TRANSLATION[genre]
        return genre
