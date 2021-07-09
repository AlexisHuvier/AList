from tkinter import ttk, RIGHT, BOTH, StringVar, messagebox, IntVar
import os

from alist.pages.right_page import RightPage


class Parameters(RightPage):
    def __init__(self, main):
        super(Parameters, self).__init__(main)
        title = ttk.Label(self, text="Paramètres", font="-size 22 -weight bold")
        title.pack(pady=15)

        theme_label = ttk.Label(self, text="Thème :", font="-size 14")
        theme_label.pack(pady=(30, 0))

        self.theme = StringVar(self)
        self.theme.set(self.main.config.get("theme", "azure-dark"))
        themes = [self.main.config.get("theme", "azure-dark")]
        themes += [i.split(".")[0] for i in os.listdir("alist/themes") if ".tcl" in i and i.split(".")[0] not in themes]
        theme_choose = ttk.OptionMenu(self, self.theme, *themes)
        theme_choose["width"] = 20
        theme_choose.pack(pady=15)

        self.translation = IntVar(self)
        self.translation.set(1 if self.main.config.get("translation", True) else 0)
        translation_checkbox = ttk.Checkbutton(self, text="Traduction Automatique", variable=self.translation,
                                               onvalue=1, offvalue=0)
        translation_checkbox.pack(pady=(30, 15))

        valid = ttk.Button(self, width=20, text="Valider", command=self.validate)
        valid.pack(pady=30)

        self.pack(side=RIGHT, fill=BOTH)

    def validate(self):
        self.main.config.set("theme", self.theme.get())
        self.main.config.set("translation", True if self.translation.get() == 1 else False)
        self.main.config.save()
        messagebox.showwarning("AList - Paramètres", "Certains paramètres nécessitent de relancer le programme.")
        self.main.show_page("accueil")
