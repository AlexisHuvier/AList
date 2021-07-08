from tkinter import ttk
from tkinter import *
from jikanpy import Jikan

from alist.utils import Config
from alist.pages import Menu, Accueil


class Main(Tk):
    def __init__(self):
        super(Main, self).__init__()
        self.jikan = Jikan()
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
            else:
                print("ERROR : Unknown Page ("+page+")")
            self.current_page = page


if __name__ == "__main__":
    Main()
