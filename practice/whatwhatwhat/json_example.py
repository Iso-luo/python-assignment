# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time: 2020-05-20 9:22 a.m.

import json

print(type(json))
with open('json/json example.json') as f:
    json_example = f.read()

print(type(json_example))  # string
print(json_example)  # 文本

# dumps
# >>> import json
# >>> j_test = {'a':1, 'b':2}
# >>> json.dumps(j_test)
# '{"a": 1, "b": 2}'
# >>> _
# '{"a": 1, "b": 2}'
# >>> type(_)
# <class 'str'>

# loads
# >> > j_str = '{"a": 2, "b": 3}'
# >> > json.loads(j_str)
# {'a': 2, 'b': 3}

# pretty print
new_json = (json)#.....?自己查格式