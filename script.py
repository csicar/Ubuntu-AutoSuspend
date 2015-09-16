#!/usr/bin/python

import bluetooth
import time
from subprocess import call
import sys

mac = sys.argv[0] 

print "In/Out Board"

def isThere(mac):
        return (bluetooth.lookup_name(mac, timeout=5) != None)

def canFind(mac):
        for i in range(0, 5):
                if(isThere(mac)):
                        return True


while True:
	print "Time: " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
	if(canFind(mac)):
		call(['./away.sh'])	
	else:
		call(['./there.sh'])
    	time.sleep(60)

