#!/usr/bin/env python3 
from sys import argv
filename=argv[1]

with open(filename) as f:
	for line in f:
            if not line.startswith('!') and not 'duplex' in line and not 'alias' in line and not 'Current configuration' in line:
                print(line.strip())
            else:
                pass
