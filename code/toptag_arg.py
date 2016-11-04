#!/usr/bin/python
import sys

topcount = [0] * 10
toptag = [0] * 10

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    thistag, thiscount = data
    min_count = min(topcount)
    min_index = topcount.index(min_count)
   
    if thiscount >= min_count:
        topcount[min_index] = thiscount
        toptag[min_index] = thistag
sort = sorted(range(len(topcount)), key = lambda k: topcount[k], reverse = True)
for i in range(0,10):
    print "{0}\t{1}".format(toptag[sort[i]],topcount[sort[i]])
