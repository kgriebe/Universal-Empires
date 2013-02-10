#!/usr/bin/python

import json
import sys, os
from random import randrange

testfile = open("testing.json", 'w+')



def json_testing():
    with open('ships.json') as ships_json:
        json_data = json.load(ships_json)
    new_dict = dict(json_data.items())

    for id in new_dict:
        rarity = new_dict[str(id)]["rarity"]
        if rarity == 1:
            new_dict[str(id)]["exp_per_level"] = randrange(200, 400)
        elif rarity == 2:
            new_dict[str(id)]["exp_per_level"] = randrange(400, 800)
        elif rarity == 3:
            new_dict[str(id)]["exp_per_level"] = randrange(800, 1600)
        elif rarity == 4:
            new_dict[str(id)]["exp_per_level"] = randrange(1600, 3200)
        elif rarity == 5:
            new_dict[str(id)]["exp_per_level"] = randrange(3200, 6400)
    string = json.dumps(new_dict, indent=4)
    testfile.write(string)
    testfile.close()


def json_confirm():
    with open('testing.json', 'r') as testing_json:
        json_data = json.load(testing_json)
    print json_data






def main():
    json_testing()
    json_confirm()


if __name__ == "__main__":
    main()