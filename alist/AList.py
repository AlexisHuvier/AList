from tkinter import ttk
from tkinter import *

from alist.utils import Config
from alist.pages import *
from alist.data import *

import os


class Main(Tk):
    def __init__(self):
        super(Main, self).__init__()
        os.chdir(os.path.dirname(__file__)+"/..")

        self.mal = MALProvider()
        self.imager = ImageProvider()
        self.translator = TranslationProvider(self)
        self.myanime = MyAnimeListProvider()
        self.mymanga = MyMangaListProvider()
        self.mal_export = MALExporter(self)
        self.mal_import = MALImporter(self)

        self.config = Config()

        self.tk.call('source', 'alist/themes/' + self.config.get("theme", "azure-dark") + '.tcl')
        ttk.Style().theme_use(self.config.get("theme", "azure-dark"))
        
        self.title("AList")
        self.geometry("1280x800")
        self.resizable(width=False, height=False)

        self.menu = Menu(self)

        self.page = Frame(self)
        self.page.pack(side=RIGHT)
        self.current_page = ""

        self.show_page("accueil")

        self.mainloop()

    def show_page(self, page):
        if self.current_page != page:
            self.page.destroy()

            temp = page.split(" ")
            if len(temp) > 1 and temp[1] != "":
                id_ = int(temp[1])
            else:
                id_ = 0
            if len(temp) > 2:
                title = " ".join(temp[2:])
            else:
                title = ""

            pages = {
                "accueil": [Accueil, []],
                "list_anime": [ListAnime, []],
                "list_manga": [ListManga, []],
                "my_anime": [MyAnime, []],
                "my_manga": [MyManga, []],
                "parameters": [Parameters, []],
                "anime ": [Anime, [id_]],
                "manga ": [Manga, [id_]],
                "modifanime ": [ModifAnime, [id_]],
                "modifmanga ": [ModifManga, [id_]],
                "stats ": [Stats, [id_, title]],
                "news ": [News, [id_, title]],
                "images ": [Images, [id_, title]],
                "videos ": [Videos, [id_, title]]
            }
            for k, v in pages.items():
                if page.startswith(k) or (page == "reload" and self.current_page.startswith(k)):
                    self.page = v[0](self, *v[1])
                    break

            if page != "reload":
                self.current_page = page


def launch():
    Main()


if __name__ == "__main__":
    Main()
