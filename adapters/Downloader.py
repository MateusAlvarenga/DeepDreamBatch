from urllib import request


class Downloader:
    def __init__(self):
        pass

    def download(self, origin, destination, name):
        f = open(destination + name, "a")
        f.close()
        request.urlretrieve(origin, destination + name)
