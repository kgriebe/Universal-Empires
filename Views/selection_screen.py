#!/usr/bin/python

import os, sys
import __builtin__
from ship_hanger import ship_hanger
from wormholes import wormholes
from communications import communications
from salvage_missions import salvage_missions
from Controllers.commands import command_process

def selection_process():
	selection = raw_input("Selection: ")
	# Check for exit/back commands
	command_process(selection)
	selection = selection.lower()
	if selection == "ship hanger":
		f = open('./Data/ship_hanger.txt', 'w')
		f.close()
		ship_hanger()
	elif selection == "wormholes":
		wormholes()
	elif selection == "salvage missions":
		salvage_missions()
	elif selection == "communications":
		communications()
	else:
		print "Invalid Selection"
		selection_process()


def selection_screen():
	selection_screen = open('./Data/selection_screen.txt')
	os.system('clear')
	for line in selection_screen:
		sys.stdout.write(line)
	print "\n"
	selection_process()

