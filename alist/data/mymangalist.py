import json
import os


class MyMangaListProvider:
    def __init__(self):
        self.file = os.path.dirname(__file__)+"/../manga.json"
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.values = json.load(f)
        else:
            self.values = {}
            self.save()

    def is_in(self, mal_id):
        return str(mal_id) in self.values.keys()

    def add(self, mal_id, name, nb_vol, nb_chap, type_):
        self.values[str(mal_id)] = {
            "id": mal_id,
            "name": name,
            "vol": 0,
            "max_vol": nb_vol,
            "chap": 0,
            "max_chap": nb_chap,
            "type": type_,
            "status": "A voir"
        }
        self.save()

    def modify(self, mal_id, **kwargs):
        for k, v in kwargs.items():
            self.values[str(mal_id)][k] = v
        self.save()

    def delete(self, mal_id):
        del self.values[str(mal_id)]
        self.save()

    def get(self, mal_id):
        return self.values.get(str(mal_id), None)

    def get_all(self):
        return self.values.values()

    def search(self, name):
        return (v for v in self.values.values() if name.lower() in v["name"].lower())

    def get_all_state(self, state):
        return (v for v in self.values.values() if v["status"] == state)

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.values, f, indent=4)
