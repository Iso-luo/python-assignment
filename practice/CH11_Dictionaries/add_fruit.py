# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-09 4:48 p.m.


def add_fruit(inventory, fruit, quantity):
    if fruit in inventory:
        inventory[fruit] = inventory.get(fruit) + quantity
    else:
        inventory[fruit] = quantity
    return inventory


new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
print("strawberries" in new_inventory)
print(new_inventory["strawberries"])
print(new_inventory)
print(add_fruit(new_inventory, 'strawberries', 25))
print(new_inventory["strawberries"])
