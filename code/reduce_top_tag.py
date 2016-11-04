#!/usr/bin/python
import sys
import csv
import collections

tagq = collections.deafaultdict(list)
taga = collections.deafaultdict(list)
tq = 0
ta = 0
#count = 0
oldkey = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    thistag, thisnode = data
    if oldTag and oldTag != thistag:
        tagq[tq].append(oldTag)
        tagq[ta].append(oldTag)
        tq =0
        ta = 0
   oldTag = thistag
   if (thisnode == 'question' or thisnode == 'answer'):
       

