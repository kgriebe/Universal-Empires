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
from random import choice

def priority_assign(pull_list, priority_dict):
    user = __builtin__.active_user
    with open("./Players/" + user + ".data") as player_json:
        player_data = json.load(player_json)

    with open("./Data/ships.json") as ships_json:
        ships_data = json.load(ships_json)
    priority_comparison_1 = []
    priority_comparison_2 = []
    priority_comparison_3 = []
    priority_comparison_4 = []
    priority_comparison_5 = []
    final_player_data = {}

    for key, value in priority_dict.iteritems():
        if str(value) in pull_list:
            if str(key) == "1":
                priority_comparison_1.append(value)
            elif str(key) == "2":
                priority_comparison_2.append(value)
            elif str(key) == "3":
                priority_comparison_3.append(value)
            elif str(key) == "4":
                priority_comparison_4.append(value)
            elif str(key) == "5":
                priority_comparison_5.append(value)
        else:
            pass
    if priority_comparison_1:
        print "You have been awarded %s." % str(ships_data[str(priority_comparison_1[0])]["name"])
        old_ships_list = player_data[user]["ship_list"]
        new_ships_list = old_ships_list
        if str(priority_comparison_1[0]) in new_ships_list:
            target_list = new_ships_list[str(priority_comparison_1[0])]
            target_list.append(str(choice(range(1, 30))))
        else:
            new_ships_list[str(priority_comparison_1[0])] = [str(choice(range(1, 30)))]
        new_player_data = {}
        for key, value in player_data[user].iteritems():
            if key == "ship_list":
                pass
            else:
                new_player_data[key] = value
        new_player_data["ship_list"] = new_ships_list
        print new_player_data
    elif priority_comparison_2:
        print "You have been awarded %s." % str(ships_data[str(priority_comparison_1[0])]["name"])
        old_ships_list = player_data[user]["ship_list"]
        new_ships_list = old_ships_list
        if str(priority_comparison_2[0]) in new_ships_list:
            target_list = new_ships_list[str(priority_comparison_2[0])]
            target_list.append(str(choice(range(1, 30))))
        else:
            new_ships_list[str(priority_comparison_2[0])] = [str(choice(range(1, 30)))]
        new_player_data = {}
        for key, value in player_data[user].iteritems():
            if key == "ship_list":
                pass
            else:
                new_player_data[key] = value
        new_player_data["ship_list"] = new_ships_list
        print new_player_data
    elif priority_comparison_3:
        print "You have been awarded %s." % str(ships_data[str(priority_comparison_1[0])]["name"])
        old_ships_list = player_data[user]["ship_list"]
        new_ships_list = old_ships_list
        if str(priority_comparison_3[0]) in new_ships_list:
            target_list = new_ships_list[str(priority_comparison_3[0])]
            target_list.append(str(choice(range(1, 30))))
        else:
            new_ships_list[str(priority_comparison_3[0])] = [str(choice(range(1, 30)))]
        new_player_data = {}
        for key, value in player_data[user].iteritems():
            if key == "ship_list":
                pass
            else:
                new_player_data[key] = value
        new_player_data["ship_list"] = new_ships_list
        print new_player_data
    elif priority_comparison_4:
        print "You have been awarded %s." % str(ships_data[str(priority_comparison_1[0])]["name"])
        old_ships_list = player_data[user]["ship_list"]
        new_ships_list = old_ships_list
        if str(priority_comparison_4[0]) in new_ships_list:
            target_list = new_ships_list[str(priority_comparison_4[0])]
            target_list.append(str(choice(range(1, 30))))
        else:
            new_ships_list[str(priority_comparison_4[0])] = [str(choice(range(1, 30)))]
        new_player_data = {}
        for key, value in player_data[user].iteritems():
            if key == "ship_list":
                pass
            else:
                new_player_data[key] = value
        new_player_data["ship_list"] = new_ships_list
        print new_player_data
    elif priority_comparison_5:
        print "You have been awarded %s." % str(ships_data[str(priority_comparison_1[0])]["name"])
        old_ships_list = player_data[user]["ship_list"]
        new_ships_list = old_ships_list
        if str(priority_comparison_5[0]) in new_ships_list:
            target_list = new_ships_list[str(priority_comparison_5[0])]
            target_list.append(str(choice(range(1, 30))))
        else:
            new_ships_list[str(priority_comparison_5[0])] = [str(choice(range(1, 30)))]
        new_player_data = {}
        for key, value in player_data[user].iteritems():
            if key == "ship_list":
                pass
            else:
                new_player_data[key] = value
        new_player_data["ship_list"] = new_ships_list
        print new_player_data
    else:
        print "You have been awarded: %s" % str(ships_data[str(choice(pull_list))]["name"])
    final_player_data[user] = new_player_data
    f = open('./Players/' + user + ".data", 'w')
    json_data = json.dumps(final_player_data)
    f.write(json_data)
    f.close()
    

