# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-21 9:55 p.m.

import urllib.parse
import requests
from key import key
import json

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimore"
key = key.s

url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
print("url: ", url)

json_data = requests.get(url).json()
print(json_data)
# with open("new_json.json", "a") as f:
#     res = f.write(str(json_data))


json_status = json_data['info']['statuscode']
if json_status == 0:
    print("api status: "+ str(json_status)+" = A successful route call. \n")
