#!/usr/bin/env python3 
from sys import argv
filename=argv[1]

#with open(filename) as f:
#	for line in f:
#            if not line.startswith('!') and not 'duplex' in line and not 'alias' in line and not 'Current configuration' in line:
#                print(line.rstrip())
#            else:
#                pass
ignore=['duplex','alias','Current configuration']

with open(filename) as f, open('config_sw1_cleared.txt','w') as dest:
	for line in f:
            for word in ignore:
                if line.startswith('!') or word in line:
                        break
            else:
                dest.write((line.rstrip()+"\n"))

