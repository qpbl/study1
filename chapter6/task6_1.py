#!/usr/bin/env python3
address=input("Enter IP address: ")
address=address.split('.')
flag=True
for i in address:
    if i.isdigit():
        if int(i) < 256:
            continue
        else:
            print("Wrong input")
            flag=False
            break
    else:
        print('Wrong input')
        flag=False
        break

if flag:
    if '.'.join(address) == '0.0.0.0':
        print("unassigned")
    elif '.'.join(address) == '255.255.255.255':
        print("local broadcast")
    elif int(address[0]) < 128:
        print("Class A")
    elif int(address[0]) < 192:
        print("Class B")
    elif int(address[0]) < 224:
        print("Class C")
    elif int(address[0]) < 240:
        print("Multicast")
    else:
        print("Unused")
else:
    print("Smth went wrong")


