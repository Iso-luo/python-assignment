# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-21 10:13 p.m.

import urllib.parse
import requests
from key import key

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = key.s

while True:
    orig = input("starting location: ")
    dest = input("destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: ", url)
    json_data = requests.get(url).json()
    json_status = json_data['info']["statuscode"]
    if json_status == 0:
        print("api status: ", json_status, " = A successful route call")


