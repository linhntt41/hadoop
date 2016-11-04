#!/usr/bin/python
import sys
import csv

#userinfo = None
#currentuserid = None
key_A = None
key_B = None

writer = csv.writer(sys.stdout, delimiter='\t')

for line in sys.stdin:
    data = line.strip().split("\t")

    if data[1] == "A":
        key_A = data[0]
        data_A = data[2:] 

    elif data[1] == "B":
        key_B = data[0]
        data_B = data[2:]
    if key_A == key_B:
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(data_B[0], data_B[1], data_B[2], key_B, data_B[3], data_B[4],data_B[5], data_B[6], data_B[7], data_A[0], data_A[1], data_A[2], data_A[3])
        
