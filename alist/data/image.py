from PIL import Image, ImageTk
import urllib.request
import os
import threading


class DownloadImage(threading.Thread):
    def __init__(self, file, url, label):
        super(DownloadImage, self).__init__()
        self.file = file
        self.url = url
        self.label = label

    def run(self):
        urllib.request.urlretrieve(self.url, self.file)
        image = Image.open(self.file)
        thumb = ImageTk.PhotoImage(image)
        self.label.configure(image=thumb)
        self.label.image = thumb


class ImageProvider:
    def __init__(self, cachedir="alist/cache/images"):
        self.cachedir = cachedir
        os.makedirs(self.cachedir, exist_ok=True)
        self.cache = os.listdir(self.cachedir)

    def apply_image_on_label(self, file, url, label):
        if file not in self.cache:
            self.cache.append(file)
            thread = DownloadImage(self.cachedir + "/" + file, url, label)
            thread.start()
        else:
            image = Image.open(self.cachedir + "/" + file)
            thumb = ImageTk.PhotoImage(image)
            label.configure(image=thumb)
            label.image = thumb

    def del_image(self, file):
        if file in self.cache:
            os.remove(self.cachedir + "/" + file)
            self.cache.remove(file)

    def del_cache(self):
        for file in self.cache:
            os.remove(self.cachedir + "/" + file)
        self.cache = []
