#!/usr/bin/python

import os, sys
import json
import random
from collections import defaultdict



# Define Variables
hp_cost = 1
attack_cost = 3
repair_cost = 1.5

rare1_max_levels = 16
rare2_max_levels = 26
rare3_max_levels = 51
rare4_max_levels = 76
rare5_max_levels = 100

support = {"hp": 4, "attack": 2, "repair": 6}
defense_platform = {"hp": 7, "attack": 1, "repair": 3}
cruiser = {"hp": 5, "attack": 6, "repair": 3}
interdictor = {"hp": 2, "attack": 5, "repair": 1}
carrier = {"hp": 6, "attack": 2, "repair": 7}
corvette = {"hp": 3, "attack": 4, "repair": 2}
bomber = {"hp": 1, "attack": 7, "repair": 1}
fighter = {"hp": 2, "attack": 4, "repair": 2}
dreadnaught = {"hp": 9, "attack": 8, "repair": 3}
leviathan = {"hp": 10, "attack": 9, "repair": 4}
super_destroyer = {"hp": 6, "attack": 10, "repair": 3}
star_station = {"hp": 10, "attack": 8, "repair": 7}
harvester = {"hp": 4, "attack": 2, "repair": 5}
mine_layer = {"hp": 2, "attack": 6, "repair": 2}
targetting_ship = {"hp": 2, "attack": 7, "repair": 3}
mobile_fleet_depot = {"hp": 8, "attack": 3, "repair": 10}
destroyer = {"hp": 3, "attack": 6, "repair": 2}
battleship = {"hp": 7, "attack": 8, "repair": 4}

def main():
    with open('ships.json') as ships_json:
        ships_data = json.load(ships_json)
    ship_hp_dict = {}
    ship_repair_dict = {}
    ship_attack_dict = {}
    hp_table_file = open('hp.json', 'w')
    support1_hp_dict = {}
    support2_hp_dict = {}
    support3_hp_dict = {}
    support4_hp_dict = {}
    support5_hp_dict = {}

    for i in range(1, 25): #Support
        id = i
        id = str(id)
        level_hp = 0
        level_dict = {}
        if ships_data[str(i)]["rarity"] == 1:
            max_hp = support["hp"] * 100
            choice_min = -10 * support["hp"]
            choice_max = 10 * support["hp"]
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(choice_min, choice_max)
                level_dict[str(i)] = level_hp
            ident = ships_data[id]["ident"]
            support1_hp_dict[ident] = level_dict
        elif ships_data[str(i)]["rarity"] == 2:
            support2_hp_dict = {}
            max_hp = support["hp"] * 150
            choice_min = -10 * support["hp"]
            choice_max = 10 * support["hp"]
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(choice_min, choice_max)
                level_dict[str(i)] = level_hp
            ident = ships_data[id]["ident"]
            support2_hp_dict[ident] = level_dict
        elif ships_data[str(i)]["rarity"] == 3:
            support3_hp_dict = {}
            max_hp = support["hp"] * 250
            choice_min = -10 * support["hp"]
            choice_max = 10 * support["hp"]
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(choice_min, choice_max)
                level_dict[str(i)] = level_hp
            ident = ships_data[id]["ident"]            
            support3_hp_dict[ident] = level_dict
        elif ships_data[str(i)]["rarity"] == 4:
            support4_hp_dict = {}
            max_hp = support["hp"] * 500
            choice_min = -10 * support["hp"]
            choice_max = 10 * support["hp"]
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(choice_min, choice_max)
                level_dict[str(i)] = level_hp
            ident = ships_data[id]["ident"]
            support4_hp_dict[ident] = level_dict
        elif ships_data[str(i)]["rarity"] == 5:
            support5_hp_dict = {}
            max_hp = support["hp"] * 1000
            choice_min = -10 * support["hp"]
            choice_max = 10 * support["hp"]
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(choice_min, choice_max)
                level_dict[str(i)] = level_hp
            ident = ships_data[id]["ident"]
            support5_hp_dict[ident] = level_dict
        ship_hp_dict.update(support1_hp_dict)
        ship_hp_dict.update(support2_hp_dict)
        ship_hp_dict.update(support3_hp_dict)
        ship_hp_dict.update(support4_hp_dict)
        ship_hp_dict.update(support5_hp_dict)
    print ship_hp_dict
    file_data = json.dumps(ship_hp_dict)
    hp_table_file.write(file_data)
    for i in range(26, 51): #Defense Platforms
        pass
    for i in range(51, 76): #Cruiser
        pass
    for i in range(76, 101): #Interdictors
        pass
    for i in range(101, 121): #Carrier
        pass
    for i in range(121, 146): #Corvette
        pass
    for i in range(146, 171): #Bomber
        pass
    for i in range(171, 196): #Fighter
        pass
    for i in range(196, 211): #Dreadnaught
        pass
    for i in range(211, 221): #Leviathan
        pass
    for i in range(221, 231): #Super Destroyer
        pass
    for i in range(231, 236): #Star Station
        pass
    for i in range(236, 261): #Harvesters
        pass
    for i in range(261, 286): #Mine Layers
        pass
    for i in range(286, 311): #Targetting Ships
        pass
    for i in range(311, 336): #Mobile Fleet Depot
        pass
    for i in range(336, 361): #Destroyers
        pass
    for i in range(361, 386): #Battleships
        pass
    
if __name__ == "__main__":
    main()
