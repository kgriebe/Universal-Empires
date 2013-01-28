#!/bin/python

class player():
    def __init__(self):
        self.name = ""
        self.ship_list = {}
        self.rank = ""
        self.credits = ""
        self.fuel_rods = ""
    
def new_player(name):
    x = player()
    x.name = name
    x.rank = "1"
    x.credits = "1000"
    x.fuel_rods = "0"
    
    f = open("./Players/" + x.name, 'a')
    f.write("Name: " + x.name + '\n')
    f.write("Rank: " + x.rank + '\n')
    f.write("Credits: " + x.credits + '\n')
    f.write("Fuel Rods: " + x.fuel_rods + '\n')
    f.close
