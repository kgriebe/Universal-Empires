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
        new_player(var)
    return var