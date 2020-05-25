# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-21 10:00 a.m.

# import xmltodict
#
# with open("xml_example.xml") as f1:
#     xml_example = f1.read()
# print(type(xml_example))
# print(xml_example)
#
# xml_dict = xmltodict.parse(xml_example)

# import yaml
# with open("yaml_example.yaml") as f3:
#     yaml_example = f3.read()
#
# yaml_dict = yaml.full_load(yaml_example)
# print(yaml_dict)

from netmiko import ConnectHandler
import re

device = {"address": "10.1.99.45", "ssh_port": 22, "username": "cisco", "password": "cisco", "device_type": "cisco_ios"}
device = list(device.values())
print(device)
ch = ConnectHandler(ip=device[0],
                    port=device[1],
                    username=device[2],
                    password=device[3],
                    device_type=device[4])
print(ch)
