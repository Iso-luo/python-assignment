# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-21 11:53 p.m.
import urllib.parse
import requests
from key import key

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = key.s

while True:
    orig = input("starting location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("url: ", url)
    json_data = requests.get(url).json()
    json_status = json_data['info']['statuscode']
    if json_status == 0:
        print("api status: ", json_status, " = A successful route call.\n")
        print("direction from ", orig, " to ", dest)
        print("trip duration: ", json_data["route"]['formattedTime'])
        print("kilometers: ", str("{:.2f}".format((json_data['route']['distance']) * 1.61)))
        print("fuel used (Ltr): ", str("{:.2f}".format((json_data['route']['fuelUsed']) * 3.78)))
        print("----------------------------------------------")
    elif json_status == 402:
        print("\n*******************************************************")
        print("status code: ", json_status, "; Invalid user inputs for one or both locations.")
        print("*******************************************************\n")
    else:
        print("\n*******************************************************")
        print("status code: ", json_status, ";Refer to: ",
              "https://developer.mapquest.com/documentation/directions=api/status-codes")
        print("*******************************************************\n")