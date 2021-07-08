import json
import os


class Config:
    def __init__(self):
        self.file = os.path.join("alist", "config.json")
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.values = json.load(f)
        else:
            self.values = {
                "theme": "azure-dark"
            }
            self.save()

    def get(self, key, default):
        return self.values.get(key, default)

    def set(self, key, value):
        self.values[key] = value

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.values, f, indent=4)
