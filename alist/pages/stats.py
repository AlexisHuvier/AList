from tkinter import ttk, RIGHT, BOTH

from alist.pages.right_page import RightPage
from alist.utils import pretty_number


class Stats(RightPage):
    def __init__(self, main, mal_id, title):
        super(Stats, self).__init__(main)
        if title.startswith("a_"):
            self.stats = self.main.mal.anime(mal_id, "stats")
            type_ = "anime"
        else:
            self.stats = self.main.mal.manga(mal_id, "stats")
            type_ = "manga"
        title = title[2:]

        title = ttk.Label(self, text=title, font="-size 22 -weight bold")
        title.pack(pady=15)

        listing = ttk.Label(self, text="Nombre de liste ayant l'anime :")
        listing.pack(pady=(15, 5))

        listing_ = ttk.Treeview(self, columns=("Etat", "Nombre",), selectmode="none", height=4)
        listing_.column("#0", width=0, stretch="no")
        listing_.column("Etat", anchor="center")
        listing_.column("Nombre", anchor="center")
        listing_.heading("#0", text="", anchor="center")
        listing_.heading("Etat", text="Etat", anchor="center")
        listing_.heading("Nombre", text="Nombre", anchor="center")

        listing_.insert("", "end", "watching",
                        values=("En visionnement",
                                pretty_number(self.stats["watching" if type_ == "anime" else "reading"]),))
        listing_.insert("", "end", "completed", values=("Complété", pretty_number(self.stats["completed"]),))
        listing_.insert("", "end", "on_hold", values=("En attente", pretty_number(self.stats["on_hold"]),))
        listing_.insert("", "end", "dropped", values=("Abandonné", pretty_number(self.stats["dropped"]),))
        listing_.insert("", "end", "plan_to_watch",
                        values=("A voir",
                                pretty_number(self.stats["plan_to_watch" if type_ == "anime" else "plan_to_read"]),))
        listing_.insert("", "end", "total", values=("Total", pretty_number(self.stats["total"]),))

        listing_.pack(pady=(5, 15))

        score = ttk.Label(self, text="Notes de l'animé :")
        score.pack(pady=(15, 5))

        score_ = ttk.Treeview(self, columns=("Note", "Nombre", "Pourcentage"), selectmode="none", height=8)
        score_.column("#0", width=0, stretch="no")
        score_.column("Note", anchor="center")
        score_.column("Nombre", anchor="center")
        score_.column("Pourcentage", anchor="center")
        score_.heading("#0", text="", anchor="center")
        score_.heading("Note", text="Note", anchor="center")
        score_.heading("Nombre", text="Nombre", anchor="center")
        score_.heading("Pourcentage", text="Pourcentage", anchor="center")

        for i in range(1, 11):
            score_.insert("", "end", str(i), values=(
                str(i), pretty_number(self.stats["scores"][str(i)]["votes"]),
                str(self.stats["scores"][str(i)]["percentage"]) + " %"
            ))

        score_.pack(pady=5)

        moyenne = 0
        total = 0
        for i in range(1, 11):
            moyenne += self.stats["scores"][str(i)]["votes"] * i
            total += self.stats["scores"][str(i)]["votes"]
        moyenne /= total

        stats = "Moyenne : "+str(round(moyenne, 2)) + "/10"
        stats_ = ttk.Label(self, text=stats)
        stats_.pack(pady=(5, 15))

        back = ttk.Button(self, text="Retour", command=lambda: self.main.show_page(type_+" "+str(mal_id)))
        back.pack(pady=15)

        self.pack(side=RIGHT, fill=BOTH)
