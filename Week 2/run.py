#! /usr/bin/env python3

import os
import requests

Path = "/data/feedback/"

key = ["title", "name", "date", "feedback"]

folder = os.listdir(Path)
for i in folder:
    keycount = 0
    fb = {}
    with open(Path + i) as fl:
        for line in fl:
            value = line.strip()
            fb[key[keycount]] = value
            keycount += 1
    print(fb)
    response = requests.post("http://35.232.216.102/feedback/",
    json=fb)
print(response.request.body)
print(response.status_code)