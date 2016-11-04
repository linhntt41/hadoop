#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')

total = 0
tag_dict = {}

for line in reader:
    node_type = line[5]
    if node_type == "question":
        tagnames = line[2]
        tag_name = tagnames.split()
        for tag in tag_name:
            if tag not in tag_dict:
                tag_dict[tag] = 1
            else:
                tag_dict[tag] += 1
for tag in tag_dict:
    print "{0}\t{1}".format(tag,tag_dict[tag])
