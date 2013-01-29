#!/bin/python
from Classes.ships import ship
import re
import json
from pprint import pprint

def new_ship(id_num):
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
