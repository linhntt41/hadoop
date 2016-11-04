#!/usr/bin/python

import sys
import csv

count = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
	
    thisKey, thisValue = data_mapped
	
    if thisKey == "fantastically":
        print thisKey, "\t", thisValue
    oldKey = thisKey	
#    if oldKey and oldKey != thisKey:
#        print oldKey, "\t", count
#        oldKey = thisKey
#        count = 0
#    oldKey = thisKey
#    count += 1
#       if thisKey = "fantastically":
#           print thisKey, "\t", thisValue
#        oldKey = thisKey
#     oldKey = thisKey
	
if oldKey != None:
    print oldKey
