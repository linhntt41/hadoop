#!/usr/bin/python
import sys, csv, re
reader = csv.reader(sys.stdin, delimiter = '\t')
for line in reader:
    body = line[4]
        node_id = line[0]
	    parts = re.split(r'\s|[.!?:;"()<>[\]#$=\-/,]', body)
	        for word in parts:
		        print "{0}\t{1}".format(word.lower(), node_id)
