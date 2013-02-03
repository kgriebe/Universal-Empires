#!/usr/bin/python

import __builtin__
import json
import sys
from Controllers.prompt import prompt

def view_generator(user):
    #Open file
    roster_file = open('./Data/roster.txt', 'w+')

    #Define Variables
    full_line = "************************************************************".center(80) + "\n"
    beginning_line = "          *****"
    end_line = "*****          " + "\n"
    empty_line = beginning_line + " ".center(50) + end_line

    roster_file.write(full_line*3)
    roster_file.write(empty_line)

    # Load up player file
    file_path = "./Players/" + __builtin__.active_user + ".data"
    with open(file_path) as player_data:
        player_json = json.load(player_data)

    # Load ship file
    ship_file_path = "./Data/ships.json"
    with open(ship_file_path) as ship_file_json:
        ship_json = json.load(ship_file_json)

    #For ships in the active ship list, create the view listing those ships.
    for id in player_json[__builtin__.active_user]["ship_list"]:
        #Format the lines
        ship = "[ " + str(id) + " ] " + ship_json[str(id)]["race"] + " " + ship_json[str(id)]["name"]
        line = beginning_line + "     " + ship + " ".ljust(45 - len(ship)) + end_line
        roster_file.write(line)

    #Write the trailing lines
    roster_file.write(empty_line)
    roster_file.write(full_line)
    roster_file.write(full_line)
    roster_file.write(full_line)
    return "Success"

def roster_view(user):
    result = view_generator(user)
    if result:
        roster_view = open('./Data/roster.txt')
    for line in roster_view:
        sys.stdout.write(line)
    print "\n"
    selection = raw_input("Info | Back | Exit".center(80) + "\n\n" + prompt(__builtin__.active_user))