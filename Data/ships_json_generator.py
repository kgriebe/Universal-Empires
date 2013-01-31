#!/usr/bin/python

import re
import json

# Open files and define dictionaries
RUFS_ship_file = open("RUFS_ships.json", 'w')
AMV_ship_file = open("AMV_ships.json", 'w')
LBS_ship_file = open("LBS_ships.json", 'w')
DIC_ship_file = open("DIC_ships.json", 'w')
STS_ship_file = open("STS_ships.json", 'w')
id_file = open("ship_ids.json", 'w')
RUFS_ship_dict = {}
AMV_ship_dict = {}
LBS_ship_dict = {}
DIC_ship_dict = {}
STS_ship_dict = {}
ships_attrs = {}
id_dict = {}

# Create the dictionaries by reading from a manually created file housing a list of ships with
# identity numbers and rarity numbers.  Sort the file into a dictionary for each race.
def dict_creator(file):
	f = open(file, 'r')

	for line in f:
		ship_name = re.search(r'(\d+)\s(\w+)\s(.+)\s\((\d)\)', line)
		if ship_name:
			if ship_name.group(2) == "RUFS":
				RUFS_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]
				id_dict[ship_name.group(1)] = [ship_name.group(2)]
			elif ship_name.group(2) == "AMV":
				AMV_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]
				id_dict[ship_name.group(1)] = [ship_name.group(2)]
			elif ship_name.group(2) == "LBS":
				LBS_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]
				id_dict[ship_name.group(1)] = [ship_name.group(2)]
			elif ship_name.group(2) == "DIC":
				DIC_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]
				id_dict[ship_name.group(1)] = [ship_name.group(2)]
			elif ship_name.group(2) == "STS":
				STS_ship_dict[ship_name.group(3)] = [ship_name.group(4), ship_name.group(1)]
				id_dict[ship_name.group(1)] = [ship_name.group(2)]
	json_string = json.dumps(id_dict)
	id_file.write(json_string)

# Update the values of the dictionary so it has the ship name, rarity, and identity number.
# Json format the string and write it to the appropriate ship file.
def dict_update():
    	# Define default attributes
    	RUFS_ships = {}
    	AMV_ships = {}
    	LBS_ships = {}
    	DIC_ships = {}
    	STS_ships = {}
    	
    	ship_attrs_base = {"exp": 0, "level": 0, "max_level": 0, "shield_points": 0, "repair_rate": 0, 
    "damage_reduction": 0, "damage_reduction_type": 0, "attack_value": 0, "speed": 0, "skill": 0, 
    "weapon_mod": 0, "shield_mod": 0, "engine_mod": 0, "damage_type": 0, "weapon_hardpoint": 0, 
    "armor_hardpoint": 0, "shield_hardpoint": 0, "engine_hardpoint": 0, "fleet_leader_skill": ""}

    	""" Iterate over key:value pairs in dicts created by dict_creator, then create new dict containing the base attributes plus
    	newly defined attributes, then insert that into a new dictionary with the id number as the key for each object.  Then convert
    	to json and dump to file."""
    	for ship_name, rare_id in RUFS_ship_dict.iteritems():
    		ship_attrs = dict(ship_attrs_base.items() + [('name', ship_name), ('ident', rare_id[1]), ('rarity', rare_id[0])])
    		RUFS_ships[rare_id[1]] = ship_attrs
    	string = json.dumps(RUFS_ships)
    	RUFS_ship_file.write(string)
    
        for ship_name, rare_id in AMV_ship_dict.iteritems():
    		ship_attrs = dict(ship_attrs_base.items() + [('name', ship_name), ('ident', rare_id[1]), ('rarity', rare_id[0])])
    		AMV_ships[rare_id[1]] = ship_attrs
    	string = json.dumps(AMV_ships)
    	AMV_ship_file.write(string)
    	
    	for ship_name, rare_id in LBS_ship_dict.iteritems():
    		ship_attrs = dict(ship_attrs_base.items() + [('name', ship_name), ('ident', rare_id[1]), ('rarity', rare_id[0])])
    		LBS_ships[rare_id[1]] = ship_attrs
    	string = json.dumps(LBS_ships)
    	LBS_ship_file.write(string)
    	
    	for ship_name, rare_id in DIC_ship_dict.iteritems():
    		ship_attrs = dict(ship_attrs_base.items() + [('name', ship_name), ('ident', rare_id[1]), ('rarity', rare_id[0])])
    		DIC_ships[rare_id[1]] = ship_attrs
    	string = json.dumps(DIC_ships)
    	DIC_ship_file.write(string)
    	
    	for ship_name, rare_id in STS_ship_dict.iteritems():
    		ship_attrs = dict(ship_attrs_base.items() + [('name', ship_name), ('ident', rare_id[1]), ('rarity', rare_id[0])])
    		STS_ships[rare_id[1]] = ship_attrs
    	string = json.dumps(STS_ships)
    	STS_ship_file.write(string)

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