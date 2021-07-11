from tkinter import ttk
from tkinter import *

from alist.utils import Config
from alist.pages import *
from alist.data import *


class Main(Tk):
    def __init__(self):
        super(Main, self).__init__()
        self.mal = MALProvider()
        self.imager = ImageProvider()
        self.translator = TranslationProvider(self)
        self.myanime = MyAnimeListProvider()
        self.mymanga = MyMangaListProvider()

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
            if page == "accueil" or (page == "reload" and self.current_page == "accueil"):
                self.page = Accueil(self)
            elif page == "list_anime" or (page == "reload" and self.current_page == "list_anime"):
                self.page = ListAnime(self)
            elif page == "list_manga" or (page == "reload" and self.current_page == "list_manga"):
                self.page = ListManga(self)
            elif page == "my_anime" or (page == "reload" and self.current_page == "my_anime"):
                self.page = MyAnime(self)
            elif page == "my_manga" or (page == "reload" and self.current_page == "my_manga"):
                self.page = MyManga(self)
            elif page == "parameters" or (page == "reload" and self.current_page == "parameters"):
                self.page = Parameters(self)
            elif page.startswith("anime ") or (page == "reload" and self.current_page.startswith("anime ")):
                self.page = Anime(self, int(page.split(" ")[1]))
            elif page.startswith("manga ") or (page == "reload" and self.current_page.startswith("manga ")):
                self.page = Manga(self, int(page.split(" ")[1]))
            elif page.startswith("modifanime ") or (page == "reload" and self.current_page.startswith("modifanime ")):
                self.page = ModifAnime(self, int(page.split(" ")[1]))
            elif page.startswith("modifmanga ") or (page == "reload" and self.current_page.startswith("modifmanga ")):
                self.page = ModifManga(self, int(page.split(" ")[1]))
            else:
                print("ERROR : Unknown Page ("+page+")")
            self.current_page = page


if __name__ == "__main__":
    Main()
