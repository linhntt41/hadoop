#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
keys = []
for line in reader:
    id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
    if node_type == "answer":
        keys  = abs_parent_id
    elif node_type == "question":
        keys = id
    print "{0}\t{1}\t{2}".format(keys, node_type,len(body))
        
        
