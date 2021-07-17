import urllib.request
import json
import os

from alist.utils import modif_text


class AListURLOpener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0'


class StreamingProvider:
    def __init__(self):
        self.opener = AListURLOpener()
        with open(os.path.dirname(__file__)+"/../sources.json") as f:
            values = json.load(f)
        self.title_modifications = values["title_modifications"]
        self.sources_vf = values["vf"]
        self.sources_vostfr = values["vostfr"]

    def provide(self, version, title, id_ep, max_ep):
        if version == "vf":
            sources = self.sources_vf
        else:
            sources = self.sources_vostfr

        id_ep = str(id_ep)
        full_id_ep = "0"*(len(str(max_ep)) - len(id_ep)) + id_ep

        results = {}
        for k, v in sources.items():
            final_title = modif_text(self.title_modifications, title)
            modif_url = {
                "{title}": final_title,
                "{id_ep}": id_ep,
                "{full_id_ep}": full_id_ep
            }
            final_url = modif_text(modif_url, v)
            u = self.opener.open(final_url)
            if u.url == final_url and u.status == 200:
                results[k] = final_url
            else:
                results[k] = None
        return results

