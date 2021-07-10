from PIL import Image, ImageTk
import urllib.request
import os


class ImageProvider:
    def __init__(self, cachedir="alist/cache/images"):
        self.cachedir = cachedir
        os.makedirs(self.cachedir, exist_ok=True)
        self.cache = os.listdir(self.cachedir)

    def get_tkinter_image(self, file, url):
        if file not in self.cache:
            urllib.request.urlretrieve(url, self.cachedir + "/" + file)
            self.cache.append(file)
        image = Image.open(self.cachedir + "/" + file)
        return ImageTk.PhotoImage(image)

    def del_image(self, file):
        if file in self.cache:
            os.remove(self.cachedir + "/" + file)
            self.cache.remove(file)

    def del_cache(self):
        for file in self.cache:
            os.remove(self.cachedir + "/" + file)
        self.cache = []
