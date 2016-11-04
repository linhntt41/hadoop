#!/usr/bin/python
import sys
import csv
from datetime import datetime

for line in sys.stdin:
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        date, time, place, item, price, card = line
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()    
        print weekday,'\t', price
