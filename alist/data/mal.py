from jikanpy import jikan, exceptions


class MALProvider:
    def __init__(self):
        self.jikan = jikan.Jikan()

    def search(self, type_="anime", name=None, page=None):
        if page is None:
            page = 1
        finalpage = (page - 1) // 5 + 1
        range_ = (page - 1) % 5
        try:
            return self.jikan.search(type_, name, finalpage)["results"][range_*10:range_*10+10]
        except (exceptions.APIException, exceptions.JikanException, exceptions.DeprecatedEndpoint):
            return []

    def anime(self, id_=0):
        try:
            return self.jikan.anime(id_)
        except (exceptions.APIException, exceptions.JikanException, exceptions.DeprecatedEndpoint):
            return None

    def anime_stats(self, id_=0):
        try:
            return self.jikan.anime(id_, "stats")
        except (exceptions.APIException, exceptions.JikanException, exceptions.DeprecatedEndpoint):
            return None

    def manga(self, id_=0, extension=None):
        try:
            return self.jikan.manga(id_, extension)
        except (exceptions.APIException, exceptions.JikanException, exceptions.DeprecatedEndpoint):
            return None

    def season(self, year=2021, season="winter"):
        try:
            return self.jikan.season(year, season)
        except (exceptions.APIException, exceptions.JikanException, exceptions.DeprecatedEndpoint):
            return []

    def character(self, id_=0, extension=None):
        try:
            return self.jikan.character(id_, extension)
        except (exceptions.APIException, exceptions.JikanException, exceptions.DeprecatedEndpoint):
            return None

    def top(self, type_="anime", page=None, subtype=None):
        if page is None:
            page = 1
        finalpage = (page - 1) // 5 + 1
        range_ = (page - 1) % 5
        try:
            return self.jikan.top(type_, finalpage, subtype)["top"][range_*10:range_*10+10]
        except (exceptions.APIException, exceptions.JikanException, exceptions.DeprecatedEndpoint):
            return []
