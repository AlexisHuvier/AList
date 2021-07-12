from lxml import etree

STATUS_MAL_AL = {
    "Plan to Watch": "A voir",
    "Plan to Read": "A voir",
    "Watching": "En visionnement",
    "Reading": "En visionnement",
    "Completed": "Fini",
    "Dropped": "Abandonné"
}


class MALImporter:
    def __init__(self, main):
        self.main = main

    def import_(self, type_, file):
        tree = etree.parse(file)
        if type_ == "anime":
            for i in tree.xpath("/myanimelist/anime"):
                title = i.find("series_title").text
                id_ = i.find("series_animedb_id").text
                max_ep = i.find("series_episodes").text
                ep = i.find("my_watched_episodes").text
                status = STATUS_MAL_AL[i.find("my_status").text]
                type_ = i.find("series_type").text
                self.main.myanime.add(id_, title, max_ep, type_)
                self.main.myanime.modify(id_, ep=ep, status=status)
        else:
            for i in tree.xpath("/myanimelist/manga"):
                title = i.find("manga_title").text
                id_ = i.find("manga_mangadb_id").text
                max_vol = i.find("manga_volumes").text
                vol = i.find("my_read_volumes").text
                max_chap = i.find("manga_chapters").text
                chap = i.find("my_read_chapters").text
                status = STATUS_MAL_AL[i.find("my_status").text]
                type_ = "Manga"
                self.main.mymanga.add(id_, title, max_vol, max_chap, type_)
                self.main.mymanga.modify(id_, vol=vol, chap=chap, status=status)
