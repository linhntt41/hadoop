#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
for line in reader:
    node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
    node_type = line[5]
    tags = tag_names.split()
    for tag in tags:
        print tag, "\t", node_type
