#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from urlparse import urlparse
for line in sys.stdin:
    data = line.strip().split("GET")
    if len(data) > 1:
        o = data[1].split(" ")[1]
        key = urlparse(o)
        print "{0}\t{1}".format(key.path, 1)

