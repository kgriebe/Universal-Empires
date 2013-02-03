#!/usr/bin/python

import os
import sys
import json
from textwrap import fill
from collections import defaultdict
from bcrypt import hashpw, gensalt
import __builtin__
from time import sleep
from getpass import getpass

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
        self.active_ship_list = {}

def new_player(user, race, password):
    player_info = {}
    ship_list = {}
    x = player()
    x.race = race
    x.name = user
    x.password = password
    x.rank = "1"
    x.credits = "1000"
    x.fuel_rods = "20"
    x.tech = "0"
    # Use this list to set the default ships dependant upon race.
    if race.lower() == "rufs":
        x.ship_list = [1, 26, 51]
        x.active_ship_list = x.ship_list
    elif race.lower() == "amv":
        x.ship_list = [6, 31, 56]
        x.active_ship_list = x.ship_list
    elif race.lower() == "dic":
        x.ship_list = [11, 36, 61]
        x.active_ship_list = x.ship_list
    elif race.lower() == "lbs":
        x.ship_list = [16, 41, 66]
        x.active_ship_list = x.ship_list
    elif race.lower() == "sts":
        x.ship_list = [21, 46, 71]
        x.active_ship_list = x.ship_list
    elif race.lower() == "help":
        help_file = open("./Data/races.help", 'r')
        for line in help_file:
            output = fill(line)
            print output + "\n"
        player_creator(user, password)
    elif race.lower() == "quit":
        sys.exit(0)
    else:
        print "Invalid Race Selection."
        player_creator(user, password)
    
    # Create/Open player file
    player_file = open("./Players/" + x.name + ".data", 'w')
    # Create dictionary of lists we can use to add ships to
    ship_list = defaultdict(list)
    active_ship_list = defaultdict(list)
    # Add default ships to dictionary under ship_list key
    ship_list['ship_list'].append(x.ship_list)
    active_ship_list['active_ship_list'].append(active_ship_list)
    # Create dictionary containing all player attributes
    player_dict = dict([('name', x.name), ('rank', x.rank), ('password', password), ('race', race.lower()), ('credits', x.credits), ('fuel_rods', x.fuel_rods), ('ship_list', x.ship_list), ('active_ship_list', x.active_ship_list)])
    # Insert player_dict into another dictionary with the player's name as the key
    player_info[x.name] = player_dict
    # Convert dictionary to json
    json_string = json.dumps(player_info)
    # Write json to player file
    player_file.write(json_string)


# Get user password, encrypt it, and return.  This is only called when a new player is created.
def password_get():
    password = getpass("Please enter your desired password: ")
    password1 = getpass("Please confirm your password: ")
    if not password == password1:
        print "Your passwords did not match.  Please try again.\n"
        password_get()
    else:
        hashed_password = hashpw(password, gensalt())
    return hashed_password

def player_creator(user, password):
    race = raw_input("Please select your race: RUFS, AMV, DIC, LBS, or STS.  Enter \"Help\" for information on each race, or \"Quit\" to exit.\n")
    new_player(user, race, password)

def login():
# Print the login screen
    login_screen = open('./Data/login_screen.txt')
    os.system('clear')
    for line in login_screen:
        sys.stdout.write(line)
    print "\n"
    user = raw_input("Login: ")
    __builtin__.active_user = user
    if not user:
        print "Invalid Selection.  Please try again."
        sleep(2)
        login()
    file_path = "./Players/" + user + ".data"
    if os.path.exists(file_path):
        password = getpass()
        with open(file_path) as player_file:
    		player_json = json.load(player_file)
    	if hashpw(password, player_json[user]["password"]) == player_json[user]["password"]:
    	    print "Login Successful.\n"
            __builtin__.active_user = user
    	else:
    	    error = "Password does not match.  Please try again.\n"
            sys.stdout.write(error)
            sleep(2)
    	    login()
    else:
        print "Creating new player."
        password = password_get()
        player_creator(user, password)
    return user

