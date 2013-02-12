#!/usr/bin/python

import json

def prompt(user):
	file_path = "./Players/" + user + ".data"
	with open(file_path) as player_data:
		player_json = json.load(player_data)

	string = "<{ Fuel Rods: %s/%s Credits: %s }> " % (player_json[user]["fuel_rods"], player_json[user]["max_fuel_rods"], player_json[user]["credits"])
	return string