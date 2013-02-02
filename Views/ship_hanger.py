#!/usr/bin/python

import os
import sys
import __builtin__
import json

full_line = "		  ************************************************************		  \n"
beginning_line = "		  **********"
end_line = "**********		  \n"
hanger_view = open('./Data/ship_hanger.txt', 'r+')

def view_generator():
	#Write the lines of stars
	hanger_view.write(full_line)
	#Set announcement line and write to file
	announcement = "Your Current Fleet Is:"
	announcement_line = beginning_line + announcement.center(40) + end_line
	hanger_view.write(announcement_line)
	#Set empty line and write to file
	empty_line = beginning_line + " ".center(40) + end_line
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
		ship = ship_json[str(id)]["race"] + " " + ship_json[str(id)]["name"]
		line = beginning_line + ship.center(40) + end_line
		hanger_view.write(line)
	hanger_view.write(empty_line)
	hanger_view.write(full_line)



	
def ship_hanger():
	os.system('clear')
	view_generator()
	hanger_screen = open('./Data/ship_hanger.txt', 'r')
	for line in hanger_screen:
		sys.stdout.write(line)
	print "\n"

