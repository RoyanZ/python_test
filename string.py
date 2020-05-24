# -*- coding:utf-8 -*-
import json

json_str = '{"name":"zhou", "age":18}'
json_str_1 = '{"name":"lu", "age":19}'

def translate(json_str):
    data = json.loads(json_str)
    print("user {name}'s age is {age}".format(name=data["name"], age=data["age"]))

if __name__ == "__main__":
    translate(json_str)
    translate(json_str_1)
