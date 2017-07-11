#!/usr/bin/env python

import os
import socket

#SIMPLE SCRIPT TO KNOCK PORTS FOR OPEN SSH server


ippaddress = raw_input("IP server to knock knock")
puertos = input("list of ports separated by commas:")


for x in puertos:
    try:
        conexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conexion.connect((ippaddress,x))
    except:
        print("ok")

print("Try to connect to server")
