#!/usr/bin/python

import os, sys
from Config.vars import empty_line, beginning_line, end_line, full_line
import __builtin__
import json
from Controllers.prompt import prompt
from Data.gamedata import current_agents
from Controllers.commands import command_process
import selection_screen
from time import sleep

def length_finder(id, attribute):
    result = len(str(ship_json[str(id)][attribute]))
    return result

def selector(selection):
    user = __builtin__.active_user
    if selection == "back":
        selection_screen.selection_screen()
    else:
        if selection in current_agents:
            os.system('clear')
            sys.stdout.write(full_line*3)
            sys.stdout.write(empty_line)
            sys.stdout.write(full_line*3)
            sub_selection = raw_input("Back | Help | Exit".center(80) + "\n\n" + prompt(user))
            sub_selection = sub_selection.lower()
            command_process(sub_selection)
            if sub_selection == "help":
              print "Help"
            elif sub_selection == "back":
              print "Back"
            else:
              print "Invalid Selection."
              sleep(2)
              selector(selection)
            
        else:
            print "Invalid Selection."
            sleep(2)
            salvage_missions()




def salvage_missions():
    user = __builtin__.active_user
    with open("./Players/" + user + ".data") as player_data:
        player_json = json.load(player_data)
    os.system('clear')
    sys.stdout.write(full_line*3)
    sys.stdout.write(empty_line)
    sys.stdout.write(beginning_line + "Salvage Missions".center(50) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(beginning_line + " "*5 + "Available Agents:" + " "*28 + end_line)
    sys.stdout.write(empty_line)
    for agent in current_agents:
        sys.stdout.write(beginning_line + " "*5 + agent.upper() + " "*(45 - len(str(agent))) + end_line)
    tech_string = "Available Tech: %s" % player_json[user]["tech"]
    sys.stdout.write(beginning_line + tech_string.center(50) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(full_line*3)
    print "\n\n"
    selection = raw_input("Agent | Back | Exit".center(80) + "\n\n" + prompt(user))
    selection = selection.lower()
    command_process(selection)
    selector(selection)
