# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-23 6:57 p.m.

import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload = {}
headers = {
  'Cookie': '__cfduid=dbad986aefd25403041526e8335a9648c1590255719; v=2'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
