#!/usr/bin/env python3 
from sys import argv
#srcfile,dstfile=argv[1],argv[2]
srcfile=argv[1]

#sw1#sh mac address-table
#Mac Address Table
#-------------------------------------------
#
#Vlan    Mac Address       Type        Ports
#----    -----------       --------    -----
# 100    01bb.c580.7000    DYNAMIC     Gi0/1
# 200    0a4b.c380.7c00    DYNAMIC     Gi0/2
# 300    a2ab.c5a0.700e    DYNAMIC     Gi0/3
# 10     0a1b.1c80.7000    DYNAMIC     Gi0/4
# 500    02b1.3c80.7b00    DYNAMIC     Gi0/5
# 200    1a4b.c580.7000    DYNAMIC     Gi0/6
# 300    0a1b.5c80.70f0    DYNAMIC     Gi0/7
# 10     01ab.c5d0.70d0    DYNAMIC     Gi0/8
# 1000   0a4b.c380.7d00    DYNAMIC     Gi0/9

#with open(filename) as f:
#	for line in f:
#            if not line.startswith('!') and not 'duplex' in line and not 'alias' in line and not 'Current configuration' in line:
#                print(line.rstrip())
#            else:
#                pass
#ignore=['duplex','alias','Current configuration']

#with open(srcfile) as f, open(dstfile,'w') as dest:
#	for line in f:
#            for word in ignore:
#                if line.startswith('!') or word in line:
#                        break
#            else:
#                dest.write((line.rstrip()+"\n"))


with open(srcfile) as f:
    for line in f:
        ismac=line.split()
        if not len(ismac) == 4:
            continue
        elif not len(ismac[1].split('.')) == 3:
            continue
        else:
            try:
                for i in ismac[1].split('.'):
                    int(i,16)
                print("{:5} {:15} {:15}".format(ismac[0],ismac[1],ismac[3]))
            except ValueError:
                print("ValueError\n")
                continue

