#!/usr/bin/python

import os, sys
import __builtin__
import json
from Config.vars import end_line, full_line, empty_line, beginning_line
from Controllers.prompt import prompt
from Controllers.commands import command_process
import sectors

with open('./Data/wormholes.json') as wormholes_json:
    wormholes_json_data = json.load(wormholes_json)

def view_creator(sector_id):
    # Create file for view and write opening
    sector_view = open("./Data/levels_view.txt", 'w+')
    sector_view.write("\n" + full_line*3 + empty_line)

    for item in wormholes_json_data[str(sector_id)]["levels"]:
        level = wormholes_json_data[str(item)]["name"]
        line = beginning_line + level.center(50) + end_line + empty_line
        sector_view.write(line)

    sector_view.write(full_line*3 + "\n")

def selection_process(selection, wormhole):
    if selection == "back":
        sectors.sectors_view(wormhole)
    else:
        # Here is where we will put level select and switch to loading combat modules.

def levels_view(sector_id, wormhole):
    view_creator(sector_id)
    sector_view_file = open('./Data/levels_view.txt', 'r')
    for line in sector_view_file:
        sys.stdout.write(line)
    selection = raw_input("Level | Back | Exit".center(80) + "\n\n" + prompt(__builtin__.active_user))
    command_process(selection)
    selection_process(selection, wormhole)