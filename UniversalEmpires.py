#!/usr/bin/python

from Classes.ships import *
from Players.new_player import *
from Players.login import *
from Classes.new_ship import *
import json
import os

starter_ships = ()
with open("./Data/RUFS_ships.json") as RUFS_json:
    RUFS_ships = json.load(RUFS_json)
with open("./Data/AMV_ships.json") as AMV_json:
    AMV_ships = json.load(AMV_json)
with open("./Data/DIC_ships.json") as DIC_json:
    DIC_ships = json.load(DIC_json)
with open("./Data/LBS_ships.json") as LBS_json:
    LBS_ships = json.load(LBS_json)    
with open("./Data/STS_ships.json") as STS_json:
    STS_ships = json.load(STS_json)
with open("./Data/ship_ids.json") as ship_ids:
    id_dict = dict(json.load(ship_ids))

def main():
    
# 	Prompt for login, load player data after login or player creation
    player_name = login()
    file_path = "./Players/" + player_name    
    with open(file_path) as player_data:
    	player_json = json.load(player_data)

# Searching player file, comparing to ships files, printing ships player has.
    print "Your starting ships are:"
    for ship_id in player_json[player_name]["ship_list"]:
        race = id_dict[str(ship_id)]
        if str(ship_id) in RUFS_ships:
            print "RUFS " + RUFS_ships[str(ship_id)]["name"]
        elif str(ship_id) in AMV_ships:
            print "AMV " + AMV_ships[str(ship_id)]["name"]
        elif str(ship_id) in DIC_ships:
            print "DIC " + DIC_ships[str(ship_id)]["name"]
        elif str(ship_id) in LBS_ships:
            print "LBS " + LBS_ships[str(ship_id)]["name"]
        elif str(ship_id) in STS_ships:
            print "STS " + STS_ships[str(ship_id)]["name"]
        else:
            print "Could not find ship id."    

 	   
if __name__ == "__main__":
        main()