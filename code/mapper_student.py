#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')

for line in reader:
    author_id = line[3]
    added_add = line [8]
    print "{0}\t{1}".format(author_id, added_add)
