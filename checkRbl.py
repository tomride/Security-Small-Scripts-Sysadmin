#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python2.x
# Script to check a list of servers in most
# Important RBL sites to rule them all


import dns.resolver
import sys
slist = ["SERVER LIST TO CHECK"]

bls = ["zen.spamhaus.org", "spam.abuse.ch", "cbl.abuseat.org", "virbl.dnsbl.bit.nl", "dnsbl.inps.de",
    "ix.dnsbl.manitu.net", "dnsbl.sorbs.net", "bl.spamcop.net",
    "xbl.spamhaus.org", "pbl.spamhaus.org", "dnsbl-1.uceprotect.net", "dnsbl-2.uceprotect.net",
    "dnsbl-3.uceprotect.net", "db.wpbl.info", "all.s5h.net","bogons.cymru.com","combined.abuse.ch","dnsbl.cyberlogic.net", "duinv.aupads.org",
    "dynip.rothen.com"]

for i in slist:
    for bl in bls:
        try:
  	    my_resolver = dns.resolver.Resolver()
	    query = '.'.join(reversed(str(i).split("."))) + "." + bl
            answers = my_resolver.query(query, "A")
	    answer_txt = my_resolver.query(query, "TXT")
            print ("IP: %s IS listed in %s (%s: %s)" %(i, bl, answers[0], answer_txt[0]))
	except dns.resolver.NXDOMAIN:
            print ("IP: %s is NOT listed in %s" %(i, bl))
