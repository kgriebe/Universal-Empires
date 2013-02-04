#!/usr/bin/python

import __builtin__
import json
import sys, os
from Controllers.prompt import prompt
from Controllers.commands import command_process
import ship_hanger

with open("./Data/ships.json") as ship_data:
    ship_json = json.load(ship_data)

def selection_process(input):
    # Load up player file
    file_path = "./Players/" + __builtin__.active_user + ".data"
    with open(file_path) as player_data:
        player_json = json.load(player_data)
    player_ship_list = player_json[__builtin__.active_user]["ship_list"]
    if input == "info":
        id = raw_input("\nPlease enter the ID number of the ship:\n")
        if int(id) in player_ship_list:
            os.system('clear')
            print "\n"
            roster_view = open('./Data/roster.txt')
            for line in roster_view:
                sys.stdout.write(line)
            roster_view.close()
            print "\n\n"
            print " " + ship_json[str(id)]["name"] + ":"    
            print "\n"  
            for item, value in ship_json[str(id)].iteritems():
                if item == "name":
                    pass
                else:
                    print " %s: %s" % (str(item).replace('_', ' ').title(), str(value))
            print "\n"
            selection = raw_input("Info | Back | Exit".center(80) + "\n\n" + prompt(__builtin__.active_user))
            if selection.lower() == "back":
                os.system('clear')
                roster_view(__builtin__.active_user)
            else:
                selection_process(selection)
        else:
            if id in ship_json:
                print "You do not command that ship.\n"
                selection_process(input)
            else:
                print "That vessel does not exist.\n"
                selection_process(input)
    elif input == "back":
        ship_hanger.ship_hanger()
    else:
        command_process(input)



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
    selection_process(selection)