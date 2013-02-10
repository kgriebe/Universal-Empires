#!/usr/bin/python

import __builtin__
import json
import sys, os
from Controllers.prompt import prompt
from Controllers.commands import command_process
import ship_hanger
from Config.vars import beginning_line, end_line, empty_line, full_line

with open("./Data/ships.json") as ship_data:
    ship_json = json.load(ship_data)

def length_finder(id, attribute):
    result = len(str(ship_json[str(id)][attribute]))
    return result



def info_generator(id):
    os.system('clear')
    print "\n"
    sys.stdout.write(full_line*3 + empty_line + beginning_line + ship_json[str(id)]["name"].center(50) + end_line +  empty_line)
    sys.stdout.write(beginning_line + " Ship Race: %s" % ship_json[str(id)]["race"] + " "*(23 - length_finder(id, "race")) + "Level: %s\\%s" % (ship_json[str(id)]["level"], ship_json[str(id)]["max_level"]) + " "*(7 - (length_finder(id, "level") + length_finder(id, "max_level"))) + end_line)
    sys.stdout.write(beginning_line + " Damage Type: %s" % ship_json[str(id)]["damage_type"] + " "*(21 - length_finder(id, "damage_type")) + "Exp: %s" % ship_json[str(id)]["exp"] + " "*(10 - length_finder(id, "exp")) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(beginning_line + " Fleet Skill: %s" % ship_json[str(id)]["fleet_leader_skill"] + " "*(36 - length_finder(id, "fleet_leader_skill")) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(full_line*2)
    sys.stdout.write(empty_line)
    sys.stdout.write(beginning_line + " Skill: %s" % ship_json[str(id)]["skill"] + " "*(27 - length_finder(id, "skill")) + "Attack: %s" % ship_json[str(id)]["attack_value"] + " "*(7 - length_finder(id, "attack_value")) + end_line)
    sys.stdout.write(beginning_line + " Ident: %s" % ship_json[str(id)]["ident"] + " "*(27 - length_finder(id, "ident")) + "Shield: %s" % ship_json[str(id)]["shield_points"] + " "*(7 - length_finder(id, "shield_points")) + end_line)
    sys.stdout.write(beginning_line + " Rarity: %s" % ship_json[str(id)]["rarity"] + " "*(26 - length_finder(id, "rarity")) + "Repair: %s" % ship_json[str(id)]["repair_rate"] + " "*(7 - length_finder(id, "repair_rate")) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(full_line*2)
    sys.stdout.write(empty_line)
    sys.stdout.write(beginning_line + " Weapon Mod: %s" % ship_json[str(id)]["weapon_mod"] + " "*(22 - length_finder(id, "weapon_mod")) + "Max Mods: %s" % ship_json[str(id)]["weapon_hardpoint"] + " "*(5 - length_finder(id, "weapon_hardpoint")) + end_line)
    sys.stdout.write(beginning_line + " Armor Mod: %s" % ship_json[str(id)]["armor_mod"] + " "*(23 - length_finder(id, "armor_mod")) + "Max Mods: %s" % ship_json[str(id)]["armor_hardpoint"] + " "*(5 - length_finder(id, "armor_hardpoint")) + end_line)
    sys.stdout.write(beginning_line + " Shield Mod: %s" % ship_json[str(id)]["shield_mod"] + " "*(22 - length_finder(id, "shield_mod")) + "Max Mods: %s" % ship_json[str(id)]["shield_hardpoint"] + " "*(5 - length_finder(id, "armor_hardpoint")) + end_line)
    sys.stdout.write(beginning_line + " Engine Mod: %s" % ship_json[str(id)]["engine_mod"] + " "*(22 - length_finder(id, "engine_mod")) + "Max Mods: %s" % ship_json[str(id)]["engine_hardpoint"] + " "*(5 - length_finder(id, "armor_hardpoint")) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(full_line*3)

def selection_process(input):
    # Load up player file
    file_path = "./Players/" + __builtin__.active_user + ".data"
    with open(file_path) as player_data:
        player_json = json.load(player_data)
    player_ship_list = player_json[__builtin__.active_user]["ship_list"]
    if input == "info":
        id = raw_input("\nPlease enter the ID number of the ship:\n")
        if int(id) in player_ship_list:
            info_generator(id)
            print "\n\n"
            print "\n"
            selection = raw_input("Info | Back | Exit".center(80) + "\n\n" + prompt(__builtin__.active_user))
            if selection.lower() == "back":
                os.system('clear')
                roster_view(__builtin__.active_user)
            else:
                selection_process(selection)
        else:
            if id in ship_json:
                print "You do not command that ship.\n"
                selection_process(input)
            else:
                print "That vessel does not exist.\n"
                selection_process(input)
    elif input == "back":
        ship_hanger.ship_hanger()
    else:
        command_process(input)
        print "Invalid Selection."
        selection = raw_input("Info | Back | Exit".center(80) + "\n\n" + prompt(__builtin__.active_user))
        selection_process(selection)


def view_generator(user):
    #Open file
    roster_file = open('./Data/roster.txt', 'w+')

    #Define Variables
    full_line = "************************************************************".center(80) + "\n"
    beginning_line = "          *****"
    end_line = "*****          " + "\n"
    empty_line = beginning_line + " ".center(50) + end_line

    roster_file.write(full_line*3)
    roster_file.write(empty_line)

    # Load up player file
    file_path = "./Players/" + __builtin__.active_user + ".data"
    with open(file_path) as player_data:
        player_json = json.load(player_data)

    #For ships in the active ship list, create the view listing those ships.
    for id in player_json[__builtin__.active_user]["ship_list"]:
        #Format the lines
        ship = "[ " + str(id) + " ] " + ship_json[str(id)]["race"] + " " + ship_json[str(id)]["name"]
        line = beginning_line + "     " + ship + " ".ljust(45 - len(ship)) + end_line
        roster_file.write(line)

    #Write the trailing lines
    roster_file.write(empty_line)
    roster_file.write(full_line)
    roster_file.write(full_line)
    roster_file.write(full_line)
    return "Success"

def roster_view(user):
    result = view_generator(user)
    if result:
        roster_view_file = open('./Data/roster.txt')
    for line in roster_view_file:
        sys.stdout.write(line)
    print "\n"
    selection = raw_input("Info | Back | Exit".center(80) + "\n\n" + prompt(__builtin__.active_user))
    selection_process(selection)




