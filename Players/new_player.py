#!/bin/python

import sys
import os
import json
from textwrap import fill
from collections import defaultdict

class player():
    def __init__(self):
        self.name = ""
        self.password = ""
        self.race = ""
        self.ship_list = {}
        self.rank = ""
        self.credits = ""
        self.fuel_rods = ""
        self.tech = ""
    
def new_player(name, race, password):
    player_info = {}
    ship_list = {}
    x = player()
    x.race = race
    x.name = name
    x.password = password
    x.rank = "1"
    x.credits = "1000"
    x.fuel_rods = "0"
    x.tech = "0"
    # Use this list to set the default ships dependant upon race.
    if race.lower() == "rufs":
        x.ship_list = [1, 26, 51]
    elif race.lower() == "amv":
        x.ship_list = [6, 31, 56]
    elif race.lower() == "dic":
        x.ship_list = [11, 36, 61]
    elif race.lower() == "lbs":
        x.ship_list = [16, 41, 66]
    elif race.lower() == "sts":
        x.ship_list = [21, 46, 71]
    elif race.lower() == "help":
        f = open("./Data/races.help", 'r')
        for line in f:
            output = fill(line)
            print output + "\n"
    else:
        print "Invalid Race Selection."
        sys.exit(1)
    
    # Check to make sure player doesn't already exist.
    if os.path.exists("./Players/" + x.name):
        print "Player already exists!"
        sys.exit(1)
    else:
        # Create/Open player file
        f = open("./Players/" + x.name, 'w')
        # Create dictionary of lists we can use to add ships to
        ship_list = defaultdict(list)
        # Add default ships to dictionary under ship_list key
        ship_list['ship_list'].append(x.ship_list)
        # Create dictionary containing all player attributes
        player_dict = dict([('name', x.name), ('rank', x.rank), ('password', password), ('race', race.lower()), ('credits', x.credits), ('fuel_rods', x.fuel_rods), ('ship_list', x.ship_list)])
        # Insert player_dict into another dictionary with the player's name as the key
        player_info[x.name] = player_dict
        # Convert dictionary to json
        json_string = json.dumps(player_info)
        # Write json to player file
        f.write(json_string)