import urllib.request

from alist.utils import modif_text


class AListURLOpener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0'


class StreamingProvider:
    def __init__(self):
        self.opener = AListURLOpener()
        self.sources_vf = {
            "voiranime": {
                "title_modifications": {
                    "lower": True,
                    " ": "-",
                    ":": "",
                    ";": "",
                    ".": "",
                    "/": ""
                },
                "url": "http://voiranime.com/anime/{title}-vf/{title}-{full_id_ep}-vf/"
            },
            "gum-gum-streaming": {
                "title_modifications": {
                    "lower": True,
                    " ": "-",
                    ":": "",
                    ";": "",
                    ".": "",
                    "/": ""
                },
                "url": "http://gum-gum-streaming.com/{title}-{id_ep}-vf/"
            }
        }
        self.sources_vostfr = {
            "voiranime": {
                "title_modifications": {
                    "lower": True,
                    " ": "-",
                    ":": "",
                    ";": ""
                },
                "url": "http://voiranime.com/anime/{title}/{title}-{full_id_ep}-vostfr/"
            },
            "gum-gum-streaming": {
                "title_modifications": {
                    "lower": True,
                    " ": "-",
                    ":": "",
                    ";": "",
                    ".": "",
                    "/": ""
                },
                "url": "http://gum-gum-streaming.com/{title}-{id_ep}-vostfr/"
            }
        }

    def provide(self, version, title, id_ep, max_ep):
        if version == "vf":
            sources = self.sources_vf
        else:
            sources = self.sources_vostfr

        id_ep = str(id_ep)
        full_id_ep = "0"*(len(str(max_ep)) - len(id_ep)) + id_ep

        results = {}
        for k, v in sources.items():
            final_title = modif_text(v["title_modifications"], title)
            modif_url = {
                "{title}": final_title,
                "{id_ep}": id_ep,
                "{full_id_ep}": full_id_ep
            }
            final_url = modif_text(modif_url, v["url"])
            u = self.opener.open(final_url)
            if u.url == final_url and u.status == 200:
                results[k] = final_url
            else:
                results[k] = None
        return results

