#!/usr/bin/env python3 
"""
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
"""


f=open('ospf.txt')

for line in f:
    #input="O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
    #input=input.split()
    input=line.split()


    output = "\n{:25} {}" * 5

    print(output.format("Prefix:",input[1],
                        "AD/Metric",str(input[2]).strip("[]"),
                        "Next-Hop",str(input[4]).strip(','),
                        "Last update:",str(input[5]).strip(','),
                        "Outbound Interface:",input[6]))
f.close()


print('WITH')


with open('ospf.txt') as f:

	for line in f:
	    input=line.split()
	    output = "\n{:25} {}" * 5
	    print(output.format("Prefix:",input[1],
	                        "AD/Metric",str(input[2]).strip("[]"),
	                        "Next-Hop",str(input[4]).strip(','),
	                        "Last update:",str(input[5]).strip(','),
	                        "Outbound Interface:",input[6]))
