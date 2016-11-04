#!/usr/bin/python

import sys

#countTotal = 0
#oldKey = None
most_path = None
most_path_count = 0
cur_path = None
cur_path_count = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    path = line.strip().split("\t")
    if len(path) != 2:
        # Something has gone wrong. Skip this line.
        continue
    if cur_path and cur_path != path:
        if cur_path_count > most_path_count:
            most_path = cur_path
            most_path_count = cur_path_count
        cur_path_count = 0
#    if oldKey and oldKey != thisKey:
#        print oldKey, "\t", countTotal
#        oldKey = thisKey;
#        countTotal = 0

 #   oldKey = thisKey
 #   countTotal += int(thisCount)
    cur_path = path
    cur_path_count += 1
#if oldKey != None:
#    print oldKey, "\t", countTotal
print "{0}\t{1}".format(most_path,most_path_count)
