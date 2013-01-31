#!/usr/bin/python
from new_player import *
import os
from bcrypt import hashpw, gensalt
player_dict = {}


def password_get():
    password = raw_input("Please enter your desired password.\n")
    password1 = raw_input("Please confirm your password.\n")
    if not password == password1:
        print "Your passwords did not match.  Please try again.\n"
        password_get()
    else:
        hashed_password = hashpw(password, gensalt())
    return hashed_password

def login():
    var = raw_input("Login: ")
    file_path = "./Players/" + var
    if os.path.exists(file_path):
        password = raw_input("Password: ")
        with open(file_path) as player_file:
    		player_json = json.load(player_file)
    	if hashpw(password, hashed) == player_json["password"]:
    	    print "Login Successful.\n"
    	else:
    	    print "Password does not match.  Please try again.\n"
    	    login()
    else:
        print "Creating New Player"
        race = raw_input("Please select your race: RUFS, AMV, DIC, LBS, STS.  Enter \"Help\" for information on each race.\n")
        password = password_get()
        new_player(var, race, password)
    return var
