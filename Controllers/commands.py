#!/usr/bin/python
import sys

def command_process(command):
	if command.lower() == "exit":
		sys.exit(0)
	else:
		return command
