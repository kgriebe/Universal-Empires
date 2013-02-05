#!/usr/bin/python

import os, sys
import json
from Config.vars import end_line, full_line, empty_line, beginning_line
import __builtin__
from sectors import sectors_view
from Controllers.commands import command_process
from Controllers.prompt import prompt
from time import sleep
import selection_screen

def view_generator():
    #Create View File and write opening
    wormholes_view = open('./Data/wormholes_screen.txt', 'w+')
    wormholes_view.write(full_line*3)
    wormholes_view.write(empty_line)
    #Set user file path, load user json, load wormholes json
    user_file_path = "./Players/" + __builtin__.active_user + ".data"
    with open(user_file_path) as player_data:
        player_json_data = json.load(player_data)
    with open("./Data/wormholes.json") as wormholes_data:
        wormholes_json_data = json.load(wormholes_data)
    #create and write wormhole list lines to view file
    for wormhole in player_json_data[__builtin__.active_user]["wormholes"]:
        wormhole_name = wormholes_json_data[str(wormhole)]["name"]
        line = beginning_line + wormhole_name.center(50) + end_line + empty_line
        wormholes_view.write(line)
    #write closing
    wormholes_view.write(full_line*3)

def selection_process(selection):
    wormhole_id = ""
    command_process(selection)
    if selection == "back":
        selection_screen.selection_screen()
    #Set user file path, load user json, load wormholes json
    user_file_path = "./Players/" + __builtin__.active_user + ".data"
    with open(user_file_path) as player_data:
        player_json_data = json.load(player_data)
    with open("./Data/wormholes.json") as wormholes_data:
        wormholes_json_data = json.load(wormholes_data)

    for wormhole in player_json_data[__builtin__.active_user]["wormholes"]:
        if selection == wormholes_json_data[str(wormhole)]["name"].lower():
            wormhole_id = wormhole
    if not wormhole_id:
        print "Invalid Selection.  Please try again."
        sleep(2)
        wormholes_view()
    else:
        sectors_view(wormhole_id)



def wormholes_view():
    os.system('clear')
    view_generator()
    wormholes_view = open('./Data/wormholes_screen.txt', 'r')
    print "\n"
    for line in wormholes_view:
        sys.stdout.write(line)
    print "\n\n"
    selection = raw_input(prompt(__builtin__.active_user))
    selection_process(selection.lower())