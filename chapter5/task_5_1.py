#!/usr/bin/env python3
addr=input('Enter the IP/Mask:')
address,mask=addr.split('/')
address=address.split('.')
#mask=int(mask)

mask=('1'*int(mask) + '0'*(32-int(mask)))
mask_octets=[mask[0:8],mask[8:16],mask[16:24],mask[25::]]

output='''
Network:
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
Mask:
    /{4}
    {5:<8} {6:<8} {7:<8} {8:<8}
    {5:08b} {6:08b} {7:08b} {8:08b}

'''
#print(output.format(int(address[0]),int(address[1]),int(address[2]),int(address[3])))
#print(output.format(mask.count('1'),int(mask_octets[0],2),int(mask_octets[1],2),int(mask_octets[2],2),int(mask_octets[3],2)))
print(output.format(int(address[0]),int(address[1]),int(address[2]),int(address[3]),mask.count('1'),int(mask_octets[0],2),int(mask_octets[1],2),int(mask_octets[2],2),int(mask_octets[3],2)))
