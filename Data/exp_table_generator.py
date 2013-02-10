#!/usr/bin/python

import os, sys
import re
import json


f1_level = 100
f2_level = 200
f3_level = 400
f4_level = 800
f5_level = 1600
f1 = open('exp_table1.json', 'w+')
f2 = open('exp_table2.json', 'w+')
f3 = open('exp_table3.json', 'w+')
f4 = open('exp_table4.json', 'w+')
f5 = open('exp_table5.json', 'w+')
f1_dict = {}
f2_dict = {}
f3_dict = {}
f4_dict = {}
f5_dict = {}




def exp_table_creator(table):
    level = 0
    exp_value = ""
    while level < 100:
        exp_value1 = (f1_level * (level * level)) + (level**3)
        f1_dict[level] = exp_value1
        exp_value2 = (f2_level * (level * level)) + (level**3)
        f2_dict[level] = exp_value2
        exp_value3 = (f3_level * (level * level)) + (level**3)
        f3_dict[level] = exp_value3
        exp_value4 = (f4_level * (level * level)) + (level**3)
        f4_dict[level] = exp_value4
        exp_value5 = (f5_level * (level * level)) + (level**3)
        f5_dict[level] = exp_value5
        level = level + 1
    string1 = json.dumps(f1_dict)
    string2 = json.dumps(f2_dict)
    string3 = json.dumps(f3_dict)
    string4 = json.dumps(f4_dict)
    string5 = json.dumps(f5_dict)

    f1.write(string1)
    f2.write(string2)
    f3.write(string3)
    f4.write(string4)
    f5.write(string5)




def main():
    exp_table_creator("f1")
    exp_table_creator("f2")
    exp_table_creator("f3")
    exp_table_creator("f4")
    exp_table_creator("f5")


if __name__ == "__main__":
    main()
