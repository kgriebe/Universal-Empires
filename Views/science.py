#!/usr/bin/python
import sys, os
import __builtin__
from Controllers.prompt import prompt
from Controllers.commands import command_process

def view_creator():
    science_file = open('./Data/science.txt', 'w+')

    #Define Variables
    full_line = "************************************************************".center(80) + "\n"
    beginning_line = "          *****"
    end_line = "*****          " + "\n"
    empty_line = beginning_line + " ".center(50) + end_line

    science_file.write(full_line*3)
    science_file.write(empty_line)
    line = beginning_line + "Applied Research".center(50) + end_line
    science_file.write(line)
    science_file.write(empty_line)
    science_file.write(full_line*3)

def applied_research():
    print "Blah"

def selection_process(selection):
    if selection.lower() == "applied research":
        applied_research()
    else:
        print "\n Invalid selection.  Please try again.\n"
        selection = raw_input("Applied Research".center(80) + "\n\n" + prompt(__builtin__.active_user))
        command_process(selection)
        selection_process(selection)

def science_view():
    view_creator()
    science_file = open('./Data/science.txt', 'r')
    os.system('clear')
    for line in science_file:
        sys.stdout.write(line)
    sys.stdout.write("\n")
    selection = raw_input("Applied Research".center(80) + "\n\n" + prompt(__builtin__.active_user))
    command_process(selection)
    selection_process(selection)

