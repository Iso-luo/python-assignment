# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-15 9:46 a.m.


from key import key
import urllib.parse
import requests

key = key
# step5 Create variables for API request

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = 'Washington'
dest = 'Baltimaore'
key = key
# urlencode 方法，正确地格式化地址
url = main_api + urllib.parse.urlencode(
    {"key": key, "from": orig, "to": dest})  # 这个就是平常看到的网址里面的 name='aa',b = b...其实就是字典

json_data = requests.get(url).json()
print(json_data)

