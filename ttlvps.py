#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Using IP Header TTL for search virtual Server on a Hardware Node (venet0)
# Incomplete for adjust
# https://openvz.org/Virtual_network_device


from scapy.all import *

hnn = input("Hardware Node to check:")
vps = input("Range to analyze")
rg =[]
hosted=[]
for k in range(80,100):
    v = vps+str(k)
    rg.append(v)


for k in rg:
    for i in range(1, 28):
        pkt = IP(dst=k, ttl=i) / UDP(dport=33434)
        # Send the packet and get a reply
        reply = sr1(pkt, verbose=0)
        if reply is None:
            # No reply =(
            break
        elif reply.type == 3:
            # We've reached our destination
            print ("Done!", reply.src)
            break
        elif reply.src == hnn and reply.type == 11:
            print ("Hosted in node")
            hosted.append(k)
        elif reply.type == 11:
            # We're in the middle somewhere
            print ("%d hops away: " % i , reply.src)


for j in hosted:
    print ("VPS hosted",j)
