#!/usr/bin/env python3 
access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

mode=input('Enter mode:')
intf=input('Enter interface number:')
vlan=input('Enter vlan:')

#access_tmp="\n".join(access_template)
#trk_tmp="\n".join(trunk_template)

template={'access':access_template,'trunk':trunk_template}

print("interface " + intf + "\n" + "\n".join(template[mode]).format(vlan))

