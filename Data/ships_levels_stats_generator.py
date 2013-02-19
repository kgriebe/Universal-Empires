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
rare5_max_levels = 7 *0

support = {"hp": 4, "attack": 2, "repair": 6}
defense = {"hp": 7, "attack": 1, "repair": 3}
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
targetting = {"hp": 2, "attack": 7, "repair": 3}
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
    attack_table_file = open('attack.json', 'w')
    repair_table_file = open('repair.json', 'w')
    support1_hp_dict = {}
    support2_hp_dict = {}
    support3_hp_dict = {}
    support4_hp_dict = {}
    support5_hp_dict = {}
    support1_attack_dict = {}
    support2_attack_dict = {}
    support3_attack_dict = {}
    support4_attack_dict = {}
    support5_attack_dict = {}
    support1_repair_dict = {}
    support2_repair_dict = {}
    support3_repair_dict = {}
    support4_repair_dict = {}
    support5_repair_dict = {}
    defense1_hp_dict = {}
    defense2_hp_dict = {}
    defense3_hp_dict = {}
    defense4_hp_dict = {}
    defense5_hp_dict = {}
    defense1_attack_dict = {}
    defense2_attack_dict = {}
    defense3_attack_dict = {}
    defense4_attack_dict = {}
    defense5_attack_dict = {}
    defense1_repair_dict = {}
    defense2_repair_dict = {}
    defense3_repair_dict = {}
    defense4_repair_dict = {}
    defense5_repair_dict = {}
    cruiser1_hp_dict = {}
    cruiser2_hp_dict = {}
    cruiser3_hp_dict = {}
    cruiser4_hp_dict = {}
    cruiser5_hp_dict = {}
    cruiser1_attack_dict = {}
    cruiser2_attack_dict = {}
    cruiser3_attack_dict = {}
    cruiser4_attack_dict = {}
    cruiser5_attack_dict = {}
    cruiser1_repair_dict = {}
    cruiser2_repair_dict = {}
    cruiser3_repair_dict = {}
    cruiser4_repair_dict = {}
    cruiser5_repair_dict = {}
    interdictor1_hp_dict = {}
    interdictor2_hp_dict = {}
    interdictor3_hp_dict = {}
    interdictor4_hp_dict = {}
    interdictor5_hp_dict = {}
    interdictor1_attack_dict = {}
    interdictor2_attack_dict = {}
    interdictor3_attack_dict = {}
    interdictor4_attack_dict = {}
    interdictor5_attack_dict = {}
    interdictor1_repair_dict = {}
    interdictor2_repair_dict = {}
    interdictor3_repair_dict = {}
    interdictor4_repair_dict = {}
    interdictor5_repair_dict = {}
    carrier1_hp_dict = {}
    carrier2_hp_dict = {}
    carrier3_hp_dict = {}
    carrier4_hp_dict = {}
    carrier5_hp_dict = {}
    carrier1_attack_dict = {}
    carrier2_attack_dict = {}
    carrier3_attack_dict = {}
    carrier4_attack_dict = {}
    carrier5_attack_dict = {}
    carrier1_repair_dict = {}
    carrier2_repair_dict = {}
    carrier3_repair_dict = {}
    carrier4_repair_dict = {}
    carrier5_repair_dict = {}
    corvette1_hp_dict = {}
    corvette2_hp_dict = {}
    corvette3_hp_dict = {}
    corvette4_hp_dict = {}
    corvette5_hp_dict = {}
    corvette1_attack_dict = {}
    corvette2_attack_dict = {}
    corvette3_attack_dict = {}
    corvette4_attack_dict = {}
    corvette5_attack_dict = {}
    corvette1_repair_dict = {}
    corvette2_repair_dict = {}
    corvette3_repair_dict = {}
    corvette4_repair_dict = {}
    corvette5_repair_dict = {}
    bomber1_hp_dict = {}
    bomber2_hp_dict = {}
    bomber3_hp_dict = {}
    bomber4_hp_dict = {}
    bomber5_hp_dict = {}
    bomber1_attack_dict = {}
    bomber2_attack_dict = {}
    bomber3_attack_dict = {}
    bomber4_attack_dict = {}
    bomber5_attack_dict = {}
    bomber1_repair_dict = {}
    bomber2_repair_dict = {}
    bomber3_repair_dict = {}
    bomber4_repair_dict = {}
    bomber5_repair_dict = {}
    fighter1_hp_dict = {}
    fighter2_hp_dict = {}
    fighter3_hp_dict = {}
    fighter4_hp_dict = {}
    fighter5_hp_dict = {}
    fighter1_attack_dict = {}
    fighter2_attack_dict = {}
    fighter3_attack_dict = {}
    fighter4_attack_dict = {}
    fighter5_attack_dict = {}
    fighter1_repair_dict = {}
    fighter2_repair_dict = {}
    fighter3_repair_dict = {}
    fighter4_repair_dict = {}
    fighter5_repair_dict = {}
    dreadnaught1_hp_dict = {}
    dreadnaught2_hp_dict = {}
    dreadnaught3_hp_dict = {}
    dreadnaught4_hp_dict = {}
    dreadnaught5_hp_dict = {}
    dreadnaught1_attack_dict = {}
    dreadnaught2_attack_dict = {}
    dreadnaught3_attack_dict = {}
    dreadnaught4_attack_dict = {}
    dreadnaught5_attack_dict = {}
    dreadnaught1_repair_dict = {}
    dreadnaught2_repair_dict = {}
    dreadnaught3_repair_dict = {}
    dreadnaught4_repair_dict = {}
    dreadnaught5_repair_dict = {}
    leviathan1_hp_dict = {}
    leviathan2_hp_dict = {}
    leviathan3_hp_dict = {}
    leviathan4_hp_dict = {}
    leviathan5_hp_dict = {}
    leviathan1_attack_dict = {}
    leviathan2_attack_dict = {}
    leviathan3_attack_dict = {}
    leviathan4_attack_dict = {}
    leviathan5_attack_dict = {}
    leviathan1_repair_dict = {}
    leviathan2_repair_dict = {}
    leviathan3_repair_dict = {}
    leviathan4_repair_dict = {}
    leviathan5_repair_dict = {}
    super_destroyer1_hp_dict = {}
    super_destroyer2_hp_dict = {}
    super_destroyer3_hp_dict = {}
    super_destroyer4_hp_dict = {}
    super_destroyer5_hp_dict = {}
    super_destroyer1_attack_dict = {}
    super_destroyer2_attack_dict = {}
    super_destroyer3_attack_dict = {}
    super_destroyer4_attack_dict = {}
    super_destroyer5_attack_dict = {}
    super_destroyer1_repair_dict = {}
    super_destroyer2_repair_dict = {}
    super_destroyer3_repair_dict = {}
    super_destroyer4_repair_dict = {}
    super_destroyer5_repair_dict = {}
    star_station1_hp_dict = {}
    star_station2_hp_dict = {}
    star_station3_hp_dict = {}
    star_station4_hp_dict = {}
    star_station5_hp_dict = {}
    star_station1_attack_dict = {}
    star_station2_attack_dict = {}
    star_station3_attack_dict = {}
    star_station4_attack_dict = {}
    star_station5_attack_dict = {}
    star_station1_repair_dict = {}
    star_station2_repair_dict = {}
    star_station3_repair_dict = {}
    star_station4_repair_dict = {}
    star_station5_repair_dict = {}
    harvester1_hp_dict = {}
    harvester2_hp_dict = {}
    harvester3_hp_dict = {}
    harvester4_hp_dict = {}
    harvester5_hp_dict = {}
    harvester1_attack_dict = {}
    harvester2_attack_dict = {}
    harvester3_attack_dict = {}
    harvester4_attack_dict = {}
    harvester5_attack_dict = {}
    harvester1_repair_dict = {}
    harvester2_repair_dict = {}
    harvester3_repair_dict = {}
    harvester4_repair_dict = {}
    harvester5_repair_dict = {}
    mine_layer1_hp_dict = {}
    mine_layer2_hp_dict = {}
    mine_layer3_hp_dict = {}
    mine_layer4_hp_dict = {}
    mine_layer5_hp_dict = {}
    mine_layer1_attack_dict = {}
    mine_layer2_attack_dict = {}
    mine_layer3_attack_dict = {}
    mine_layer4_attack_dict = {}
    mine_layer5_attack_dict = {}
    mine_layer1_repair_dict = {}
    mine_layer2_repair_dict = {}
    mine_layer3_repair_dict = {}
    mine_layer4_repair_dict = {}
    mine_layer5_repair_dict = {}
    targetting1_hp_dict = {}
    targetting2_hp_dict = {}
    targetting3_hp_dict = {}
    targetting4_hp_dict = {}
    targetting5_hp_dict = {}
    targetting1_attack_dict = {}
    targetting2_attack_dict = {}
    targetting3_attack_dict = {}
    targetting4_attack_dict = {}
    targetting5_attack_dict = {}
    targetting1_repair_dict = {}
    targetting2_repair_dict = {}
    targetting3_repair_dict = {}
    targetting4_repair_dict = {}
    targetting5_repair_dict = {}
    mobile_fleet_depot1_hp_dict = {}
    mobile_fleet_depot2_hp_dict = {}
    mobile_fleet_depot3_hp_dict = {}
    mobile_fleet_depot4_hp_dict = {}
    mobile_fleet_depot5_hp_dict = {}
    mobile_fleet_depot1_attack_dict = {}
    mobile_fleet_depot2_attack_dict = {}
    mobile_fleet_depot3_attack_dict = {}
    mobile_fleet_depot4_attack_dict = {}
    mobile_fleet_depot5_attack_dict = {}
    mobile_fleet_depot1_repair_dict = {}
    mobile_fleet_depot2_repair_dict = {}
    mobile_fleet_depot3_repair_dict = {}
    mobile_fleet_depot4_repair_dict = {}
    mobile_fleet_depot5_repair_dict = {}
    destroyer1_hp_dict = {}
    destroyer2_hp_dict = {}
    destroyer3_hp_dict = {}
    destroyer4_hp_dict = {}
    destroyer5_hp_dict = {}
    destroyer1_attack_dict = {}
    destroyer2_attack_dict = {}
    destroyer3_attack_dict = {}
    destroyer4_attack_dict = {}
    destroyer5_attack_dict = {}
    destroyer1_repair_dict = {}
    destroyer2_repair_dict = {}
    destroyer3_repair_dict = {}
    destroyer4_repair_dict = {}
    destroyer5_repair_dict = {}
    battleship1_hp_dict = {}
    battleship2_hp_dict = {}
    battleship3_hp_dict = {}
    battleship4_hp_dict = {}
    battleship5_hp_dict = {}
    battleship1_attack_dict = {}
    battleship2_attack_dict = {}
    battleship3_attack_dict = {}
    battleship4_attack_dict = {}
    battleship5_attack_dict = {}
    battleship1_repair_dict = {}
    battleship2_repair_dict = {}
    battleship3_repair_dict = {}
    battleship4_repair_dict = {}
    battleship5_repair_dict = {}

    
    for i in range(1, 25): #Support
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
        
        if ships_data[str(i)]["rarity"] == 1:
            
            #Define values for level-level variation
            max_hp = support["hp"] * 100
            max_attack = support["attack"] * 20
            max_repair = support["repair"] * 10
            hp_choice_min = 1 * support["hp"]
            attack_choice_min = 1 * support["attack"]
            repair_choice_min = 1 * support["repair"]
            hp_choice_max = 2 * support["hp"]
            attack_choice_max = 2 * support["attack"]
            repair_choice_max = 2 * support["repair"]
            
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
                
            ident = ships_data[id]["ident"]
            support1_hp_dict[ident] = level_hp_dict
            support1_attack_dict[ident] = level_attack_dict
            support1_repair_dict[ident] = level_repair_dict
            
        elif ships_data[str(i)]["rarity"] == 2:
            
            #Define values for level-level variation
            max_hp = support["hp"] * 150
            max_attack = support["attack"] * 30
            max_repair = support["repair"] * 15
            hp_choice_min = 1 * support["hp"]
            attack_choice_min = 1 * support["attack"]
            repair_choice_min = 1 * support["repair"]
            hp_choice_max = 3 * support["hp"]
            attack_choice_max = 3 * support["attack"]
            repair_choice_max = 3 * support["repair"]
            
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
                
            ident = ships_data[id]["ident"]
            support2_hp_dict[ident] = level_hp_dict
            support2_attack_dict[ident] = level_attack_dict
            support2_repair_dict[ident] = level_repair_dict
            
        elif ships_data[str(i)]["rarity"] == 3:
            
            #Define values for level-level variation
            max_hp = support["hp"] * 250
            max_attack = support["attack"] * 50
            max_repair = support["repair"] * 25
            hp_choice_min = 1 * support["hp"]
            attack_choice_min = 1 * support["attack"]
            repair_choice_min = 1 * support["repair"]
            hp_choice_max = 4 * support["hp"]
            attack_choice_max = 4 * support["attack"]
            repair_choice_max = 4 * support["repair"]
            
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
                
            ident = ships_data[id]["ident"]
            support3_hp_dict[ident] = level_hp_dict
            support3_attack_dict[ident] = level_attack_dict
            support3_repair_dict[ident] = level_repair_dict
            
        elif ships_data[str(i)]["rarity"] == 4:
            
            #Define values for level-level variation
            max_hp = support["hp"] * 500
            max_attack = support["attack"] * 100
            max_repair = support["repair"] * 50
            hp_choice_min =  4 * support["hp"]
            attack_choice_min = 1 * support["attack"]
            repair_choice_min = 1 * support["repair"]
            hp_choice_max = 5 * support["hp"]
            attack_choice_max = 5 * support["attack"]
            repair_choice_max = 5 * support["repair"]
            
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
                
            ident = ships_data[id]["ident"]
            support4_hp_dict[ident] = level_hp_dict
            support4_attack_dict[ident] = level_attack_dict
            support4_repair_dict[ident] = level_repair_dict
            
        elif ships_data[str(i)]["rarity"] == 5:
            
            #Define values for level-level variation
            max_hp = support["hp"] * 1000
            max_attack = support["attack"] * 200
            max_repair = support["repair"] * 100
            hp_choice_min = 1 * support["hp"]
            attack_choice_min = 1 * support["attack"]
            repair_choice_min = 1 * support["repair"]
            hp_choice_max = 7 * support["hp"]
            attack_choice_max = 7 * support["attack"]
            repair_choice_max = 7 * support["repair"]
            
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
                
            ident = ships_data[id]["ident"]
            support5_hp_dict[ident] = level_hp_dict
            support5_attack_dict[ident] = level_attack_dict
            support5_repair_dict[ident] = level_repair_dict
            
        ship_hp_dict.update(support1_hp_dict)
        ship_hp_dict.update(support2_hp_dict)
        ship_hp_dict.update(support3_hp_dict)
        ship_hp_dict.update(support4_hp_dict)
        ship_hp_dict.update(support5_hp_dict)
        ship_attack_dict.update(support1_attack_dict)
        ship_attack_dict.update(support2_attack_dict)
        ship_attack_dict.update(support3_attack_dict)
        ship_attack_dict.update(support4_attack_dict)
        ship_attack_dict.update(support5_attack_dict)
        ship_repair_dict.update(support1_repair_dict)
        ship_repair_dict.update(support2_repair_dict)
        ship_repair_dict.update(support3_repair_dict)
        ship_repair_dict.update(support4_repair_dict)
        ship_repair_dict.update(support5_repair_dict)
        
    for i in range(26, 51): #Defense Platforms
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = defense["hp"] * 100
            max_attack = defense["attack"] * 20
            max_repair = defense["repair"] * 10
            hp_choice_min = 1 * defense["hp"]
            attack_choice_min = 1 * defense["attack"]
            repair_choice_min = 1 * defense["repair"]
            hp_choice_max = 2 * defense["hp"]
            attack_choice_max = 2 * defense["attack"]
            repair_choice_max = 2 * defense["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            defense1_hp_dict[ident] = level_hp_dict
            defense1_attack_dict[ident] = level_attack_dict
            defense1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = defense["hp"] * 150
            max_attack = defense["attack"] * 30
            max_repair = defense["repair"] * 15
            hp_choice_min = 1 * defense["hp"]
            attack_choice_min = 1 * defense["attack"]
            repair_choice_min = 1 * defense["repair"]
            hp_choice_max = 3 * defense["hp"]
            attack_choice_max = 3 * defense["attack"]
            repair_choice_max = 3 * defense["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            defense2_hp_dict[ident] = level_hp_dict
            defense2_attack_dict[ident] = level_attack_dict
            defense2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = defense["hp"] * 250
            max_attack = defense["attack"] * 50
            max_repair = defense["repair"] * 25
            hp_choice_min = 1 * defense["hp"]
            attack_choice_min = 1 * defense["attack"]
            repair_choice_min = 1 * defense["repair"]
            hp_choice_max = 4 * defense["hp"]
            attack_choice_max = 4 * defense["attack"]
            repair_choice_max = 4 * defense["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            defense3_hp_dict[ident] = level_hp_dict
            defense3_attack_dict[ident] = level_attack_dict
            defense3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = defense["hp"] * 500
            max_attack = defense["attack"] * 100
            max_repair = defense["repair"] * 50
            hp_choice_min = 1 * defense["hp"]
            attack_choice_min = 1 * defense["attack"]
            repair_choice_min = 1 * defense["repair"]
            hp_choice_max = 5 * defense["hp"]
            attack_choice_max = 5 * defense["attack"]
            repair_choice_max = 5 * defense["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            defense4_hp_dict[ident] = level_hp_dict
            defense4_attack_dict[ident] = level_attack_dict
            defense4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = defense["hp"] * 1000
            max_attack = defense["attack"] * 200
            max_repair = defense["repair"] * 100
            hp_choice_min = 1 * defense["hp"]
            attack_choice_min = 1 * defense["attack"]
            repair_choice_min = 1 * defense["repair"]
            hp_choice_max = 7 * defense["hp"]
            attack_choice_max = 7 * defense["attack"]
            repair_choice_max = 7 * defense["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            defense5_hp_dict[ident] = level_hp_dict
            defense5_attack_dict[ident] = level_attack_dict
            defense5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(defense1_hp_dict)
        ship_hp_dict.update(defense2_hp_dict)
        ship_hp_dict.update(defense3_hp_dict)
        ship_hp_dict.update(defense4_hp_dict)
        ship_hp_dict.update(defense5_hp_dict)
        ship_attack_dict.update(defense1_attack_dict)
        ship_attack_dict.update(defense2_attack_dict)
        ship_attack_dict.update(defense3_attack_dict)
        ship_attack_dict.update(defense4_attack_dict)
        ship_attack_dict.update(defense5_attack_dict)
        ship_repair_dict.update(defense1_repair_dict)
        ship_repair_dict.update(defense2_repair_dict)
        ship_repair_dict.update(defense3_repair_dict)
        ship_repair_dict.update(defense4_repair_dict)
        ship_repair_dict.update(defense5_repair_dict)
    
    for i in range(51, 76): #Cruiser
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = cruiser["hp"] * 100
            max_attack = cruiser["attack"] * 20
            max_repair = cruiser["repair"] * 10
            hp_choice_min = 1 * cruiser["hp"]
            attack_choice_min = 1 * cruiser["attack"]
            repair_choice_min = 1 * cruiser["repair"]
            hp_choice_max = 2 * cruiser["hp"]
            attack_choice_max = 2 * cruiser["attack"]
            repair_choice_max = 2 * cruiser["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            cruiser1_hp_dict[ident] = level_hp_dict
            cruiser1_attack_dict[ident] = level_attack_dict
            cruiser1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = cruiser["hp"] * 150
            max_attack = cruiser["attack"] * 30
            max_repair = cruiser["repair"] * 15
            hp_choice_min = 1 * cruiser["hp"]
            attack_choice_min = 1 * cruiser["attack"]
            repair_choice_min = 1 * cruiser["repair"]
            hp_choice_max = 3 * cruiser["hp"]
            attack_choice_max = 3 * cruiser["attack"]
            repair_choice_max = 3 * cruiser["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            cruiser2_hp_dict[ident] = level_hp_dict
            cruiser2_attack_dict[ident] = level_attack_dict
            cruiser2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = cruiser["hp"] * 250
            max_attack = cruiser["attack"] * 50
            max_repair = cruiser["repair"] * 25
            hp_choice_min = 1 * cruiser["hp"]
            attack_choice_min = 1 * cruiser["attack"]
            repair_choice_min = 1 * cruiser["repair"]
            hp_choice_max = 4 * cruiser["hp"]
            attack_choice_max = 4 * cruiser["attack"]
            repair_choice_max = 4 * cruiser["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            cruiser3_hp_dict[ident] = level_hp_dict
            cruiser3_attack_dict[ident] = level_attack_dict
            cruiser3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = cruiser["hp"] * 500
            max_attack = cruiser["attack"] * 100
            max_repair = cruiser["repair"] * 50
            hp_choice_min = 1 * cruiser["hp"]
            attack_choice_min = 1 * cruiser["attack"]
            repair_choice_min = 1 * cruiser["repair"]
            hp_choice_max = 5 * cruiser["hp"]
            attack_choice_max = 5 * cruiser["attack"]
            repair_choice_max = 5 * cruiser["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            cruiser4_hp_dict[ident] = level_hp_dict
            cruiser4_attack_dict[ident] = level_attack_dict
            cruiser4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = cruiser["hp"] * 1000
            max_attack = cruiser["attack"] * 200
            max_repair = cruiser["repair"] * 100
            hp_choice_min = 1 * cruiser["hp"]
            attack_choice_min = 1 * cruiser["attack"]
            repair_choice_min = 1 * cruiser["repair"]
            hp_choice_max = 7 * cruiser["hp"]
            attack_choice_max = 7 * cruiser["attack"]
            repair_choice_max = 7 * cruiser["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            cruiser5_hp_dict[ident] = level_hp_dict
            cruiser5_attack_dict[ident] = level_attack_dict
            cruiser5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(cruiser1_hp_dict)
        ship_hp_dict.update(cruiser2_hp_dict)
        ship_hp_dict.update(cruiser3_hp_dict)
        ship_hp_dict.update(cruiser4_hp_dict)
        ship_hp_dict.update(cruiser5_hp_dict)
        ship_attack_dict.update(cruiser1_attack_dict)
        ship_attack_dict.update(cruiser2_attack_dict)
        ship_attack_dict.update(cruiser3_attack_dict)
        ship_attack_dict.update(cruiser4_attack_dict)
        ship_attack_dict.update(cruiser5_attack_dict)
        ship_repair_dict.update(cruiser1_repair_dict)
        ship_repair_dict.update(cruiser2_repair_dict)
        ship_repair_dict.update(cruiser3_repair_dict)
        ship_repair_dict.update(cruiser4_repair_dict)
        ship_repair_dict.update(cruiser5_repair_dict)
    
    for i in range(76, 101): #Interdictors
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = interdictor["hp"] * 100
            max_attack = interdictor["attack"] * 20
            max_repair = interdictor["repair"] * 10
            hp_choice_min = 1 * interdictor["hp"]
            attack_choice_min = 1 * interdictor["attack"]
            repair_choice_min = 1 * interdictor["repair"]
            hp_choice_max = 2 * interdictor["hp"]
            attack_choice_max = 2 * interdictor["attack"]
            repair_choice_max = 2 * interdictor["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            interdictor1_hp_dict[ident] = level_hp_dict
            interdictor1_attack_dict[ident] = level_attack_dict
            interdictor1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = interdictor["hp"] * 150
            max_attack = interdictor["attack"] * 30
            max_repair = interdictor["repair"] * 15
            hp_choice_min = 1 * interdictor["hp"]
            attack_choice_min = 1 * interdictor["attack"]
            repair_choice_min = 1 * interdictor["repair"]
            hp_choice_max = 3 * interdictor["hp"]
            attack_choice_max = 3 * interdictor["attack"]
            repair_choice_max = 3 * interdictor["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            interdictor2_hp_dict[ident] = level_hp_dict
            interdictor2_attack_dict[ident] = level_attack_dict
            interdictor2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = interdictor["hp"] * 250
            max_attack = interdictor["attack"] * 50
            max_repair = interdictor["repair"] * 25
            hp_choice_min = 1 * interdictor["hp"]
            attack_choice_min = 1 * interdictor["attack"]
            repair_choice_min = 1 * interdictor["repair"]
            hp_choice_max = 4 * interdictor["hp"]
            attack_choice_max = 4 * interdictor["attack"]
            repair_choice_max = 4 * interdictor["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            interdictor3_hp_dict[ident] = level_hp_dict
            interdictor3_attack_dict[ident] = level_attack_dict
            interdictor3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = interdictor["hp"] * 500
            max_attack = interdictor["attack"] * 100
            max_repair = interdictor["repair"] * 50
            hp_choice_min = 1 * interdictor["hp"]
            attack_choice_min = 1 * interdictor["attack"]
            repair_choice_min = 1 * interdictor["repair"]
            hp_choice_max = 5 * interdictor["hp"]
            attack_choice_max = 5 * interdictor["attack"]
            repair_choice_max = 5 * interdictor["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            interdictor4_hp_dict[ident] = level_hp_dict
            interdictor4_attack_dict[ident] = level_attack_dict
            interdictor4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = interdictor["hp"] * 1000
            max_attack = interdictor["attack"] * 200
            max_repair = interdictor["repair"] * 100
            hp_choice_min = 1 * interdictor["hp"]
            attack_choice_min = 1 * interdictor["attack"]
            repair_choice_min = 1 * interdictor["repair"]
            hp_choice_max = 7 * interdictor["hp"]
            attack_choice_max = 7 * interdictor["attack"]
            repair_choice_max = 7 * interdictor["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            interdictor5_hp_dict[ident] = level_hp_dict
            interdictor5_attack_dict[ident] = level_attack_dict
            interdictor5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(interdictor1_hp_dict)
        ship_hp_dict.update(interdictor2_hp_dict)
        ship_hp_dict.update(interdictor3_hp_dict)
        ship_hp_dict.update(interdictor4_hp_dict)
        ship_hp_dict.update(interdictor5_hp_dict)
        ship_attack_dict.update(interdictor1_attack_dict)
        ship_attack_dict.update(interdictor2_attack_dict)
        ship_attack_dict.update(interdictor3_attack_dict)
        ship_attack_dict.update(interdictor4_attack_dict)
        ship_attack_dict.update(interdictor5_attack_dict)
        ship_repair_dict.update(interdictor1_repair_dict)
        ship_repair_dict.update(interdictor2_repair_dict)
        ship_repair_dict.update(interdictor3_repair_dict)
        ship_repair_dict.update(interdictor4_repair_dict)
        ship_repair_dict.update(interdictor5_repair_dict)
    
    for i in range(101, 121): #Carrier
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = carrier["hp"] * 100
            max_attack = carrier["attack"] * 20
            max_repair = carrier["repair"] * 10
            hp_choice_min = 1 * carrier["hp"]
            attack_choice_min = 1 * carrier["attack"]
            repair_choice_min = 1 * carrier["repair"]
            hp_choice_max = 2 * carrier["hp"]
            attack_choice_max = 2 * carrier["attack"]
            repair_choice_max = 2 * carrier["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            carrier1_hp_dict[ident] = level_hp_dict
            carrier1_attack_dict[ident] = level_attack_dict
            carrier1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = carrier["hp"] * 150
            max_attack = carrier["attack"] * 30
            max_repair = carrier["repair"] * 15
            hp_choice_min = 1 * carrier["hp"]
            attack_choice_min = 1 * carrier["attack"]
            repair_choice_min = 1 * carrier["repair"]
            hp_choice_max = 3 * carrier["hp"]
            attack_choice_max = 3 * carrier["attack"]
            repair_choice_max = 3 * carrier["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            carrier2_hp_dict[ident] = level_hp_dict
            carrier2_attack_dict[ident] = level_attack_dict
            carrier2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = carrier["hp"] * 250
            max_attack = carrier["attack"] * 50
            max_repair = carrier["repair"] * 25
            hp_choice_min = 1 * carrier["hp"]
            attack_choice_min = 1 * carrier["attack"]
            repair_choice_min = 1 * carrier["repair"]
            hp_choice_max = 4 * carrier["hp"]
            attack_choice_max = 4 * carrier["attack"]
            repair_choice_max = 4 * carrier["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            carrier3_hp_dict[ident] = level_hp_dict
            carrier3_attack_dict[ident] = level_attack_dict
            carrier3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = carrier["hp"] * 500
            max_attack = carrier["attack"] * 100
            max_repair = carrier["repair"] * 50
            hp_choice_min = 1 * carrier["hp"]
            attack_choice_min = 1 * carrier["attack"]
            repair_choice_min = 1 * carrier["repair"]
            hp_choice_max = 5 * carrier["hp"]
            attack_choice_max = 5 * carrier["attack"]
            repair_choice_max = 5 * carrier["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            carrier4_hp_dict[ident] = level_hp_dict
            carrier4_attack_dict[ident] = level_attack_dict
            carrier4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = carrier["hp"] * 1000
            max_attack = carrier["attack"] * 200
            max_repair = carrier["repair"] * 100
            hp_choice_min = 1 * carrier["hp"]
            attack_choice_min = 1 * carrier["attack"]
            repair_choice_min = 1 * carrier["repair"]
            hp_choice_max = 7 * carrier["hp"]
            attack_choice_max = 7 * carrier["attack"]
            repair_choice_max = 7 * carrier["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            carrier5_hp_dict[ident] = level_hp_dict
            carrier5_attack_dict[ident] = level_attack_dict
            carrier5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(carrier1_hp_dict)
        ship_hp_dict.update(carrier2_hp_dict)
        ship_hp_dict.update(carrier3_hp_dict)
        ship_hp_dict.update(carrier4_hp_dict)
        ship_hp_dict.update(carrier5_hp_dict)
        ship_attack_dict.update(carrier1_attack_dict)
        ship_attack_dict.update(carrier2_attack_dict)
        ship_attack_dict.update(carrier3_attack_dict)
        ship_attack_dict.update(carrier4_attack_dict)
        ship_attack_dict.update(carrier5_attack_dict)
        ship_repair_dict.update(carrier1_repair_dict)
        ship_repair_dict.update(carrier2_repair_dict)
        ship_repair_dict.update(carrier3_repair_dict)
        ship_repair_dict.update(carrier4_repair_dict)
        ship_repair_dict.update(carrier5_repair_dict)
    
    for i in range(121, 146): #Corvette
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = corvette["hp"] * 100
            max_attack = corvette["attack"] * 20
            max_repair = corvette["repair"] * 10
            hp_choice_min = 1 * corvette["hp"]
            attack_choice_min = 1 * corvette["attack"]
            repair_choice_min = 1 * corvette["repair"]
            hp_choice_max = 2 * corvette["hp"]
            attack_choice_max = 2 * corvette["attack"]
            repair_choice_max = 2 * corvette["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            corvette1_hp_dict[ident] = level_hp_dict
            corvette1_attack_dict[ident] = level_attack_dict
            corvette1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = corvette["hp"] * 150
            max_attack = corvette["attack"] * 30
            max_repair = corvette["repair"] * 15
            hp_choice_min = 1 * corvette["hp"]
            attack_choice_min = 1 * corvette["attack"]
            repair_choice_min = 1 * corvette["repair"]
            hp_choice_max = 3 * corvette["hp"]
            attack_choice_max = 3 * corvette["attack"]
            repair_choice_max = 3 * corvette["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            corvette2_hp_dict[ident] = level_hp_dict
            corvette2_attack_dict[ident] = level_attack_dict
            corvette2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = corvette["hp"] * 250
            max_attack = corvette["attack"] * 50
            max_repair = corvette["repair"] * 25
            hp_choice_min = 1 * corvette["hp"]
            attack_choice_min = 1 * corvette["attack"]
            repair_choice_min = 1 * corvette["repair"]
            hp_choice_max = 4 * corvette["hp"]
            attack_choice_max = 4 * corvette["attack"]
            repair_choice_max = 4 * corvette["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            corvette3_hp_dict[ident] = level_hp_dict
            corvette3_attack_dict[ident] = level_attack_dict
            corvette3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = corvette["hp"] * 500
            max_attack = corvette["attack"] * 100
            max_repair = corvette["repair"] * 50
            hp_choice_min = 1 * corvette["hp"]
            attack_choice_min = 1 * corvette["attack"]
            repair_choice_min = 1 * corvette["repair"]
            hp_choice_max = 5 * corvette["hp"]
            attack_choice_max = 5 * corvette["attack"]
            repair_choice_max = 5 * corvette["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            corvette4_hp_dict[ident] = level_hp_dict
            corvette4_attack_dict[ident] = level_attack_dict
            corvette4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = corvette["hp"] * 1000
            max_attack = corvette["attack"] * 200
            max_repair = corvette["repair"] * 100
            hp_choice_min = 1 * corvette["hp"]
            attack_choice_min = 1 * corvette["attack"]
            repair_choice_min = 1 * corvette["repair"]
            hp_choice_max = 7 * corvette["hp"]
            attack_choice_max = 7 * corvette["attack"]
            repair_choice_max = 7 * corvette["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            corvette5_hp_dict[ident] = level_hp_dict
            corvette5_attack_dict[ident] = level_attack_dict
            corvette5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(corvette1_hp_dict)
        ship_hp_dict.update(corvette2_hp_dict)
        ship_hp_dict.update(corvette3_hp_dict)
        ship_hp_dict.update(corvette4_hp_dict)
        ship_hp_dict.update(corvette5_hp_dict)
        ship_attack_dict.update(corvette1_attack_dict)
        ship_attack_dict.update(corvette2_attack_dict)
        ship_attack_dict.update(corvette3_attack_dict)
        ship_attack_dict.update(corvette4_attack_dict)
        ship_attack_dict.update(corvette5_attack_dict)
        ship_repair_dict.update(corvette1_repair_dict)
        ship_repair_dict.update(corvette2_repair_dict)
        ship_repair_dict.update(corvette3_repair_dict)
        ship_repair_dict.update(corvette4_repair_dict)
        ship_repair_dict.update(corvette5_repair_dict)
    
    for i in range(146, 171): #Bomber
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = bomber["hp"] * 100
            max_attack = bomber["attack"] * 20
            max_repair = bomber["repair"] * 10
            hp_choice_min = 1 * bomber["hp"]
            attack_choice_min = 1 * bomber["attack"]
            repair_choice_min = 1 * bomber["repair"]
            hp_choice_max = 2 * bomber["hp"]
            attack_choice_max = 2 * bomber["attack"]
            repair_choice_max = 2 * bomber["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            bomber1_hp_dict[ident] = level_hp_dict
            bomber1_attack_dict[ident] = level_attack_dict
            bomber1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = bomber["hp"] * 150
            max_attack = bomber["attack"] * 30
            max_repair = bomber["repair"] * 15
            hp_choice_min = 1 * bomber["hp"]
            attack_choice_min = 1 * bomber["attack"]
            repair_choice_min = 1 * bomber["repair"]
            hp_choice_max = 3 * bomber["hp"]
            attack_choice_max = 3 * bomber["attack"]
            repair_choice_max = 3 * bomber["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            bomber2_hp_dict[ident] = level_hp_dict
            bomber2_attack_dict[ident] = level_attack_dict
            bomber2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = bomber["hp"] * 250
            max_attack = bomber["attack"] * 50
            max_repair = bomber["repair"] * 25
            hp_choice_min = 1 * bomber["hp"]
            attack_choice_min = 1 * bomber["attack"]
            repair_choice_min = 1 * bomber["repair"]
            hp_choice_max = 4 * bomber["hp"]
            attack_choice_max = 4 * bomber["attack"]
            repair_choice_max = 4 * bomber["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            bomber3_hp_dict[ident] = level_hp_dict
            bomber3_attack_dict[ident] = level_attack_dict
            bomber3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = bomber["hp"] * 500
            max_attack = bomber["attack"] * 100
            max_repair = bomber["repair"] * 50
            hp_choice_min = 1 * bomber["hp"]
            attack_choice_min = 1 * bomber["attack"]
            repair_choice_min = 1 * bomber["repair"]
            hp_choice_max = 5 * bomber["hp"]
            attack_choice_max = 5 * bomber["attack"]
            repair_choice_max = 5 * bomber["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            bomber4_hp_dict[ident] = level_hp_dict
            bomber4_attack_dict[ident] = level_attack_dict
            bomber4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = bomber["hp"] * 1000
            max_attack = bomber["attack"] * 200
            max_repair = bomber["repair"] * 100
            hp_choice_min = 1 * bomber["hp"]
            attack_choice_min = 1 * bomber["attack"]
            repair_choice_min = 1 * bomber["repair"]
            hp_choice_max = 7 * bomber["hp"]
            attack_choice_max = 7 * bomber["attack"]
            repair_choice_max = 7 * bomber["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            bomber5_hp_dict[ident] = level_hp_dict
            bomber5_attack_dict[ident] = level_attack_dict
            bomber5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(bomber1_hp_dict)
        ship_hp_dict.update(bomber2_hp_dict)
        ship_hp_dict.update(bomber3_hp_dict)
        ship_hp_dict.update(bomber4_hp_dict)
        ship_hp_dict.update(bomber5_hp_dict)
        ship_attack_dict.update(bomber1_attack_dict)
        ship_attack_dict.update(bomber2_attack_dict)
        ship_attack_dict.update(bomber3_attack_dict)
        ship_attack_dict.update(bomber4_attack_dict)
        ship_attack_dict.update(bomber5_attack_dict)
        ship_repair_dict.update(bomber1_repair_dict)
        ship_repair_dict.update(bomber2_repair_dict)
        ship_repair_dict.update(bomber3_repair_dict)
        ship_repair_dict.update(bomber4_repair_dict)
        ship_repair_dict.update(bomber5_repair_dict)
    
    for i in range(171, 196): #Fighter
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = fighter["hp"] * 100
            max_attack = fighter["attack"] * 20
            max_repair = fighter["repair"] * 10
            hp_choice_min = 1 * fighter["hp"]
            attack_choice_min = 1 * fighter["attack"]
            repair_choice_min = 1 * fighter["repair"]
            hp_choice_max = 2 * fighter["hp"]
            attack_choice_max = 2 * fighter["attack"]
            repair_choice_max = 2 * fighter["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            fighter1_hp_dict[ident] = level_hp_dict
            fighter1_attack_dict[ident] = level_attack_dict
            fighter1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = fighter["hp"] * 150
            max_attack = fighter["attack"] * 30
            max_repair = fighter["repair"] * 15
            hp_choice_min = 1 * fighter["hp"]
            attack_choice_min = 1 * fighter["attack"]
            repair_choice_min = 1 * fighter["repair"]
            hp_choice_max = 3 * fighter["hp"]
            attack_choice_max = 3 * fighter["attack"]
            repair_choice_max = 3 * fighter["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            fighter2_hp_dict[ident] = level_hp_dict
            fighter2_attack_dict[ident] = level_attack_dict
            fighter2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = fighter["hp"] * 250
            max_attack = fighter["attack"] * 50
            max_repair = fighter["repair"] * 25
            hp_choice_min = 1 * fighter["hp"]
            attack_choice_min = 1 * fighter["attack"]
            repair_choice_min = 1 * fighter["repair"]
            hp_choice_max = 5 * fighter["hp"]
            attack_choice_max = 5 * fighter["attack"]
            repair_choice_max = 5 * fighter["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            fighter3_hp_dict[ident] = level_hp_dict
            fighter3_attack_dict[ident] = level_attack_dict
            fighter3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = fighter["hp"] * 500
            max_attack = fighter["attack"] * 100
            max_repair = fighter["repair"] * 50
            hp_choice_min = 1 * fighter["hp"]
            attack_choice_min = 1 * fighter["attack"]
            repair_choice_min = 1 * fighter["repair"]
            hp_choice_max = 5 * fighter["hp"]
            attack_choice_max = 5 * fighter["attack"]
            repair_choice_max = 5 * fighter["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            fighter4_hp_dict[ident] = level_hp_dict
            fighter4_attack_dict[ident] = level_attack_dict
            fighter4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = fighter["hp"] * 1000
            max_attack = fighter["attack"] * 200
            max_repair = fighter["repair"] * 100
            hp_choice_min = 1 * fighter["hp"]
            attack_choice_min = 1 * fighter["attack"]
            repair_choice_min = 1 * fighter["repair"]
            hp_choice_max = 7 * fighter["hp"]
            attack_choice_max = 7 * fighter["attack"]
            repair_choice_max = 7 * fighter["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            fighter5_hp_dict[ident] = level_hp_dict
            fighter5_attack_dict[ident] = level_attack_dict
            fighter5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(fighter1_hp_dict)
        ship_hp_dict.update(fighter2_hp_dict)
        ship_hp_dict.update(fighter3_hp_dict)
        ship_hp_dict.update(fighter4_hp_dict)
        ship_hp_dict.update(fighter5_hp_dict)
        ship_attack_dict.update(fighter1_attack_dict)
        ship_attack_dict.update(fighter2_attack_dict)
        ship_attack_dict.update(fighter3_attack_dict)
        ship_attack_dict.update(fighter4_attack_dict)
        ship_attack_dict.update(fighter5_attack_dict)
        ship_repair_dict.update(fighter1_repair_dict)
        ship_repair_dict.update(fighter2_repair_dict)
        ship_repair_dict.update(fighter3_repair_dict)
        ship_repair_dict.update(fighter4_repair_dict)
        ship_repair_dict.update(fighter5_repair_dict)
    
    for i in range(196, 211): #Dreadnaught
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = dreadnaught["hp"] * 100
            max_attack = dreadnaught["attack"] * 20
            max_repair = dreadnaught["repair"] * 10
            hp_choice_min = 1 * dreadnaught["hp"]
            attack_choice_min = 1 * dreadnaught["attack"]
            repair_choice_min = 1 * dreadnaught["repair"]
            hp_choice_max = 2 * dreadnaught["hp"]
            attack_choice_max = 2 * dreadnaught["attack"]
            repair_choice_max = 2 * dreadnaught["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            dreadnaught1_hp_dict[ident] = level_hp_dict
            dreadnaught1_attack_dict[ident] = level_attack_dict
            dreadnaught1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = dreadnaught["hp"] * 150
            max_attack = dreadnaught["attack"] * 30
            max_repair = dreadnaught["repair"] * 15
            hp_choice_min = 1 * dreadnaught["hp"]
            attack_choice_min = 1 * dreadnaught["attack"]
            repair_choice_min = 1 * dreadnaught["repair"]
            hp_choice_max = 3 * dreadnaught["hp"]
            attack_choice_max = 3 * dreadnaught["attack"]
            repair_choice_max = 3 * dreadnaught["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            dreadnaught2_hp_dict[ident] = level_hp_dict
            dreadnaught2_attack_dict[ident] = level_attack_dict
            dreadnaught2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = dreadnaught["hp"] * 250
            max_attack = dreadnaught["attack"] * 50
            max_repair = dreadnaught["repair"] * 25
            hp_choice_min = 1 * dreadnaught["hp"]
            attack_choice_min = 1 * dreadnaught["attack"]
            repair_choice_min = 1 * dreadnaught["repair"]
            hp_choice_max = 5 * dreadnaught["hp"]
            attack_choice_max = 5 * dreadnaught["attack"]
            repair_choice_max = 5 * dreadnaught["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            dreadnaught3_hp_dict[ident] = level_hp_dict
            dreadnaught3_attack_dict[ident] = level_attack_dict
            dreadnaught3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = dreadnaught["hp"] * 500
            max_attack = dreadnaught["attack"] * 100
            max_repair = dreadnaught["repair"] * 50
            hp_choice_min = 1 * dreadnaught["hp"]
            attack_choice_min = 1 * dreadnaught["attack"]
            repair_choice_min = 1 * dreadnaught["repair"]
            hp_choice_max = 5 * dreadnaught["hp"]
            attack_choice_max = 5 * dreadnaught["attack"]
            repair_choice_max = 5 * dreadnaught["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            dreadnaught4_hp_dict[ident] = level_hp_dict
            dreadnaught4_attack_dict[ident] = level_attack_dict
            dreadnaught4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = dreadnaught["hp"] * 1000
            max_attack = dreadnaught["attack"] * 200
            max_repair = dreadnaught["repair"] * 100
            hp_choice_min = 1 * dreadnaught["hp"]
            attack_choice_min = 1 * dreadnaught["attack"]
            repair_choice_min = 1 * dreadnaught["repair"]
            hp_choice_max = 7 * dreadnaught["hp"]
            attack_choice_max = 7 * dreadnaught["attack"]
            repair_choice_max = 7 * dreadnaught["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            dreadnaught5_hp_dict[ident] = level_hp_dict
            dreadnaught5_attack_dict[ident] = level_attack_dict
            dreadnaught5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(dreadnaught1_hp_dict)
        ship_hp_dict.update(dreadnaught2_hp_dict)
        ship_hp_dict.update(dreadnaught3_hp_dict)
        ship_hp_dict.update(dreadnaught4_hp_dict)
        ship_hp_dict.update(dreadnaught5_hp_dict)
        ship_attack_dict.update(dreadnaught1_attack_dict)
        ship_attack_dict.update(dreadnaught2_attack_dict)
        ship_attack_dict.update(dreadnaught3_attack_dict)
        ship_attack_dict.update(dreadnaught4_attack_dict)
        ship_attack_dict.update(dreadnaught5_attack_dict)
        ship_repair_dict.update(dreadnaught1_repair_dict)
        ship_repair_dict.update(dreadnaught2_repair_dict)
        ship_repair_dict.update(dreadnaught3_repair_dict)
        ship_repair_dict.update(dreadnaught4_repair_dict)
        ship_repair_dict.update(dreadnaught5_repair_dict)
    
    for i in range(211, 221): #Leviathan
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = leviathan["hp"] * 100
            max_attack = leviathan["attack"] * 20
            max_repair = leviathan["repair"] * 10
            hp_choice_min = 1 * leviathan["hp"]
            attack_choice_min = 1 * leviathan["attack"]
            repair_choice_min = 1 * leviathan["repair"]
            hp_choice_max = 2 * leviathan["hp"]
            attack_choice_max = 2 * leviathan["attack"]
            repair_choice_max = 2 * leviathan["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            leviathan1_hp_dict[ident] = level_hp_dict
            leviathan1_attack_dict[ident] = level_attack_dict
            leviathan1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = leviathan["hp"] * 150
            max_attack = leviathan["attack"] * 30
            max_repair = leviathan["repair"] * 15
            hp_choice_min = 1 * leviathan["hp"]
            attack_choice_min = 1 * leviathan["attack"]
            repair_choice_min = 1 * leviathan["repair"]
            hp_choice_max = 3 * leviathan["hp"]
            attack_choice_max = 3 * leviathan["attack"]
            repair_choice_max = 3 * leviathan["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            leviathan2_hp_dict[ident] = level_hp_dict
            leviathan2_attack_dict[ident] = level_attack_dict
            leviathan2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = leviathan["hp"] * 250
            max_attack = leviathan["attack"] * 50
            max_repair = leviathan["repair"] * 25
            hp_choice_min = 1 * leviathan["hp"]
            attack_choice_min = 1 * leviathan["attack"]
            repair_choice_min = 1 * leviathan["repair"]
            hp_choice_max = 5 * leviathan["hp"]
            attack_choice_max = 5 * leviathan["attack"]
            repair_choice_max = 5 * leviathan["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            leviathan3_hp_dict[ident] = level_hp_dict
            leviathan3_attack_dict[ident] = level_attack_dict
            leviathan3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = leviathan["hp"] * 500
            max_attack = leviathan["attack"] * 100
            max_repair = leviathan["repair"] * 50
            hp_choice_min = 1 * leviathan["hp"]
            attack_choice_min = 1 * leviathan["attack"]
            repair_choice_min = 1 * leviathan["repair"]
            hp_choice_max = 5 * leviathan["hp"]
            attack_choice_max = 5 * leviathan["attack"]
            repair_choice_max = 5 * leviathan["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            leviathan4_hp_dict[ident] = level_hp_dict
            leviathan4_attack_dict[ident] = level_attack_dict
            leviathan4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = leviathan["hp"] * 1000
            max_attack = leviathan["attack"] * 200
            max_repair = leviathan["repair"] * 100
            hp_choice_min = 1 * leviathan["hp"]
            attack_choice_min = 1 * leviathan["attack"]
            repair_choice_min = 1 * leviathan["repair"]
            hp_choice_max = 7 * leviathan["hp"]
            attack_choice_max = 7 * leviathan["attack"]
            repair_choice_max = 7 * leviathan["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            leviathan5_hp_dict[ident] = level_hp_dict
            leviathan5_attack_dict[ident] = level_attack_dict
            leviathan5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(leviathan1_hp_dict)
        ship_hp_dict.update(leviathan2_hp_dict)
        ship_hp_dict.update(leviathan3_hp_dict)
        ship_hp_dict.update(leviathan4_hp_dict)
        ship_hp_dict.update(leviathan5_hp_dict)
        ship_attack_dict.update(leviathan1_attack_dict)
        ship_attack_dict.update(leviathan2_attack_dict)
        ship_attack_dict.update(leviathan3_attack_dict)
        ship_attack_dict.update(leviathan4_attack_dict)
        ship_attack_dict.update(leviathan5_attack_dict)
        ship_repair_dict.update(leviathan1_repair_dict)
        ship_repair_dict.update(leviathan2_repair_dict)
        ship_repair_dict.update(leviathan3_repair_dict)
        ship_repair_dict.update(leviathan4_repair_dict)
        ship_repair_dict.update(leviathan5_repair_dict)
    
    for i in range(221, 231): #Super Destroyer
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = super_destroyer["hp"] * 100
            max_attack = super_destroyer["attack"] * 20
            max_repair = super_destroyer["repair"] * 10
            hp_choice_min = 1 * super_destroyer["hp"]
            attack_choice_min = 1 * super_destroyer["attack"]
            repair_choice_min = 1 * super_destroyer["repair"]
            hp_choice_max = 2 * super_destroyer["hp"]
            attack_choice_max = 2 * super_destroyer["attack"]
            repair_choice_max = 2 * super_destroyer["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            super_destroyer1_hp_dict[ident] = level_hp_dict
            super_destroyer1_attack_dict[ident] = level_attack_dict
            super_destroyer1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = super_destroyer["hp"] * 150
            max_attack = super_destroyer["attack"] * 30
            max_repair = super_destroyer["repair"] * 15
            hp_choice_min = 1 * super_destroyer["hp"]
            attack_choice_min = 1 * super_destroyer["attack"]
            repair_choice_min = 1 * super_destroyer["repair"]
            hp_choice_max = 3 * super_destroyer["hp"]
            attack_choice_max = 3 * super_destroyer["attack"]
            repair_choice_max = 3 * super_destroyer["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            super_destroyer2_hp_dict[ident] = level_hp_dict
            super_destroyer2_attack_dict[ident] = level_attack_dict
            super_destroyer2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = super_destroyer["hp"] * 250
            max_attack = super_destroyer["attack"] * 50
            max_repair = super_destroyer["repair"] * 25
            hp_choice_min = 1 * super_destroyer["hp"]
            attack_choice_min = 1 * super_destroyer["attack"]
            repair_choice_min = 1 * super_destroyer["repair"]
            hp_choice_max = 5 * super_destroyer["hp"]
            attack_choice_max = 5 * super_destroyer["attack"]
            repair_choice_max = 5 * super_destroyer["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            super_destroyer3_hp_dict[ident] = level_hp_dict
            super_destroyer3_attack_dict[ident] = level_attack_dict
            super_destroyer3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = super_destroyer["hp"] * 500
            max_attack = super_destroyer["attack"] * 100
            max_repair = super_destroyer["repair"] * 50
            hp_choice_min = 1 * super_destroyer["hp"]
            attack_choice_min = 1 * super_destroyer["attack"]
            repair_choice_min = 1 * super_destroyer["repair"]
            hp_choice_max = 5 * super_destroyer["hp"]
            attack_choice_max = 5 * super_destroyer["attack"]
            repair_choice_max = 5 * super_destroyer["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            super_destroyer4_hp_dict[ident] = level_hp_dict
            super_destroyer4_attack_dict[ident] = level_attack_dict
            super_destroyer4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = super_destroyer["hp"] * 1000
            max_attack = super_destroyer["attack"] * 200
            max_repair = super_destroyer["repair"] * 100
            hp_choice_min = 1 * super_destroyer["hp"]
            attack_choice_min = 1 * super_destroyer["attack"]
            repair_choice_min = 1 * super_destroyer["repair"]
            hp_choice_max = 7 * super_destroyer["hp"]
            attack_choice_max = 7 * super_destroyer["attack"]
            repair_choice_max = 7 * super_destroyer["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            super_destroyer5_hp_dict[ident] = level_hp_dict
            super_destroyer5_attack_dict[ident] = level_attack_dict
            super_destroyer5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(super_destroyer1_hp_dict)
        ship_hp_dict.update(super_destroyer2_hp_dict)
        ship_hp_dict.update(super_destroyer3_hp_dict)
        ship_hp_dict.update(super_destroyer4_hp_dict)
        ship_hp_dict.update(super_destroyer5_hp_dict)
        ship_attack_dict.update(super_destroyer1_attack_dict)
        ship_attack_dict.update(super_destroyer2_attack_dict)
        ship_attack_dict.update(super_destroyer3_attack_dict)
        ship_attack_dict.update(super_destroyer4_attack_dict)
        ship_attack_dict.update(super_destroyer5_attack_dict)
        ship_repair_dict.update(super_destroyer1_repair_dict)
        ship_repair_dict.update(super_destroyer2_repair_dict)
        ship_repair_dict.update(super_destroyer3_repair_dict)
        ship_repair_dict.update(super_destroyer4_repair_dict)
        ship_repair_dict.update(super_destroyer5_repair_dict)
    
    for i in range(231, 236): #Star Station
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = star_station["hp"] * 100
            max_attack = star_station["attack"] * 20
            max_repair = star_station["repair"] * 10
            hp_choice_min = 1 * star_station["hp"]
            attack_choice_min = 1 * star_station["attack"]
            repair_choice_min = 1 * star_station["repair"]
            hp_choice_max = 2 * star_station["hp"]
            attack_choice_max = 2 * star_station["attack"]
            repair_choice_max = 2 * star_station["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            star_station1_hp_dict[ident] = level_hp_dict
            star_station1_attack_dict[ident] = level_attack_dict
            star_station1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = star_station["hp"] * 150
            max_attack = star_station["attack"] * 30
            max_repair = star_station["repair"] * 15
            hp_choice_min = 1 * star_station["hp"]
            attack_choice_min = 1 * star_station["attack"]
            repair_choice_min = 1 * star_station["repair"]
            hp_choice_max = 3 * star_station["hp"]
            attack_choice_max = 3 * star_station["attack"]
            repair_choice_max = 3 * star_station["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            star_station2_hp_dict[ident] = level_hp_dict
            star_station2_attack_dict[ident] = level_attack_dict
            star_station2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = star_station["hp"] * 250
            max_attack = star_station["attack"] * 50
            max_repair = star_station["repair"] * 25
            hp_choice_min = 1 * star_station["hp"]
            attack_choice_min = 1 * star_station["attack"]
            repair_choice_min = 1 * star_station["repair"]
            hp_choice_max = 5 * star_station["hp"]
            attack_choice_max = 5 * star_station["attack"]
            repair_choice_max = 5 * star_station["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            star_station3_hp_dict[ident] = level_hp_dict
            star_station3_attack_dict[ident] = level_attack_dict
            star_station3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = star_station["hp"] * 500
            max_attack = star_station["attack"] * 100
            max_repair = star_station["repair"] * 50
            hp_choice_min = 1 * star_station["hp"]
            attack_choice_min = 1 * star_station["attack"]
            repair_choice_min = 1 * star_station["repair"]
            hp_choice_max = 5 * star_station["hp"]
            attack_choice_max = 5 * star_station["attack"]
            repair_choice_max = 5 * star_station["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            star_station4_hp_dict[ident] = level_hp_dict
            star_station4_attack_dict[ident] = level_attack_dict
            star_station4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = star_station["hp"] * 1000
            max_attack = star_station["attack"] * 200
            max_repair = star_station["repair"] * 100
            hp_choice_min = 1 * star_station["hp"]
            attack_choice_min = 1 * star_station["attack"]
            repair_choice_min = 1 * star_station["repair"]
            hp_choice_max = 7 * star_station["hp"]
            attack_choice_max = 7 * star_station["attack"]
            repair_choice_max = 7 * star_station["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            star_station5_hp_dict[ident] = level_hp_dict
            star_station5_attack_dict[ident] = level_attack_dict
            star_station5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(star_station1_hp_dict)
        ship_hp_dict.update(star_station2_hp_dict)
        ship_hp_dict.update(star_station3_hp_dict)
        ship_hp_dict.update(star_station4_hp_dict)
        ship_hp_dict.update(star_station5_hp_dict)
        ship_attack_dict.update(star_station1_attack_dict)
        ship_attack_dict.update(star_station2_attack_dict)
        ship_attack_dict.update(star_station3_attack_dict)
        ship_attack_dict.update(star_station4_attack_dict)
        ship_attack_dict.update(star_station5_attack_dict)
        ship_repair_dict.update(star_station1_repair_dict)
        ship_repair_dict.update(star_station2_repair_dict)
        ship_repair_dict.update(star_station3_repair_dict)
        ship_repair_dict.update(star_station4_repair_dict)
        ship_repair_dict.update(star_station5_repair_dict)
    
    for i in range(236, 261): #Harvesters
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = harvester["hp"] * 100
            max_attack = harvester["attack"] * 20
            max_repair = harvester["repair"] * 10
            hp_choice_min = 1 * harvester["hp"]
            attack_choice_min = 1 * harvester["attack"]
            repair_choice_min = 1 * harvester["repair"]
            hp_choice_max = 2 * harvester["hp"]
            attack_choice_max = 2 * harvester["attack"]
            repair_choice_max = 2 * harvester["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            harvester1_hp_dict[ident] = level_hp_dict
            harvester1_attack_dict[ident] = level_attack_dict
            harvester1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = harvester["hp"] * 150
            max_attack = harvester["attack"] * 30
            max_repair = harvester["repair"] * 15
            hp_choice_min = 1 * harvester["hp"]
            attack_choice_min = 1 * harvester["attack"]
            repair_choice_min = 1 * harvester["repair"]
            hp_choice_max = 3 * harvester["hp"]
            attack_choice_max = 3 * harvester["attack"]
            repair_choice_max = 3 * harvester["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            harvester2_hp_dict[ident] = level_hp_dict
            harvester2_attack_dict[ident] = level_attack_dict
            harvester2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = harvester["hp"] * 250
            max_attack = harvester["attack"] * 50
            max_repair = harvester["repair"] * 25
            hp_choice_min = 1 * harvester["hp"]
            attack_choice_min = 1 * harvester["attack"]
            repair_choice_min = 1 * harvester["repair"]
            hp_choice_max = 5 * harvester["hp"]
            attack_choice_max = 5 * harvester["attack"]
            repair_choice_max = 5 * harvester["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            harvester3_hp_dict[ident] = level_hp_dict
            harvester3_attack_dict[ident] = level_attack_dict
            harvester3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = harvester["hp"] * 500
            max_attack = harvester["attack"] * 100
            max_repair = harvester["repair"] * 50
            hp_choice_min = 1 * harvester["hp"]
            attack_choice_min = 1 * harvester["attack"]
            repair_choice_min = 1 * harvester["repair"]
            hp_choice_max = 5 * harvester["hp"]
            attack_choice_max = 5 * harvester["attack"]
            repair_choice_max = 5 * harvester["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            harvester4_hp_dict[ident] = level_hp_dict
            harvester4_attack_dict[ident] = level_attack_dict
            harvester4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = harvester["hp"] * 1000
            max_attack = harvester["attack"] * 200
            max_repair = harvester["repair"] * 100
            hp_choice_min = 1 * harvester["hp"]
            attack_choice_min = 1 * harvester["attack"]
            repair_choice_min = 1 * harvester["repair"]
            hp_choice_max = 7 * harvester["hp"]
            attack_choice_max = 7 * harvester["attack"]
            repair_choice_max = 7 * harvester["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            harvester5_hp_dict[ident] = level_hp_dict
            harvester5_attack_dict[ident] = level_attack_dict
            harvester5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(harvester1_hp_dict)
        ship_hp_dict.update(harvester2_hp_dict)
        ship_hp_dict.update(harvester3_hp_dict)
        ship_hp_dict.update(harvester4_hp_dict)
        ship_hp_dict.update(harvester5_hp_dict)
        ship_attack_dict.update(harvester1_attack_dict)
        ship_attack_dict.update(harvester2_attack_dict)
        ship_attack_dict.update(harvester3_attack_dict)
        ship_attack_dict.update(harvester4_attack_dict)
        ship_attack_dict.update(harvester5_attack_dict)
        ship_repair_dict.update(harvester1_repair_dict)
        ship_repair_dict.update(harvester2_repair_dict)
        ship_repair_dict.update(harvester3_repair_dict)
        ship_repair_dict.update(harvester4_repair_dict)
        ship_repair_dict.update(harvester5_repair_dict)
    
    for i in range(261, 286): #Mine Layers
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = mine_layer["hp"] * 100
            max_attack = mine_layer["attack"] * 20
            max_repair = mine_layer["repair"] * 10
            hp_choice_min = 1 * mine_layer["hp"]
            attack_choice_min = 1 * mine_layer["attack"]
            repair_choice_min = 1 * mine_layer["repair"]
            hp_choice_max = 2 * mine_layer["hp"]
            attack_choice_max = 2 * mine_layer["attack"]
            repair_choice_max = 2 * mine_layer["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mine_layer1_hp_dict[ident] = level_hp_dict
            mine_layer1_attack_dict[ident] = level_attack_dict
            mine_layer1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = mine_layer["hp"] * 150
            max_attack = mine_layer["attack"] * 30
            max_repair = mine_layer["repair"] * 15
            hp_choice_min = 1 * mine_layer["hp"]
            attack_choice_min = 1 * mine_layer["attack"]
            repair_choice_min = 1 * mine_layer["repair"]
            hp_choice_max = 3 * mine_layer["hp"]
            attack_choice_max = 3 * mine_layer["attack"]
            repair_choice_max = 3 * mine_layer["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mine_layer2_hp_dict[ident] = level_hp_dict
            mine_layer2_attack_dict[ident] = level_attack_dict
            mine_layer2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = mine_layer["hp"] * 250
            max_attack = mine_layer["attack"] * 50
            max_repair = mine_layer["repair"] * 25
            hp_choice_min = 1 * mine_layer["hp"]
            attack_choice_min = 1 * mine_layer["attack"]
            repair_choice_min = 1 * mine_layer["repair"]
            hp_choice_max = 5 * mine_layer["hp"]
            attack_choice_max = 5 * mine_layer["attack"]
            repair_choice_max = 5 * mine_layer["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mine_layer3_hp_dict[ident] = level_hp_dict
            mine_layer3_attack_dict[ident] = level_attack_dict
            mine_layer3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = mine_layer["hp"] * 500
            max_attack = mine_layer["attack"] * 100
            max_repair = mine_layer["repair"] * 50
            hp_choice_min = 1 * mine_layer["hp"]
            attack_choice_min = 1 * mine_layer["attack"]
            repair_choice_min = 1 * mine_layer["repair"]
            hp_choice_max = 5 * mine_layer["hp"]
            attack_choice_max = 5 * mine_layer["attack"]
            repair_choice_max = 5 * mine_layer["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mine_layer4_hp_dict[ident] = level_hp_dict
            mine_layer4_attack_dict[ident] = level_attack_dict
            mine_layer4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = mine_layer["hp"] * 1000
            max_attack = mine_layer["attack"] * 200
            max_repair = mine_layer["repair"] * 100
            hp_choice_min = 1 * mine_layer["hp"]
            attack_choice_min = 1 * mine_layer["attack"]
            repair_choice_min = 1 * mine_layer["repair"]
            hp_choice_max = 7 * mine_layer["hp"]
            attack_choice_max = 7 * mine_layer["attack"]
            repair_choice_max = 7 * mine_layer["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mine_layer5_hp_dict[ident] = level_hp_dict
            mine_layer5_attack_dict[ident] = level_attack_dict
            mine_layer5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(mine_layer1_hp_dict)
        ship_hp_dict.update(mine_layer2_hp_dict)
        ship_hp_dict.update(mine_layer3_hp_dict)
        ship_hp_dict.update(mine_layer4_hp_dict)
        ship_hp_dict.update(mine_layer5_hp_dict)
        ship_attack_dict.update(mine_layer1_attack_dict)
        ship_attack_dict.update(mine_layer2_attack_dict)
        ship_attack_dict.update(mine_layer3_attack_dict)
        ship_attack_dict.update(mine_layer4_attack_dict)
        ship_attack_dict.update(mine_layer5_attack_dict)
        ship_repair_dict.update(mine_layer1_repair_dict)
        ship_repair_dict.update(mine_layer2_repair_dict)
        ship_repair_dict.update(mine_layer3_repair_dict)
        ship_repair_dict.update(mine_layer4_repair_dict)
        ship_repair_dict.update(mine_layer5_repair_dict)
    
    for i in range(286, 311): #Targetting Ships
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = targetting["hp"] * 100
            max_attack = targetting["attack"] * 20
            max_repair = targetting["repair"] * 10
            hp_choice_min = 1 * targetting["hp"]
            attack_choice_min = 1 * targetting["attack"]
            repair_choice_min = 1 * targetting["repair"]
            hp_choice_max = 2 * targetting["hp"]
            attack_choice_max = 2 * targetting["attack"]
            repair_choice_max = 2 * targetting["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            targetting1_hp_dict[ident] = level_hp_dict
            targetting1_attack_dict[ident] = level_attack_dict
            targetting1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = targetting["hp"] * 150
            max_attack = targetting["attack"] * 30
            max_repair = targetting["repair"] * 15
            hp_choice_min = 1 * targetting["hp"]
            attack_choice_min = 1 * targetting["attack"]
            repair_choice_min = 1 * targetting["repair"]
            hp_choice_max = 3 * targetting["hp"]
            attack_choice_max = 3 * targetting["attack"]
            repair_choice_max = 3 * targetting["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            targetting2_hp_dict[ident] = level_hp_dict
            targetting2_attack_dict[ident] = level_attack_dict
            targetting2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = targetting["hp"] * 250
            max_attack = targetting["attack"] * 50
            max_repair = targetting["repair"] * 25
            hp_choice_min = 1 * targetting["hp"]
            attack_choice_min = 1 * targetting["attack"]
            repair_choice_min = 1 * targetting["repair"]
            hp_choice_max = 5 * targetting["hp"]
            attack_choice_max = 5 * targetting["attack"]
            repair_choice_max = 5 * targetting["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            targetting3_hp_dict[ident] = level_hp_dict
            targetting3_attack_dict[ident] = level_attack_dict
            targetting3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = targetting["hp"] * 500
            max_attack = targetting["attack"] * 100
            max_repair = targetting["repair"] * 50
            hp_choice_min = 1 * targetting["hp"]
            attack_choice_min = 1 * targetting["attack"]
            repair_choice_min = 1 * targetting["repair"]
            hp_choice_max = 5 * targetting["hp"]
            attack_choice_max = 5 * targetting["attack"]
            repair_choice_max = 5 * targetting["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            targetting4_hp_dict[ident] = level_hp_dict
            targetting4_attack_dict[ident] = level_attack_dict
            targetting4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = targetting["hp"] * 1000
            max_attack = targetting["attack"] * 200
            max_repair = targetting["repair"] * 100
            hp_choice_min = 1 * targetting["hp"]
            attack_choice_min = 1 * targetting["attack"]
            repair_choice_min = 1 * targetting["repair"]
            hp_choice_max = 7 * targetting["hp"]
            attack_choice_max = 7 * targetting["attack"]
            repair_choice_max = 7 * targetting["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            targetting5_hp_dict[ident] = level_hp_dict
            targetting5_attack_dict[ident] = level_attack_dict
            targetting5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(targetting1_hp_dict)
        ship_hp_dict.update(targetting2_hp_dict)
        ship_hp_dict.update(targetting3_hp_dict)
        ship_hp_dict.update(targetting4_hp_dict)
        ship_hp_dict.update(targetting5_hp_dict)
        ship_attack_dict.update(targetting1_attack_dict)
        ship_attack_dict.update(targetting2_attack_dict)
        ship_attack_dict.update(targetting3_attack_dict)
        ship_attack_dict.update(targetting4_attack_dict)
        ship_attack_dict.update(targetting5_attack_dict)
        ship_repair_dict.update(targetting1_repair_dict)
        ship_repair_dict.update(targetting2_repair_dict)
        ship_repair_dict.update(targetting3_repair_dict)
        ship_repair_dict.update(targetting4_repair_dict)
        ship_repair_dict.update(targetting5_repair_dict)
    
    for i in range(311, 336): #Mobile Fleet Depot
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = mobile_fleet_depot["hp"] * 100
            max_attack = mobile_fleet_depot["attack"] * 20
            max_repair = mobile_fleet_depot["repair"] * 10
            hp_choice_min = 1 * mobile_fleet_depot["hp"]
            attack_choice_min = 1 * mobile_fleet_depot["attack"]
            repair_choice_min = 1 * mobile_fleet_depot["repair"]
            hp_choice_max = 2 * mobile_fleet_depot["hp"]
            attack_choice_max = 2 * mobile_fleet_depot["attack"]
            repair_choice_max = 2 * mobile_fleet_depot["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mobile_fleet_depot1_hp_dict[ident] = level_hp_dict
            mobile_fleet_depot1_attack_dict[ident] = level_attack_dict
            mobile_fleet_depot1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = mobile_fleet_depot["hp"] * 150
            max_attack = mobile_fleet_depot["attack"] * 30
            max_repair = mobile_fleet_depot["repair"] * 15
            hp_choice_min = 1 * mobile_fleet_depot["hp"]
            attack_choice_min = 1 * mobile_fleet_depot["attack"]
            repair_choice_min = 1 * mobile_fleet_depot["repair"]
            hp_choice_max = 3 * mobile_fleet_depot["hp"]
            attack_choice_max = 3 * mobile_fleet_depot["attack"]
            repair_choice_max = 3 * mobile_fleet_depot["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mobile_fleet_depot2_hp_dict[ident] = level_hp_dict
            mobile_fleet_depot2_attack_dict[ident] = level_attack_dict
            mobile_fleet_depot2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = mobile_fleet_depot["hp"] * 250
            max_attack = mobile_fleet_depot["attack"] * 50
            max_repair = mobile_fleet_depot["repair"] * 25
            hp_choice_min = 1 * mobile_fleet_depot["hp"]
            attack_choice_min = 1 * mobile_fleet_depot["attack"]
            repair_choice_min = 1 * mobile_fleet_depot["repair"]
            hp_choice_max = 5 * mobile_fleet_depot["hp"]
            attack_choice_max = 5 * mobile_fleet_depot["attack"]
            repair_choice_max = 5 * mobile_fleet_depot["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mobile_fleet_depot3_hp_dict[ident] = level_hp_dict
            mobile_fleet_depot3_attack_dict[ident] = level_attack_dict
            mobile_fleet_depot3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = mobile_fleet_depot["hp"] * 500
            max_attack = mobile_fleet_depot["attack"] * 100
            max_repair = mobile_fleet_depot["repair"] * 50
            hp_choice_min = 1 * mobile_fleet_depot["hp"]
            attack_choice_min = 1 * mobile_fleet_depot["attack"]
            repair_choice_min = 1 * mobile_fleet_depot["repair"]
            hp_choice_max = 5 * mobile_fleet_depot["hp"]
            attack_choice_max = 5 * mobile_fleet_depot["attack"]
            repair_choice_max = 5 * mobile_fleet_depot["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mobile_fleet_depot4_hp_dict[ident] = level_hp_dict
            mobile_fleet_depot4_attack_dict[ident] = level_attack_dict
            mobile_fleet_depot4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = mobile_fleet_depot["hp"] * 1000
            max_attack = mobile_fleet_depot["attack"] * 200
            max_repair = mobile_fleet_depot["repair"] * 100
            hp_choice_min = 1 * mobile_fleet_depot["hp"]
            attack_choice_min = 1 * mobile_fleet_depot["attack"]
            repair_choice_min = 1 * mobile_fleet_depot["repair"]
            hp_choice_max = 7 * mobile_fleet_depot["hp"]
            attack_choice_max = 7 * mobile_fleet_depot["attack"]
            repair_choice_max = 7 * mobile_fleet_depot["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            mobile_fleet_depot5_hp_dict[ident] = level_hp_dict
            mobile_fleet_depot5_attack_dict[ident] = level_attack_dict
            mobile_fleet_depot5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(mobile_fleet_depot1_hp_dict)
        ship_hp_dict.update(mobile_fleet_depot2_hp_dict)
        ship_hp_dict.update(mobile_fleet_depot3_hp_dict)
        ship_hp_dict.update(mobile_fleet_depot4_hp_dict)
        ship_hp_dict.update(mobile_fleet_depot5_hp_dict)
        ship_attack_dict.update(mobile_fleet_depot1_attack_dict)
        ship_attack_dict.update(mobile_fleet_depot2_attack_dict)
        ship_attack_dict.update(mobile_fleet_depot3_attack_dict)
        ship_attack_dict.update(mobile_fleet_depot4_attack_dict)
        ship_attack_dict.update(mobile_fleet_depot5_attack_dict)
        ship_repair_dict.update(mobile_fleet_depot1_repair_dict)
        ship_repair_dict.update(mobile_fleet_depot2_repair_dict)
        ship_repair_dict.update(mobile_fleet_depot3_repair_dict)
        ship_repair_dict.update(mobile_fleet_depot4_repair_dict)
        ship_repair_dict.update(mobile_fleet_depot5_repair_dict)
    
    for i in range(336, 361): #Destroyers
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = destroyer["hp"] * 100
            max_attack = destroyer["attack"] * 20
            max_repair = destroyer["repair"] * 10
            hp_choice_min = 1 * destroyer["hp"]
            attack_choice_min = 1 * destroyer["attack"]
            repair_choice_min = 1 * destroyer["repair"]
            hp_choice_max = 2 * destroyer["hp"]
            attack_choice_max = 2 * destroyer["attack"]
            repair_choice_max = 2 * destroyer["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            destroyer1_hp_dict[ident] = level_hp_dict
            destroyer1_attack_dict[ident] = level_attack_dict
            destroyer1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = destroyer["hp"] * 150
            max_attack = destroyer["attack"] * 30
            max_repair = destroyer["repair"] * 15
            hp_choice_min = 1 * destroyer["hp"]
            attack_choice_min = 1 * destroyer["attack"]
            repair_choice_min = 1 * destroyer["repair"]
            hp_choice_max = 3 * destroyer["hp"]
            attack_choice_max = 3 * destroyer["attack"]
            repair_choice_max = 3 * destroyer["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            destroyer2_hp_dict[ident] = level_hp_dict
            destroyer2_attack_dict[ident] = level_attack_dict
            destroyer2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = destroyer["hp"] * 250
            max_attack = destroyer["attack"] * 50
            max_repair = destroyer["repair"] * 25
            hp_choice_min = 1 * destroyer["hp"]
            attack_choice_min = 1 * destroyer["attack"]
            repair_choice_min = 1 * destroyer["repair"]
            hp_choice_max = 5 * destroyer["hp"]
            attack_choice_max = 5 * destroyer["attack"]
            repair_choice_max = 5 * destroyer["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            destroyer3_hp_dict[ident] = level_hp_dict
            destroyer3_attack_dict[ident] = level_attack_dict
            destroyer3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = destroyer["hp"] * 500
            max_attack = destroyer["attack"] * 100
            max_repair = destroyer["repair"] * 50
            hp_choice_min = 1 * destroyer["hp"]
            attack_choice_min = 1 * destroyer["attack"]
            repair_choice_min = 1 * destroyer["repair"]
            hp_choice_max = 5 * destroyer["hp"]
            attack_choice_max = 5 * destroyer["attack"]
            repair_choice_max = 5 * destroyer["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            destroyer4_hp_dict[ident] = level_hp_dict
            destroyer4_attack_dict[ident] = level_attack_dict
            destroyer4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = destroyer["hp"] * 1000
            max_attack = destroyer["attack"] * 200
            max_repair = destroyer["repair"] * 100
            hp_choice_min = 1 * destroyer["hp"]
            attack_choice_min = 1 * destroyer["attack"]
            repair_choice_min = 1 * destroyer["repair"]
            hp_choice_max = 7 * destroyer["hp"]
            attack_choice_max = 7 * destroyer["attack"]
            repair_choice_max = 7 * destroyer["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            destroyer5_hp_dict[ident] = level_hp_dict
            destroyer5_attack_dict[ident] = level_attack_dict
            destroyer5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(destroyer1_hp_dict)
        ship_hp_dict.update(destroyer2_hp_dict)
        ship_hp_dict.update(destroyer3_hp_dict)
        ship_hp_dict.update(destroyer4_hp_dict)
        ship_hp_dict.update(destroyer5_hp_dict)
        ship_attack_dict.update(destroyer1_attack_dict)
        ship_attack_dict.update(destroyer2_attack_dict)
        ship_attack_dict.update(destroyer3_attack_dict)
        ship_attack_dict.update(destroyer4_attack_dict)
        ship_attack_dict.update(destroyer5_attack_dict)
        ship_repair_dict.update(destroyer1_repair_dict)
        ship_repair_dict.update(destroyer2_repair_dict)
        ship_repair_dict.update(destroyer3_repair_dict)
        ship_repair_dict.update(destroyer4_repair_dict)
        ship_repair_dict.update(destroyer5_repair_dict)
    
    for i in range(361, 386): #Battleships
        id = i
        id = str(id)
        level_hp = 0
        level_attack = 0
        level_repair = 0
        level_hp_dict = {}
        level_attack_dict = {}
        level_repair_dict = {}
    
        if ships_data[str(i)]["rarity"] == 1:
        
            #Define values for level-level variation
            max_hp = battleship["hp"] * 100
            max_attack = battleship["attack"] * 20
            max_repair = battleship["repair"] * 10
            hp_choice_min = 1 * battleship["hp"]
            attack_choice_min = 1 * battleship["attack"]
            repair_choice_min = 1 * battleship["repair"]
            hp_choice_max = 2 * battleship["hp"]
            attack_choice_max = 2 * battleship["attack"]
            repair_choice_max = 2 * battleship["repair"]
        
            for i in range(1, rare1_max_levels):
                level_hp = level_hp + (max_hp / rare1_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare1_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare1_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            battleship1_hp_dict[ident] = level_hp_dict
            battleship1_attack_dict[ident] = level_attack_dict
            battleship1_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 2:
        
            #Define values for level-level variation
            max_hp = battleship["hp"] * 150
            max_attack = battleship["attack"] * 30
            max_repair = battleship["repair"] * 15
            hp_choice_min = 1 * battleship["hp"]
            attack_choice_min = 1 * battleship["attack"]
            repair_choice_min = 1 * battleship["repair"]
            hp_choice_max = 3 * battleship["hp"]
            attack_choice_max = 3 * battleship["attack"]
            repair_choice_max = 3 * battleship["repair"]
        
            for i in range(1, rare2_max_levels):
                level_hp = level_hp + (max_hp / rare2_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare2_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare2_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            battleship2_hp_dict[ident] = level_hp_dict
            battleship2_attack_dict[ident] = level_attack_dict
            battleship2_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 3:
        
            #Define values for level-level variation
            max_hp = battleship["hp"] * 250
            max_attack = battleship["attack"] * 50
            max_repair = battleship["repair"] * 25
            hp_choice_min = 1 * battleship["hp"]
            attack_choice_min = 1 * battleship["attack"]
            repair_choice_min = 1 * battleship["repair"]
            hp_choice_max = 5 * battleship["hp"]
            attack_choice_max = 5 * battleship["attack"]
            repair_choice_max = 5 * battleship["repair"]
        
            for i in range(1, rare3_max_levels):
                level_hp = level_hp + (max_hp / rare3_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare3_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare3_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            battleship3_hp_dict[ident] = level_hp_dict
            battleship3_attack_dict[ident] = level_attack_dict
            battleship3_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 4:
        
            #Define values for level-level variation
            max_hp = battleship["hp"] * 500
            max_attack = battleship["attack"] * 100
            max_repair = battleship["repair"] * 50
            hp_choice_min = 1 * battleship["hp"]
            attack_choice_min = 1 * battleship["attack"]
            repair_choice_min = 1 * battleship["repair"]
            hp_choice_max = 5 * battleship["hp"]
            attack_choice_max = 5 * battleship["attack"]
            repair_choice_max = 5 * battleship["repair"]
        
            for i in range(1, rare4_max_levels):
                level_hp = level_hp + (max_hp / rare4_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare4_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare4_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            battleship4_hp_dict[ident] = level_hp_dict
            battleship4_attack_dict[ident] = level_attack_dict
            battleship4_repair_dict[ident] = level_repair_dict
        
        elif ships_data[str(i)]["rarity"] == 5:
        
            #Define values for level-level variation
            max_hp = battleship["hp"] * 1000
            max_attack = battleship["attack"] * 200
            max_repair = battleship["repair"] * 100
            hp_choice_min = 1 * battleship["hp"]
            attack_choice_min = 1 * battleship["attack"]
            repair_choice_min = 1 * battleship["repair"]
            hp_choice_max = 7 * battleship["hp"]
            attack_choice_max = 7 * battleship["attack"]
            repair_choice_max = 7 * battleship["repair"]
        
            for i in range(1, rare5_max_levels):
                level_hp = level_hp + (max_hp / rare5_max_levels) + random.randrange(hp_choice_min, hp_choice_max)
                level_attack = level_attack + (max_attack / rare5_max_levels) + random.randrange(attack_choice_min, attack_choice_max)
                level_repair = level_repair + (max_repair / rare5_max_levels) + random.randrange(repair_choice_min, repair_choice_max)
                level_hp_dict[str(i)] = level_hp
                level_attack_dict[str(i)] = level_attack
                level_repair_dict[str(i)] = level_repair
            
            ident = ships_data[id]["ident"]
            battleship5_hp_dict[ident] = level_hp_dict
            battleship5_attack_dict[ident] = level_attack_dict
            battleship5_repair_dict[ident] = level_repair_dict
        
        ship_hp_dict.update(battleship1_hp_dict)
        ship_hp_dict.update(battleship2_hp_dict)
        ship_hp_dict.update(battleship3_hp_dict)
        ship_hp_dict.update(battleship4_hp_dict)
        ship_hp_dict.update(battleship5_hp_dict)
        ship_attack_dict.update(battleship1_attack_dict)
        ship_attack_dict.update(battleship2_attack_dict)
        ship_attack_dict.update(battleship3_attack_dict)
        ship_attack_dict.update(battleship4_attack_dict)
        ship_attack_dict.update(battleship5_attack_dict)
        ship_repair_dict.update(battleship1_repair_dict)
        ship_repair_dict.update(battleship2_repair_dict)
        ship_repair_dict.update(battleship3_repair_dict)
        ship_repair_dict.update(battleship4_repair_dict)
        ship_repair_dict.update(battleship5_repair_dict)
    hp_string = json.dumps(ship_hp_dict)
    hp_table_file.write(hp_string)
    attack_string = json.dumps(ship_attack_dict)
    attack_table_file.write(attack_string)
    repair_string = json.dumps(ship_repair_dict)
    repair_table_file.write(repair_string)

if __name__ == "__main__":
    main()
