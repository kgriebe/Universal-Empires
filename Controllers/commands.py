#!/usr/bin/python
import sys

def command_process(command):
    if command.lower() == "exit":
        sys.exit(0)
    elif command.lower() == "":
        return "null"
    else:
        return command
