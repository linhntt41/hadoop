#!/usr/bin/python
import sys


#topTag=[0]*10
count = 0
oldTag = None
for line in sys.stdin:
    data=line.strip().split('\t')
    if len(data) != 2:
        continue
	
    thisTag,thisnode = data
    if oldTag and oldTag != thisTag:
        print oldTag,"\t", count
    oldTag = thisTag
    count += 1
if oldTag != None:
    print oldTag,"\t", count

