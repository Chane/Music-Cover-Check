import logging
import sys
import argparse
import os

from config import BASEPATH

class Checker:
    def __init__(self):
        parser = argparse.ArgumentParser();
        parser.add_argument(
            '-d', '--debug',
            help = "Log debug information",
            action = "store_const", dest = "loglevel", const = logging.DEBUG,
            default = logging.WARNING
        )

        parser.add_argument(
            '-v', '--verbose',
            help = "Log verbose information",
            action = "store_const", dest = "loglevel", const = logging.INFO
        )

        args = parser.parse_args();

        logging.basicConfig(stream = sys.stdout, level = args.loglevel)
        self.logger = logging.getLogger(__name__)

    def writeMessage(self, message):
        self.logger.log(logging.INFO, message)

    def writeDebug(self, message):
        self.logger.log(logging.DEBUG, message)


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
        
        self.writeMessage("Missing artwork:" + str(len(albums)))

        albums.sort()
        with open(BASEPATH + '/missing_art.txt', 'w') as f:
            for line in albums:
                f.write(f"{line}\n")
