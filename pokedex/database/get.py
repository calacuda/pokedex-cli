# -*- encoding: utf-8 -*-

import os
import urllib.request
import gzip


from .. import resource_path


def download_database():
    target = os.path.join(resource_path, "veekun-pokedex.sqlite")
    url = "http://veekun.com/static/pokedex/downloads/veekun-pokedex.sqlite.gz"
    # print(target)
    if os.path.isfile(target):
        return

    print("Downloading database...")
    request = urllib.request.urlopen(url)
    with open(target, "wb") as output_file:
        output_file.write(gzip.decompress(request.read()))
    print("Done!")
