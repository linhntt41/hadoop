#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from urlparse import urlparse
for line in sys.stdin:
    line = line.strip()
    first = line.find("\"")
    last = line.rfind("\"")
    if (first > 1 and last > 2):
        request = line[first+1:last]
        acUrl = request.split(" ")[1]
        key = re.sub(r"^http://www.the-associates.co.uk"
        print "{0}\t{1}".format(doc.path,1)
#for line in sys.stdin:
#    data = line.strip().split("GET")
#    if len(data) > 1:
#        key = data[0].split(" ")[0]
#        print "{0}\t{1}".format(key, 1)

