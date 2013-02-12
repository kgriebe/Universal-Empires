#!/usr/bin/python

from Config.vars import full_line, empty_line, beginning_line, end_line
import os, sys
import json
from Controllers.commands import command_process
from time import sleep
from Data.gamedata import *
from Controllers.prompt import prompt
import __builtin__
import salvage_missions


def general_view_creator():
    pass

def number_check(potential_number):
    try:
        number = int(potential_number)
        return number
    except:
        selection = raw_input("Error: Not a valid vessel identification number.  Please try again.\n")
        number_check(selection)

def agent_view_creator(selection):
    counter = 1
    priority_list = []

    with open("./Data/ships.json") as ships_json:
        ship_data = json.load(ships_json)
    user = __builtin__.active_user

    if selection == "general":
        general_view_creator()
        
    os.system('clear')
    sys.stdout.write(full_line*3)
    sys.stdout.write(empty_line)
    sys.stdout.write(beginning_line + (selection.upper() + " Agent").center(50) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(beginning_line + " Current ships with x2 salvage rate:" + " "*14 + end_line)
    if selection == "rufs":
        for item in rufs_bonus:
            string = ship_data[str(item)]["name"]
            sys.stdout.write(beginning_line + "     " + string + " "*(45 - len(string)) + end_line)
    elif selection == "sts":
        for item in sts_bonus:
            string = ship_data[str(item)]["name"]
            sys.stdout.write(beginning_line + "     " + string + " "*(45 - len(string)) + end_line)
    elif selection == "lbs":
        for item in lbs_bonus:
            string = ship_data[str(item)]["name"]
            sys.stdout.write(beginning_line + "     " + string + " "*(45 - len(string)) + end_line)
    elif selection == "dic":
        for item in dic_bonus:
            string = ship_data[str(item)]["name"]
            sys.stdout.write(beginning_line + "     " + string + " "*(45 - len(string)) + end_line)
    elif selection == "amv":
        for item in amv_bonus:
            string = ship_data[str(item)]["name"]
            sys.stdout.write(beginning_line + "     " + string + " "*(45 - len(string)) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(full_line*3)
    sys.stdout.write("\n")
    sys.stdout.write("Back | Exit".center(80) + "\n\n")
    sub_selection = raw_input("Please enter the amount of tech to spend:".center(80) + "\n\n" + prompt(user))
    sub_selection = sub_selection.lower()
    command_process(sub_selection)
    if sub_selection == "back":
        salvage_missions.salvage_missions()
    else:
        try:
            tech_spend = int(sub_selection)
            sys.stdout.write("\n")
            if tech_spend <= 5:
                sys.stdout.write("You can select up to %d ships for your priority target list.\n" % tech_spend)
                target_number = raw_input("How many priority targets do you wish to select?\n")
                target_number = number_check(target_number)
                if target_number > tech_spend:
                    print "Error: You can only select up to %d priority targets.\n" % tech_spend
                    sleep(2)
                    agent_view_creator(selection)
                while counter <= target_number:
                    ship = raw_input("Please enter the identificiation number of priority target %s:\n" % counter)
                    ship_id = number_check(ship)
                    if str(ship_id) in ship_data:
                        pass
                    else:
                        print "That identifier is not valid."
                        sleep(2)
                        agent_view_creator(selection)
                    counter += 1
            elif tech_spend >= 5 and tech_spend <= 10:
                sys.stdout.write("You can select up to 5 ships for your priority target list.\n")
                target_number = raw_input("How many priority targets do you wish to select?\n")
                target_number = number_check(target_number)
                if target_number > 5:
                    print "Error: You can only select up to 5 priority targets.\n"
                    sleep(2)
                    agent_view_creator(selection)
                while counter <= target_number:
                    ship = raw_input("Please enter the identificiation number of priority target %s:\n" % counter)
                    ship_id = number_check(ship)
                    if str(ship_id) in ship_data:
                        pass
                    else:
                        print "That identifier is not valid."
                        sleep(2)
                        agent_view_creator(selection)
                    counter += 1
            else:
                print "Error: You can only spend a maximum of 10 tech per mission."
                sleep(2)
                agent_view_creator(selection)

        except:
            print "Invalid Selection"
            sleep(2)
            agent_view_creator(selection)


def agent_view(selection):
    if selection == "general":
        general_view_creator()
    else:
        agent_view_creator(selection)