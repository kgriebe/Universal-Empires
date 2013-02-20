#!/usr/bin/python

import os, sys
import json
import random
import ships_levels_stats_generator

def main():
	number = 10
	ships_levels_stats_generator.interface(str(number))
	
	for i in range(0, number):
	    with open('../Test/attack%s.json' % i) as attack_json:
	        attack_data = json.load(attack_json)
	    with open('../Test/hp%s.json' % i) as hp_json:
	        hp_data = json.load(hp_json)
	    with open('../Test/repair%s.json' % i) as repair_json:
	        repair_data = json.load(repair_json)
	        
	    for key in sorted(attack_data.iterkeys()):
	        if len(attack_data[key]) < 20:
	            print "Under 20."
	        elif len(attack_data[key]) < 30:
	            print "Under 30."
	        elif len(attack_data[key]) < 60:
	            print "Under 50."
	        elif len(attack_data[key]) < 80:
	            print "Under 80."
	        else:
	            print "Over 80."
	
	
	
	
#	with open('attack.json') as attack_json:
#		attack_data = json.load(attack_json)
#	with open('hp.json') as hp_json:
#		hp_data = json.load(hp_json)
#	with open('repair.json') as repair_json:
#		repair_data = json.load(repair_json)










if __name__ == "__main__":
	main()