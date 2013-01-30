#!/bin/python
from Classes.ships import ship
import re
import json
from pprint import pprint


def id_search(id_num):
	with open('./Data/AMV_ships.json') as amv:
		amv_json = json.load(amv)
	with open('./Data/DIC_ships.json') as dic:
		dic_json = json.load(dic)
	with open('./Data/LBS_ships.json') as lbs:
		lbs_json = json.load(lbs)
	with open('./Data/RUFS_ships.json') as rufs:
		rufs_json = json.load(rufs)
	with open('./Data/STS_ships.json') as sts:
		sts_json = json.load(sts)

	if id_num in amv_json:
		print "AMV"
	elif id_num in dic_json:
		print "DIC"
		
	elif id_num in lbs_json:
		print "LBS"
	elif id_num in rufs_json:
		print "RUFS"
	elif id_num in sts_json:
		print "STS"
	else:
		print "Error, ID not found in any ship database."
	


def new_ship():
	"""Here we define the attributes that every ship possesses.  This allows us to
	iterate through the list and assign all these variables when the object is instantiated
	without having to type in one line of code for each attribute."""
	ship_attrs = ["name", "exp", "level", "max_level", "ident", "rarity", "shield_points",
	 "repair_rate", "damage_reduction", "damage_reduction_type", "attack_value", "speed", 
	 "skill", "weapon_mod", "shield_mod", "engine_mod", "damage_type", "weapon_hardpoint", 
	 "armor_hardpoint", "shield_hardpoint", "engine_hardpoint", "fleet_leader_skill"]

	"""Open the file and parse the json data within.""" 
	with open('./Data/ships.json') as f:
		d = json.load(f)

	"""Call the ship function from the ships module."""	
	new_ship_obj = ship()

	"""Iterate through attribute list and assign the proper value for each ship."""
	for attr in ship_attrs:
		setattr(new_ship_obj, attr, d[id_num][attr])
#		Debug
#		x = getattr(new_ship_obj, attr)
#		print x
	print new_ship_obj
