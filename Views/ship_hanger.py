#!/usr/bin/python

import os
import sys
import __builtin__
import json
from Controllers.commands import command_process
import selection_screen

def view_generator():
	#Open file
	hanger_view = open('./Data/ship_hanger.txt', 'w+')

	#Define Variables
	full_line = "************************************************************".center(80) + "\n"
	beginning_line = "          *****"
	end_line = "*****          " + "\n"
	empty_line = beginning_line + " ".center(50) + end_line

	#Write the lines of stars
	hanger_view.write(full_line)
	hanger_view.write(full_line)
	hanger_view.write(full_line)
	hanger_view.write(empty_line)

	#Set announcement line and write to file
	announcement = "Your Current Fleet Is:"
	announcement_line = beginning_line + announcement.center(50) + end_line
	hanger_view.write(announcement_line)
	hanger_view.write(empty_line)

	#Print player ship list with names
	file_path = "./Players/" + __builtin__.active_user + ".data"
	with open(file_path) as player_data:
		player_json = json.load(player_data)

	ship_file_path = "./Data/ships.json"
#	ship_file_path = "./Data/" + player_json[__builtin__.active_user]["race"].upper() + "_ships.json"
	
	with open(ship_file_path) as ship_file_json:
		ship_json = json.load(ship_file_json)
	
	for id in player_json[__builtin__.active_user]["ship_list"]:
		ship = "[ " + str(id) + " ] " + ship_json[str(id)]["race"] + " " + ship_json[str(id)]["name"]
		line = beginning_line + "     " + ship + " ".ljust(45 - len(ship)) + end_line
		hanger_view.write(line)
	
	hanger_view.write(empty_line)
	# closing1 = "Enter ship identification number"
	# closing2 = "for more information:"
	# closing_line1 = beginning_line + closing1.center(50) + end_line
	# closing_line2 = beginning_line + closing2.center(50) + end_line
	# hanger_view.write(closing_line1)
	# hanger_view.write(closing_line2)
	# hanger_view.write(empty_line)
	hanger_view.write(full_line)
	hanger_view.write(full_line)
	hanger_view.write(full_line)
	return "Success"
	
def ship_hanger():
	os.system('clear')
	result = view_generator()
	if result:
		hanger_screen = open("./Data/ship_hanger.txt", 'r')
		for line in hanger_screen:
			sys.stdout.write(line)
		print "\n"
		os.remove("./Data/ship_hanger.txt")
	else:
		print "Error creating ship hanger view.  Exiting."
		sys.exit(1)
	selection = raw_input("Enter ship identification number for more information: ")
	result = command_process(selection)
	if selection.lower() == "back":
		selection_screen.selection_screen()
	if result:
		print "Worked!"


