#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python2.x
# Script to check a list of servers in most
# Important RBL sites to rule them all
# Require changes, mail authentication for notifications


import dns.resolver
import sys
import smtplib

slist=[""]
blist=[]


bls = ["zen.spamhaus.org", "spam.abuse.ch", "cbl.abuseat.org", "virbl.dnsbl.bit.nl", "dnsbl.inps.de",
    "ix.dnsbl.manitu.net", "dnsbl.sorbs.net", "bl.spamcop.net",
    "xbl.spamhaus.org", "pbl.spamhaus.org", "dnsbl-1.uceprotect.net", "psbl.surriel.com", "dnsbl-2.uceprotect.net",
    "dnsbl-3.uceprotect.net", "db.wpbl.info", "all.s5h.net","bogons.cymru.com","combined.abuse.ch",
    "dnsbl.spfbl.net", "dnsbl.cyberlogic.net", "duinv.aupads.org","dynip.rothen.com"]



def main():

    for i in slist:
        for bl in bls:
            try:
  	        my_resolver = dns.resolver.Resolver()
    	        query = '.'.join(reversed(str(i).split("."))) + "." + bl
                answers = my_resolver.query(query, "A")
	        answer_txt = my_resolver.query(query, "TXT")
                notification(i,bl,answers[0],answer_txt[0])
       	    except dns.resolver.NXDOMAIN:
                print ("IP: %s is NOT listed in %s" %(i, bl))


def notification(i,bl,answer,atxt):
    sender = "email"
    receivers = "email"
    subject = "Server IP listed:%s" %i
    text = 'Server %s IS listed in %s (%s: %s)' %(i,bl,answer,atxt)
    message = string.join((
	"From: %s" % sender,
        "To: %s" % receivers,
        "Subject: %s" % subject ,
        "",
        text
        ), "\r\n")
    server = smtplib.SMTP('server_ip_address',port)
    server.login("email","password")
    server.sendmail(sender, receivers, message)         
    server.quit()

if __name__ == "__main__":
    main()
