from tkinter import ttk
from tkinter import *
from jikanpy import Jikan

from alist.utils import Config


class Main(Tk):
    def __init__(self):
        super(Main, self).__init__()
        self.jikan = Jikan()
        self.config = Config()

        self.tk.call('source', 'alist/themes/' + self.config.get("theme", "azure-dark") + '.tcl')
        ttk.Style().theme_use(self.config.get("theme", "azure-dark"))
        
        self.title("AList")
        self.geometry("1280x900")
        self.resizable(width=False, height=False)

        self.titre = ttk.Label(self, text="AList")
        self.titre.pack()

        self.mainloop()


if __name__ == "__main__":
    Main()
