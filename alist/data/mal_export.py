from lxml import etree

from tkinter import simpledialog

STATUS_AL_MAL = {
    "A voir": "Plan to Watch",
    "MA voir": "Plan to Read",
    "En visionnement": "Watching",
    "MEn visionnement": "Reading",
    "Fini": "Completed",
    "Abandonné": "Dropped"
}


class MALExporter:
    def __init__(self, main):
        self.main = main

    def export(self, type_, file):
        if type_ == "anime":
            mal = etree.Element("myanimelist")

            myinfo = etree.SubElement(mal, "myinfo")
            username = etree.SubElement(myinfo, "user_name")
            username.text = simpledialog.askstring("AList - Export MAL", "Pseudo MyAnimeList :")
            export_type = etree.SubElement(myinfo, "user_export_type")
            export_type.text = "1"

            for i in self.main.myanime.get_all():
                anime = etree.SubElement(mal, "anime")

                infos = {
                    "series_animedb_id": str(i["id"]),
                    "series_title": str(i["name"]),
                    "series_episodes": str(i["max_ep"]),
                    "series_type": str(i["type"]),
                    "my_watched_episodes": str(i["ep"]),
                    "my_status": STATUS_AL_MAL[i["status"]],
                    "update_on_import": str(1)
                }

                for k, v in infos.items():
                    temp = etree.SubElement(anime, k)
                    temp.text = v

            with open(file, "w") as f:
                f.write(etree.tostring(mal, pretty_print=True).decode("utf-8"))

        else:
            mal = etree.Element("myanimelist")

            myinfo = etree.SubElement(mal, "myinfo")
            username = etree.SubElement(myinfo, "user_name")
            username.text = simpledialog.askstring("AList - Export MAL", "Pseudo MyAnimeList :")
            export_type = etree.SubElement(myinfo, "user_export_type")
            export_type.text = "2"

            for i in self.main.mymanga.get_all():
                manga = etree.SubElement(mal, "manga")

                if i["status"] == "En visionnement":
                    status = "MEn visionnement"
                elif i["status"] == "A voir":
                    status = "MA voir"
                else:
                    status = i["status"]

                infos = {
                    "manga_mangadb_id": str(i["id"]),
                    "manga_title": str(i["name"]),
                    "manga_volumes": str(i["max_vol"]),
                    "manga_chaptes": str(i["max_chap"]),
                    "my_read_volumes": str(i["vol"]),
                    "my_read_chapters": str(i["chap"]),
                    "my_status": STATUS_AL_MAL[status],
                    "update_on_import": str(1)
                }

                for k, v in infos.items():
                    temp = etree.SubElement(manga, k)
                    temp.text = v

            with open(file, "w") as f:
                f.write(etree.tostring(mal, pretty_print=True).decode("utf-8"))
