import os

from config import BASEPATH

class Checker:

    def run(self):
        albums = []
        for root, dirs, files in os.walk(BASEPATH):
            if len(dirs) == 0:
                append = True
                for f in files:
                    if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png") or f.endswith(".gif") or f.endswith(".JPG"):
                        append = False
                if append:
                    albums.append(root)
        
        print("Missing artwork:" + str(len(albums)))

        albums.sort()
        with open(BASEPATH + '/missing_art.txt', 'w') as f:
            for line in albums:
                f.write(f"{line}\n")