def pull_generator(pulls, race):
    with open("./Data/ships.json") as ships_json:
        ship_data = json.load(ships_json)
    pull_list = []
    result_list = []
    counter = 0
    for item in ship_list:
        if ship_data[str(item)]["rarity"] == 5:
            item = str(item)
            pull_list.append(item)
        elif ship_data[str(item)]["rarity"] == 4:
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
        elif ship_data[str(item)]["rarity"] == 3:
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
            pull_list.append(item)
    for ship in bonus_list:
        if ship_data[str(ship)]["rarity"] == 5:
            pull_list.append(ship)
        elif ship_data[str(ship)]["rarity"] == 4:
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
        elif ship_data[str(ship)]["rarity"] == 3:
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
            pull_list.append(ship)
    while counter < int(pulls):
        result = choice(pull_list)
        counter += 1
        result_list.append(result)
    result_list.append("232")
    return result_list



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
    # Set variables and open files
    counter = 1
    priority_dict = {}

    with open("./Data/ships.json") as ships_json:
        ship_data = json.load(ships_json)
    user = __builtin__.active_user

    # Begin generating race-specific agent view
    os.system('clear')
    sys.stdout.write(full_line*3)
    sys.stdout.write(empty_line)
    sys.stdout.write(beginning_line + (selection.upper() + " Agent").center(50) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(beginning_line + " Current ships with x2 salvage rate:" + " "*14 + end_line)
    # Check to see what agent/race we should be displaying.
    for item in bonus_list:
        string = ship_data[str(item)]["name"]
        sys.stdout.write(beginning_line + "     " + string + " "*(45 - len(string)) + end_line)
    sys.stdout.write(empty_line)
    sys.stdout.write(full_line*3)
    sys.stdout.write("\n")
    sys.stdout.write("Back | Exit".center(80) + "\n\n")
    # Ask the player how much tech he is going to spend
    sub_selection = raw_input("Please enter the amount of tech to spend:".center(80) + "\n\n" + prompt(user))
    sub_selection = sub_selection.lower()
    command_process(sub_selection)
    # Check for "back"
    if sub_selection == "back":
        salvage_missions.salvage_missions()
    else:
        # Check to see if the player input can be converted to an integer
        try:
            tech_spend = number_check(sub_selection)
            sys.stdout.write("\n")
            # If input is an integer and less than or equal to 5, ask player how many ships for priority list
            if tech_spend <= 5:
                sys.stdout.write("You can select up to %d ships for your priority target list.\n" % tech_spend)
                target_number = raw_input("How many priority targets do you wish to select?\n")
                # Check to make sure player entered an integer
                target_number = number_check(target_number)
                # Start handling exception cases
                if target_number > tech_spend:
                    print "Error: You can only select up to %d priority targets.\n" % tech_spend
                    sleep(2)
                    agent_view_creator(selection)
                # If no exception, iterate through number of targets specified and collect each target id
                while counter <= target_number:
                    ship = raw_input("Please enter the identificiation number of priority target %s:\n" % counter)
                    ship_id = number_check(ship)
                    # If the target ID is valid, check to make sure the player hasn't already added it
                    if str(ship_id) in priority_dict.items():
                        print "Error: You may only select each ship one time."
                        agent_view_creator(selection)
                    else:
                        if str(ship_id) in ship_data:
                            priority_dict[counter] = ship_id
                    # If the target ID is invalid, notify player and go back to agent_view
                        else:
                            print "That identifier is not valid."
                            sleep(2)
                            agent_view_creator(selection)
                    counter += 1
            # If input is between 5 and 10, ask player how many ships for priority list
            elif tech_spend > 5 and tech_spend <= 10:
                sys.stdout.write("You can select up to 5 ships for your priority target list.\n")
                target_number = raw_input("How many priority targets do you wish to select?\n")
                # Make sure input is an integer
                target_number = number_check(target_number)
                # If player is trying to set more than 5 priority targets, error
                if target_number > 5:
                    print "Error: You can only select up to 5 priority targets.\n"
                    sleep(2)
                    agent_view_creator(selection)
                while counter <= target_number:
                    # Collect identification numbers for priority targets
                    ship = raw_input("Please enter the identificiation number of priority target %s:\n" % counter)
                    ship_id = number_check(ship)
                    # If target ID is valid, enter it into priority dict
                    if str(ship_id) in ship_data:
                        priority_dict[counter] = ship_id
                    # If target is invalid, notify player and return to agent_view
                    else:
                        print "That identifier is not valid."
                        sleep(2)
                        agent_view_creator(selection)
                    counter += 1
            # Raise error if player tries to spend more than 10 tech on one mission.
            else:
                print "Error: You can only spend a maximum of 10 tech per mission."
                sleep(2)
                agent_view_creator(selection)

        except:
            print "Invalid Selection"
            sleep(2)
            agent_view_creator(selection)
    final_pull_list = pull_generator(tech_spend, selection)
    result = priority_assign(final_pull_list, priority_dict)

def agent_view(selection):
    if selection == "general":
        general_view_creator()
    else:
        agent_view_creator(selection)