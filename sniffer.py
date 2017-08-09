#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import argparse
from scapy.all import *
ap_list = []
pb_list = []

def PacketHandler(pkt) :
    if pkt.haslayer(Dot11) :
        if pkt.type == 0 and pkt.subtype == 8 :
	    if pkt.addr2 not in ap_list :
	        ap_list.append(pkt.addr2)
		print "AP MAC: %s with SSID: %s " %(pkt.addr2, pkt.info)

def PacketHandler2(pkt) :
    if pkt.haslayer(Dot11) :
        if pkt.type == 0 and pkt.subtype == 4 :
            if pkt.addr2 not in pb_list :
                pb_list.append(pkt.addr2)
                print "Transmissor Address: %s with SSID: %s " %(pkt.addr2, pkt.info)

def PacketHandler3(pkt) :
    if pkt.haslayer(Dot11Deauth) :
        #print pkt.sprinf("Deauth from AP [%Dot11.addr2%] Client [%Dot11.addr1%], Reason [%Dot11Deauth.reason%]")
        print "Deauth FROM AP: %s  Client %s Reason %s" %(pkt.addr2, pkt.addr1, pkt.reason)

parser = argparse.ArgumentParser()
parser.add_argument("-ap", "--ap", help="Detect AP")
parser.add_argument("-pb", "--pb", help="Detect Probe Request")
parser.add_argument("-pa", "--pa", help="Detect Deauth")
args = parser.parse_args()


if args.ap:
    sniff(iface="mon0", prn = PacketHandler)  

if args.pb:
    sniff(iface="mon0", prn = PacketHandler2)

if args.pa:
    sniff(iface="mon0", prn = PacketHandler3)
