#!/usr/bin/bash

ifconfig

echo "enter the required interface: "
read inter 

echo "enter the desired mac address: "
read mac


ifconfig $inter down
ifconfig $inter hw ether $mac 
ifconfig $inter up

echo "mac adress changed successfully"