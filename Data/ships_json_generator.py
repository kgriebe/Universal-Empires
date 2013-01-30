#!/usr/bin/python

import re
import json

# Open files and define dictionaries
RUFS_ship_file = open("RUFS_ships.json", 'w')
AMV_ship_file = open("AMV_ships.json", 'w')
LBS_ship_file = open("LBS_ships.json", 'w')
DIC_ship_file = open("DIC_ships.json", 'w')
STS_ship_file = open("STS_ships.json", 'w')
RUFS_ship_dict = {}
AMV_ship_dict = {}
LBS_ship_dict = {}
DIC_ship_dict = {}
STS_ship_dict = {}
ships_attrs = {}
ship_attrs_json = {}

# Create the dictionaries by reading from a manually created file housing a list of ships with
# identity numbers and rarity numbers.  Sort the file into a dictionary for each race.
def dict_creator(file):
	f = open(file, 'r')

	for line in f:
		ship_name = re.search(r'(\d+)\s(\w+)\s(.+)\s\((\d)\)', line)
		if ship_name:
			if ship_name.group(2) == "RUFS":
				RUFS_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]
			elif ship_name.group(2) == "AMV":
				AMV_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]
			elif ship_name.group(2) == "LBS":
				LBS_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]
			elif ship_name.group(2) == "DIC":
				DIC_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]
			elif ship_name.group(2) == "STS":
				STS_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]		

# Update the values of the dictionary so it has the ship name, rarity, and identity number.
# Json format the string and write it to the appropriate ship file.
def dict_update():
	# Define default attributes
	ship_attrs = {"name": "Default", "exp": 0, "level": 0, "max_level": 0, "ident": 0, 
	"rarity": 0, "shield_points": 0, "repair_rate": 0, "damage_reduction": 0, 
	"damage_reduction_type": 0, "attack_value": 0, "speed": 0, "skill": 0, "weapon_mod": 0, 
	"shield_mod": 0, "engine_mod": 0, "damage_type": 0, "weapon_hardpoint": 0, 
	"armor_hardpoint": 0, "shield_hardpoint": 0, "engine_hardpoint": 0, "fleet_leader_skill": ""}

	""" Iterate over the ship dictionaries, convert the value tuple (containing id number and
		rarity number) into a list so it can be accessed via index.  Format json and assign it
		variable, then write it to file"""
	for ship, value in RUFS_ship_dict.iteritems():
		attribute_list = list(value)
		ship_attrs = {"name": ship, "exp": 0, "level": 0, "max_level": 0, "ident": attribute_list[1], 
	"rarity": attribute_list[0], "shield_points": 0, "repair_rate": 0, "damage_reduction": 0, 
	"damage_reduction_type": 0, "attack_value": 0, "speed": 0, "skill": 0, "weapon_mod": 0, 
	"shield_mod": 0, "engine_mod": 0, "damage_type": 0, "weapon_hardpoint": 0, 
	"armor_hardpoint": 0, "shield_hardpoint": 0, "engine_hardpoint": 0, "fleet_leader_skill": ""}
		string = json.dumps({attribute_list[1]:ship_attrs})
		RUFS_ship_file.write(string + "," + "\n")

	for ship, value in AMV_ship_dict.iteritems():
		attribute_list = list(value)
		ship_attrs = {"name": ship, "exp": 0, "level": 0, "max_level": 0, "ident": attribute_list[1], 
	"rarity": attribute_list[0], "shield_points": 0, "repair_rate": 0, "damage_reduction": 0, 
	"damage_reduction_type": 0, "attack_value": 0, "speed": 0, "skill": 0, "weapon_mod": 0, 
	"shield_mod": 0, "engine_mod": 0, "damage_type": 0, "weapon_hardpoint": 0, 
	"armor_hardpoint": 0, "shield_hardpoint": 0, "engine_hardpoint": 0, "fleet_leader_skill": ""}
		string = json.dumps({attribute_list[1]:ship_attrs})
		AMV_ship_file.write(string + "," + "\n")

	for ship, value in LBS_ship_dict.iteritems():
		attribute_list = list(value)
		ship_attrs = {"name": ship, "exp": 0, "level": 0, "max_level": 0, "ident": attribute_list[1], 
	"rarity": attribute_list[0], "shield_points": 0, "repair_rate": 0, "damage_reduction": 0, 
	"damage_reduction_type": 0, "attack_value": 0, "speed": 0, "skill": 0, "weapon_mod": 0, 
	"shield_mod": 0, "engine_mod": 0, "damage_type": 0, "weapon_hardpoint": 0, 
	"armor_hardpoint": 0, "shield_hardpoint": 0, "engine_hardpoint": 0, "fleet_leader_skill": ""}
		string = json.dumps({attribute_list[1]:ship_attrs})
		LBS_ship_file.write(string + "," + "\n")

	for ship, value in DIC_ship_dict.iteritems():
		attribute_list = list(value)
		ship_attrs = {"name": ship, "exp": 0, "level": 0, "max_level": 0, "ident": attribute_list[1], 
	"rarity": attribute_list[0], "shield_points": 0, "repair_rate": 0, "damage_reduction": 0, 
	"damage_reduction_type": 0, "attack_value": 0, "speed": 0, "skill": 0, "weapon_mod": 0, 
	"shield_mod": 0, "engine_mod": 0, "damage_type": 0, "weapon_hardpoint": 0, 
	"armor_hardpoint": 0, "shield_hardpoint": 0, "engine_hardpoint": 0, "fleet_leader_skill": ""}
		string = json.dumps({attribute_list[1]:ship_attrs})
		DIC_ship_file.write(string + "," + "\n")

	for ship, value in STS_ship_dict.iteritems():
		attribute_list = list(value)
		ship_attrs = {"name": ship, "exp": 0, "level": 0, "max_level": 0, "ident": attribute_list[1], 
	"rarity": attribute_list[0], "shield_points": 0, "repair_rate": 0, "damage_reduction": 0, 
	"damage_reduction_type": 0, "attack_value": 0, "speed": 0, "skill": 0, "weapon_mod": 0, 
	"shield_mod": 0, "engine_mod": 0, "damage_type": 0, "weapon_hardpoint": 0, 
	"armor_hardpoint": 0, "shield_hardpoint": 0, "engine_hardpoint": 0, "fleet_leader_skill": ""}
		string = json.dumps({attribute_list[1]:ship_attrs})
		STS_ship_file.write(string + "," + "\n")

def main():
	dict_creator("Ships.txt")

	dict_update()
	STS_ship_file.close()
	DIC_ship_file.close()
	LBS_ship_file.close()
	AMV_ship_file.close()
	RUFS_ship_file.close()

if __name__ == "__main__":
        main()