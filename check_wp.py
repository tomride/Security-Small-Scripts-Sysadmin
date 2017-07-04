#!/usr/bin/python

#Small Script to find Wordpress installations in Hosting Server (modify the path if necessary)
#and check and compare to current version of Wordpress to detect attack vector

import json
import urllib2
import os

path = "/var/www/vhosts/"
lstDir = os.walk(path)
lista=[]
lista2=[]
lista3=[]

url = "http://api.wordpress.org/core/version-check/1.7/"

datos = json.load(urllib2.urlopen(url))
ultima_estable = datos['offers'][0]['current']

def findingwp():
    for root, dirs, files in lstDir:
        if "version.php" in files and "wp-includes" in root:
            all = root+"/version.php"
            lista.append(all)

def checkwp():
    for ruta in lista:
        for line in open(ruta):
            if "wp_version ="  in line:
                if ultima_estable in line:
                    lista3.append(ruta) 
                else:
                    lista2.append(ruta)

def show():
    for k in lista2:
        print("Outdated Wordpress Installations:",k)

    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    for k in lista3:
        print("Updated Wordpress Installations:",k)

if __name__ == "__main__":
    findingwp()
    checkwp()
    show()





