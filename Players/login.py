#!/usr/bin/python
from new_player import *
import os

def login():
    var = raw_input("Login: ")
    file_path = "./Players/" + var
    if os.path.exists(file_path):
        password = raw_input("Password: ")
    else:
        print "Creating New Player"
        race = raw_input("Please select your race: RUFS, AMV, DIC, LBS, STS.  Enter \"Help\" for information on each race.\n")
        new_player(var, race)
    return var