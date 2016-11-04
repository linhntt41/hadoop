#!/usr/bin/python
import sys

count_hour = [0]*24
oldAuthor = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    thisAuthor, thisHour = data
    if oldAuthor and oldAuthor != thisAuthor:
        for hour, count in enumerate(count_hour):
            if count == max(count_hour):
                print oldAuthor,"\t",hour
        count_hour = [0]*24
    oldAuthor = thisAuthor
    active_hour = int(thisHour.split(" ")[1][0:2])
    count_hour[active_hour] += 1
    #count_hour[int(thisHour)] += 1
if oldAuthor != None:
    for hour, count in enumerate(count_hour):
        if count == max(count_hour):
            print oldAuthor,"\t",hour
    
