#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
tags = []
for line in reader:
    id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
    if node_type == "answer":
        tags = tagnames.split()
    for tag in tags:
        print tag
        
        
