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


class TranslationProvider:
    def __init__(self, main):
        self.main = main
        self.translator = GoogleTranslator()

    def translate(self, text, src="en", dest="fr"):
        if self.main.config.get("translation", True):
            return self.translator.translate(text, lang_src=src, lang_tgt=dest)
        else:
            return text

    def manuel_translate(self, text):
        if self.main.config.get("translation", True):
            if text in GENRE_TRANSLATION.keys():
                return GENRE_TRANSLATION[text]
            else:
                return self.translate(text)
        else:
            return text
