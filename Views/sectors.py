#!/usr/bin/python

import json
import os, sys
from Config.vars import end_line, full_line, empty_line, beginning_line
from Controllers.prompt import prompt
from Controllers.commands import command_process
from time import sleep
import __builtin__
import levels

with open("./Data/wormholes.json") as wormholes_data:
    wormholes_json_data = json.load(wormholes_data)

def view_creator(wormhole):
    # Create file for view and write opening
    sub_view = open("./Data/sectors.txt", 'w+')
    sub_view.write("\n" + full_line*3 + empty_line)
    if wormholes_json_data[str(wormhole)]["is_wormhole"]:
        for item in wormholes_json_data[str(wormhole)]["sectors"]:
            sector = wormholes_json_data[str(item)]["name"]
            line = beginning_line + sector.center(50) + end_line + empty_line
            sub_view.write(line)
    else:
        print "This wormhole has no sectors."
    sub_view.write(empty_line + full_line*3 + "\n")

def selection_process(selection, wormhole):
    command_process(selection)
    sector_id = ""
    for item in wormholes_json_data[str(wormhole)]["sectors"]:
        if selection == wormholes_json_data[str(item)]["name"].lower():
            sector_id = item
    if not sector_id:
        print "Invalid Selection.  Please try again."
        sleep(2)
        sectors_view(wormhole)
    else:
        levels.levels_view(sector_id, wormhole)


def sectors_view(wormhole):
    view_creator(wormhole)
    os.system('clear')
    sub_view = open("./Data/sectors.txt", 'r')
    for line in sub_view:
        sys.stdout.write(line)
    selection = raw_input("Please select a level:".center(80) + "\n\n" + "Level | Back | Exit".center(80) + "\n\n" + prompt(__builtin__.active_user))
    selection = selection.lower()
    selection_process(selection, wormhole)