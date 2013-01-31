#!/bin/python

import sys
import os
import json
from collections import defaultdict

class player():
    def __init__(self):
        self.name = ""
        self.ship_list = {}
        self.rank = ""
        self.credits = ""
        self.fuel_rods = ""
        self.tech = ""
    
def new_player(name):
    player_info = {}
    ship_list = {}
    x = player()
    x.name = name
    x.rank = "1"
    x.credits = "1000"
    x.fuel_rods = "0"
    x.tech = "0"
    # Use this list to set the default ships dependant upon race.
    x.ship_list = [9, 57]
    
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
        player_dict = dict([('name', x.name), ('rank', x.rank), ('credits', x.credits), ('fuel_rods', x.fuel_rods), ('ship_list', x.ship_list)])
        # Insert player_dict into another dictionary with the player's name as the key
        player_info[x.name] = player_dict
        # Convert dictionary to json
        json_string = json.dumps(player_info)
        # Write json to player file
        f.write(json_string)