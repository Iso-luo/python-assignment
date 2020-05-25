# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-21 9:49 p.m.

import urllib.parse
import requests
from key import key
import json

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = key.s

url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})

json_data = requests.get(url).json()  # 返回一个 dict{}
print(type(json_data), json_data)
str_data = json.dumps(json_data)  # 得到json格式字符串，Code Beautify->Json viewer->Tree Viewer
print(str_data)

for i in json_data['route']['legs'][0]['maneuvers']:
    print("Distance: ",i['distance'])
