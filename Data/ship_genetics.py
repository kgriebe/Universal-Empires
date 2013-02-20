#!/usr/bin/python

import os, sys
import json
import random

def main():
	with open('attack.json') as attack_json:
		attack_data = json.load(attack_json)
	with open('hp.json') as hp_json:
		hp_data = json.load(hp_json)
	with open('repair.json') as repair_json:
		repair_data = json.load(repair_json)

	print attack_data
	for key, value in sorted(attack_data["5"].iteritems()):
		print key, value










if __name__ == "__main__":
	main()