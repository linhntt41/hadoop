#!/usr/bin/python
import sys
import collections

sales = collections.defaultdict(list)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    sales[int(thisKey)].append(float(thisSale))

for k in sales:
    print k, "\t", sum(sales[k])
