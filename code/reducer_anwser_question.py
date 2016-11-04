#!/usr/bin/python
import sys

total_answers_length = 0
number_of_answers = 0
question_length = 0
last_question = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 3:
        continue
    question_id, note_type, body_len = data
    body_len = float(body_len)
    if last_question != None and last_question != question_id:
        if number_of_answers > 0:
            average_answer_length = total_answers_length / number_of_answers
        else:
            average_answer_length = 0

        print "{0}\t{1}\t{2}".format(last_question, question_length, average_answer_length)
        total_answers_length = 0
        number_of_answers = 0
        question_length = 0
    if  note_type == "answer":
        total_answers_length += body_len
        number_of_answers += 1
    elif note_type == "question":
        question_length += body_len
    last_question = question_id
if last_question != None:
    if number_of_answers > 0:
        average_answer_length = total_answers_length / number_of_answers
    else:
        average_answer_length = 0

    print "{0}\t{1}\t{2}".format(last_question, question_length, average_answer_length)
