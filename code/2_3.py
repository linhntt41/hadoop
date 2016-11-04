#!/usr/bin/python
import sys

for line in sys.stdin:
    if len(data) == 10:
    ip, id, user, datetime, timezone, method, path, proto, status, size = data
    fileName = path.split('/')[-1]
    print "{0}\t{1}".format(path,fileName)
