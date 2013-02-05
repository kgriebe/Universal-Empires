#!/bin/python

import sys
import os
import json
from textwrap import fill
from collections import defaultdict
import __builtin__

class player():
    def __init__(self):
        self.name = ""
        self.password = ""
        self.race = ""
        self.ship_list = {}
        self.rank = ""
        self.credits = ""
        self.fuel_rods = ""
        self.max_fuel_rods = ""
        self.tech = ""
        self.active_ship_list = {}
    
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
    x.max_fuel_rods = "20"
    x.tech = "0"
    # Use this list to set the default ships dependant upon race.
    if race.lower() == "rufs":
        x.ship_list = [1, 26, 51]
        x.active_ship_list = [1, 26, 51]
    elif race.lower() == "amv":
        x.ship_list = [6, 31, 56]
        x.active_ship_list = [6, 31, 56]
    elif race.lower() == "dic":
        x.ship_list = [11, 36, 61]
        x.active_ship_list = [11, 36, 61]
    elif race.lower() == "lbs":
        x.ship_list = [16, 41, 66]
        x.active_ship_list = [16, 41, 66]
    elif race.lower() == "sts":
        x.ship_list = [21, 46, 71]
        x.active_ship_list = [21, 46, 71]
    elif race.lower() == "help":
        help_file = open("./Data/races.help", 'r')
        for line in help_file:
            output = fill(line)
            print output + "\n"
    elif race.lower() == "quit":
        sys.exit(0)
    else:
        print "Invalid Race Selection."
    
    # Create/Open player file
    player_file = open("./Players/" + x.name, 'w')
    # Create dictionary of lists we can use to add ships to
    ship_list = defaultdict(list)
    # Add default ships to dictionary under ship_list key
    ship_list['ship_list'].append(x.ship_list)
    # Create dictionary containing all player attributes
    player_dict = dict([('name', x.name), ('rank', x.rank), ('password', password), ('race', race.lower()), ('credits', x.credits), ('fuel_rods', x.fuel_rods), ('ship_list', x.ship_list), ('active_ship_list', x.active_ship_list)])
    # Insert player_dict into another dictionary with the player's name as the key
    player_info[x.name] = player_dict
    # Convert dictionary to json
    json_string = json.dumps(player_info)
    # Write json to player file
    player_file.write(json_string)
    # Set player as active user
    __builtin__.active_user = x.name