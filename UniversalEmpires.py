#!/usr/bin/python

from Classes.ships import *
from Players.new_player import *
from Players.login import *
from Classes.new_ship import *
from Views.selection_screen import *
import json
import os

def main():
    
# 	Prompt for login, load player data after login or player creation
    player_name = login()
    file_path = "./Players/" + player_name + ".data"   
    with open(file_path) as player_data:
    	player_json = json.load(player_data)
    selection_screen()

 	   
if __name__ == "__main__":
        main()