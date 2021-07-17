from tkinter import ttk, RIGHT, BOTH, LEFT, messagebox
from datetime import datetime

from alist.pages.right_page import RightPage
from alist.utils import ScrollFrame, open_url, StringChooser


class Episodes(RightPage):
    def __init__(self, main, mal_id, title):
        super(Episodes, self).__init__(main)
        self.mal_id = mal_id
        self.current_page = int(title.split("_")[0])
        self.last_page = 0
        self.episodes = None
        self.urls = None

        self.title = "_".join(title.split("_")[1:])

        title = ttk.Label(self, text=self.title, font="-size 22 -weight bold")
        title.pack(pady=15)

        bottom_frame = ttk.Frame(self)

        left_page = ttk.Button(bottom_frame, text="<-", width=20, command=self.previous_page)
        left_page.pack(side=LEFT, padx=20)
        self.num_page = ttk.Label(bottom_frame, text="Page "+str(self.current_page)+"/"+str(self.last_page))
        self.num_page.pack(side=LEFT, padx=20)
        right_page = ttk.Button(bottom_frame, text="->", width=20, command=self.next_page)
        right_page.pack(side=LEFT, padx=20)

        bottom_frame.pack(pady=10)

        self.scroll = ScrollFrame(self, width=1080, height=600)
        self.scroll.pack_propagate(False)

        self.scroll.pack(pady=10)

        self.back = ttk.Button(self, text="Retour", command=lambda: self.main.show_page("anime "+str(mal_id)))
        self.back.pack(pady=10)

        self.pack(side=RIGHT, fill=BOTH)

        self.reload_results()

    def reload_results(self):
        self.episodes = self.main.mal.anime(self.mal_id, "episodes", self.current_page)
        self.last_page = self.episodes["episodes_last_page"]
        self.num_page["text"] = "Page "+str(self.current_page)+"/"+str(self.last_page)

        self.scroll.destroy()
        self.back.destroy()

        self.scroll = ScrollFrame(self, width=1080, height=580)
        self.scroll.pack_propagate(False)

        if self.last_page == 1:
            max_ep = len(self.episodes["episodes"])
        else:
            max_ep = 100 * self.last_page - 1

        for i, episode in enumerate(self.episodes["episodes"]):
            date = datetime.strptime(episode["aired"], "%Y-%m-%dT%H:%M:%S+00:00")

            temp = ttk.Frame(self.scroll.viewport)

            ttitle = ttk.Label(temp, text=str(episode["episode_id"]) + " - " + episode["title"], font="-weight bold")
            ttitle.pack(pady=10)

            infos = ttk.Frame(temp)

            date = ttk.Label(infos, text="Date : "+str(date.day)+"/"+str(date.month)+"/"+str(date.year))
            date.pack(side=LEFT, padx=10)
            filler = ttk.Label(infos, text="Filler : "+("Oui" if episode["filler"] else "Non"))
            filler.pack(side=LEFT, padx=10)
            recap = ttk.Label(infos, text="Recap : "+("Oui" if episode["recap"] else "Non"))
            recap.pack(side=LEFT, padx=10)

            infos.pack(pady=5)

            btn = ttk.Frame(temp)

            vostfr = ttk.Button(btn, text="VOSTFR",
                                command=lambda a=episode: self.open_episode("vostfr", a["episode_id"], max_ep))
            vostfr.pack(side=LEFT, padx=10)

            mal = ttk.Button(btn, text="Lien MAL", command=lambda a=episode: open_url(a["video_url"]))
            mal.pack(side=LEFT, padx=10)

            vf = ttk.Button(btn, text="VF",
                            command=lambda a=episode: self.open_episode("vf", a["episode_id"], max_ep))
            vf.pack(side=LEFT, padx=10)

            btn.pack(pady=5)

            temp.grid(row=i // 2, column=i % 2, pady=10, padx=5)

        for i in range(2):
            self.scroll.viewport.columnconfigure(i, weight=1)

        self.scroll.pack(pady=10)

        self.back = ttk.Button(self, text="Retour",
                               command=lambda: self.main.show_page("anime "+str(self.mal_id)))
        self.back.pack(pady=10)

    def open_episode(self, version, ep_id, max_ep):
        results = {k: v for k, v in self.main.streaming.provide(version, self.title, ep_id, max_ep).items()
                   if v is not None}
        if len(results.keys()) == 0:
            messagebox.showwarning("AList - Episodes", "Aucun lien n'a été trouvé pour cet épisode.")
        else:
            self.urls = results
            StringChooser(self, "AList - Episodes", "Choisissez la source :", self.valid_episode, *results.keys())

    def valid_episode(self, choice):
        open_url(self.urls[choice])

    def next_page(self):
        if self.current_page != self.last_page:
            self.current_page += 1
            self.reload_results()

    def previous_page(self):
        if self.current_page != 1:
            self.current_page -= 1
            self.reload_results()
