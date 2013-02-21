#!/usr/bin/python

import os, sys
import json
import random
import ships_levels_stats_generator
import collections

def fitness_eval():
	number = 10
	attack_data = {}
	hp_data = {}
	repair_data = {}
	attack_fitness_dict = {}
	hp_fitness_dict = {}
	repair_fitness_dict = {}

	ships_levels_stats_generator.interface(str(number))
	
	# format is {file_number {ship_id {level: value}}}
	for i in range(0, number):
	    with open('../Test/attack%s.json' % i) as attack_json:
	        attack_data[i] = json.load(attack_json)
	    with open('../Test/hp%s.json' % i) as hp_json:
	        hp_data[i] = json.load(hp_json)
	    with open('../Test/repair%s.json' % i) as repair_json:
	        repair_data[i] = json.load(repair_json)

	for file_number in attack_data.iterkeys():
	    fitness = 0
	    for ship_id in attack_data[file_number].iterkeys():
	        if len(attack_data[file_number][ship_id]) == 15:
	            for i in range(1, 16):
	                level = str(i)
	                value1 = attack_data[file_number][ship_id][level]
	                for i in range(0, number):
	                    value2 = attack_data[i][ship_id][level]
	                    if value2 * .9 <= value1 <= value2 * 1.1:
	                        pass
	                    else:
#	                        print "Increasing Fitness: [%s, %s, %s-%s]" % (value1, value2, value2 * .9, value2 * 1.1)
	                        fitness+=1
	        elif len(attack_data[file_number][ship_id]) == 25:
	            for i in range(1, 26):
	                level = str(i)
	                value1 = attack_data[file_number][ship_id][level]
	                for i in range(0, number):
	                    value2 = attack_data[i][ship_id][level]
	                    if value2 * .9 <= value1 <= value2 * 1.1:
	                        pass
	                    else:
	                        fitness += 1
	        elif len(attack_data[file_number][ship_id]) == 50:
	            for i in range(1, 51):
	                level = str(i)
	                value1 = attack_data[file_number][ship_id][level]
	                for i in range(0, number):
	                    value2 = attack_data[i][ship_id][level]
	                    if value2 * .9 <= value1 <= value2 * 1.1:
	                        pass
	                    else:
	                        fitness += 1
	        elif len(attack_data[file_number][ship_id]) == 75:
	            for i in range(1, 76):
	                level = str(i)
	                value1 = attack_data[file_number][ship_id][level]
	                for i in range(0, number):
	                    value2 = attack_data[i][ship_id][level]
	                    if value2 * .9 <= value1 <= value2 * 1.1:
	                        pass
	                    else:
	                        fitness += 1
	        elif len(attack_data[file_number][ship_id]) == 99:
	            for i in range(1, 76):
	                level = str(i)
	                value1 = attack_data[file_number][ship_id][level]
	                for i in range(0, number):
	                    value2 = attack_data[i][ship_id][level]
	                    if value2 * .9 <= value1 <= value2 * 1.1:
	                        pass
	                    else:
	                        fitness += 1
	    attack_fitness_dict[file_number] = fitness
	print sorted(attack_fitness_dict.items(), key=lambda x: x[1])
	print attack_data[2]["232"]["99"]
	

	
def main():
    fitness_eval()

if __name__ == "__main__":
	main()