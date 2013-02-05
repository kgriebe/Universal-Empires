#!/usr/bin/python

import os
import sys
import __builtin__
import json
from Controllers.commands import command_process
import selection_screen
from Controllers.prompt import prompt
from roster import roster_view
from science import science_view

def view_generator():
	#Open file
	hanger_file = open('./Data/ship_hanger.txt', 'w+')

	#Define Variables
	full_line = "************************************************************".center(80) + "\n"
	beginning_line = "          *****"
	end_line = "*****          " + "\n"
	empty_line = beginning_line + " ".center(50) + end_line

	#Write the lines of stars
	hanger_file.write(full_line)
	hanger_file.write(full_line)
	hanger_file.write(full_line)
	hanger_file.write(empty_line)

	#Set announcement line and write to file
	announcement = "Your Active Fleet Is:"
	announcement_line = beginning_line + announcement.center(50) + end_line
	hanger_file.write(announcement_line)
	hanger_file.write(empty_line)

	#Print player ship list with names
	file_path = "./Players/" + __builtin__.active_user + ".data"
	with open(file_path) as player_data:
		player_json = json.load(player_data)

	ship_file_path = "./Data/ships.json"
#	ship_file_path = "./Data/" + player_json[__builtin__.active_user]["race"].upper() + "_ships.json"
	
	#Import ship.json
	with open(ship_file_path) as ship_file_json:
		ship_json = json.load(ship_file_json)
	#For ships in the active ship list, create the view listing those ships.
	for id in player_json[__builtin__.active_user]["active_ship_list"]:
		#Format the lines
		ship = "[ " + str(id) + " ] " + ship_json[str(id)]["race"] + " " + ship_json[str(id)]["name"]
		line = beginning_line + "     " + ship + " ".ljust(45 - len(ship)) + end_line
		hanger_file.write(line)
	#Write the trailing lines
	hanger_file.write(empty_line)
	hanger_file.write(full_line)
	hanger_file.write(full_line)
	hanger_file.write(full_line)
	return "Success"

#Prints the keys:values under each ship id
def ship_info(id):
	file_path = "./Data/ships.json"
	with open(file_path) as ship_data:
		ship_json = json.load(ship_data)
	print ship_json[id]

def get_selection():
    user = __builtin__.active_user
    #Print prompt and wait for input
    user_select = raw_input("Engineering | Roster | Salvage | Science | Galactic Market | Exit".center(80) + "\n\n" + 
        prompt(user))
    #Check command to see if it was a special case i.e. exit
    result = command_process(user_select)
    if result == "null":
        print "Invalid Selection.  Please try again.\n"
        get_selection()
    else:
        return str(user_select)

def ship_hanger():
    #Set user variable for simplicity
    user = __builtin__.active_user
    #Clear the screen
    os.system('clear')
    #Generate the view file
    result = view_generator()
    #Check to see that it completed successfully.  If it didn't, exit gracefully.  If it did, show view.
    if result:
        hanger_screen = open("./Data/ship_hanger.txt", 'r')
        for line in hanger_screen:
            sys.stdout.write(line)
        print "\n"
        os.remove("./Data/ship_hanger.txt")
    else:
        print "Error creating ship hanger view.  Exiting."
        sys.exit(1)
    #Print player ship list with names
    file_path = "./Players/" + user + ".data"
    # Import player.json data
    with open(file_path) as player_data:
        player_json = json.load(player_data)
    selection = get_selection()
    #Check command, and if "back" return to previous screen
    if selection.lower() == "back":
        selection_screen.selection_screen()
    elif selection.lower() == "roster":
        os.system('clear')
        roster_view(user)
    elif selection.lower() == "science":
        science_view()
		