#!/usr/bin/env python3
addr=input('Enter the IP/Mask:')

address,mask=addr.split('/')
address=address.split('.')
bin_address='{:08b}{:08b}{:08b}{:08b}'.format(int(address[0]),int(address[1]),int(address[2]),int(address[3]))

mask=int(mask)

netaddr=(bin_address[0:mask]+'0'*(32-mask))
net_octets=[netaddr[0:8],netaddr[8:16],netaddr[16:24],netaddr[25::]]

bin_mask=('1'*mask + '0'*(32-mask))
mask_octets=[bin_mask[0:8],bin_mask[8:16],bin_mask[16:24],bin_mask[24::]]

print(netaddr)
print(bin_mask)
output_addr='''
Network:
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
'''
output_mask='''
Mask:
    /{0}
    {1:<8} {2:<8} {3:<8} {4:<8}
    {1:08b} {2:08b} {3:08b} {4:08b}

'''
#print(output.format(int(address[0]),int(address[1]),int(address[2]),int(address[3])))
#print(output.format(mask.count('1'),int(mask_octets[0],2),int(mask_octets[1],2),int(mask_octets[2],2),int(mask_octets[3],2)))
print(output_addr.format(int(net_octets[0],2),int(net_octets[1],2),int(net_octets[2],2),int(net_octets[3],2)))
print(output_mask.format(mask,int(mask_octets[0],2),int(mask_octets[1],2),int(mask_octets[2],2),int(mask_octets[3],2)))
