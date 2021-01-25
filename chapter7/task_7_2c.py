#!/usr/bin/env python3 
from sys import argv
srcfile,dstfile=argv[1],argv[2]

#with open(filename) as f:
#	for line in f:
#            if not line.startswith('!') and not 'duplex' in line and not 'alias' in line and not 'Current configuration' in line:
#                print(line.rstrip())
#            else:
#                pass
ignore=['duplex','alias','Current configuration']

with open(srcfile) as f, open(dstfile,'w') as dest:
	for line in f:
            for word in ignore:
                if line.startswith('!') or word in line:
                        break
            else:
                dest.write((line.rstrip()+"\n"))

