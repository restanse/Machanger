#! /usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
result = subprocess.call("ifconfig",shell=True)
print(result)

inter_input = str(raw_input("enter the required interface: "))

mac = str(raw_input("enter the desired mac address: "))

subprocess.call("ifconfig "+ inter_input +" down",shell=True)
subprocess.call("ifconfig "+ inter_input +" hw ether "+ mac ,shell=True)
subprocess.call("ifconfig "+ inter_input +" up",shell=True)
print("mac address "+ inter_input +" changed successfully")
print(result)







