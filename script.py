#!/usr/bin/python

import bluetooth
import time
from subprocess import call

htc1m8 = '00:ee:bd:6a:64:ff'

print "In/Out Board"

def isThere(mac):
        return (bluetooth.lookup_name(mac, timeout=5) != None)

def canFind(mac):
        for i in range(0, 5):
                if(isThere(mac)):
                        return True


while True:
	print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
	if(canFind(htc1m8)):
		call(['echo',' hi'])	
	else:
		call(['./suspend.sh'])
    	time.sleep(60)

