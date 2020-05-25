# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-11 1:15 a.m.

data2 = {
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            }
        }
    }
}

for level1_keys, level1_vals in data2:
    for i in level1_keys:
        print(i)
        print(level1_keys[i])