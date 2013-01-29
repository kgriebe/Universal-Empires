#!/bin/python
from Classes.ships import ship
import re

def new_ship():
    f = open("./Data/RUF_ships.py", 'r')
    new_ship = ship()
    for line in f:
        new_ship = re.search(r'name = "RUF Salvager"', line)
        if new_ship:
            print new_ship.group(0)
    
    