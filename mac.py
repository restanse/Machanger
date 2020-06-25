#! /usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
result = subprocess.call("ifconfig",shell=True)
print(result)

inter_input = str(raw_input("enter the required interface: "))

mac = str(raw_input("enter the desired mac address: "))

if inter_input == "eth0":
	subprocess.call("ifconfig eth0 down",shell=True)
	subprocess.call("ifconfig eth0 hw ether "+ mac ,shell=True)
	subprocess.call("ifconfig eth0 up",shell=True)
	print("mac address eth0 changed successfully")
	print(result)

elif inter_input == "wlan0":
	subprocess.call("ifconfig wlan0 down",shell=True)
	subprocess.call("ifconfig wlan0 hw ether "+ mac ,shell=True)
	subprocess.call("ifconfig wlan0 up",shell=True)
	print("mac address wlan0 changed successfully")
	print(result)
	

elif inter_input == "wlan1":
	subprocess.call("ifconfig wlan1 down",shell=True)
	subprocess.call("ifconfig wlan1 hw ether "+ mac,shell=True)
	subprocess.call("ifconfig wlan1 up",shell=True)
	print("mac address wlan1 changed successfully")
	print(result)

else:
	print("invalid network interface name")






