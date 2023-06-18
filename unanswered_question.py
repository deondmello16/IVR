#Importing Json To convert and read json

import json

#Used to split words in a question and return it in a string

def split_question(question):
    return question.split(' ')

#Used to insert all the list questions and Write it in Json file

def insert_question(question_lst):
    f=open('unanswered_questions.json','r')
    question_set_json = f.read()
    question_set_python = json.loads(question_set_json)
    question_set_python.append(question_lst)
    f=open("unanswered_question",'w')
    question_set_json=json.dumps(question_set_python)
    f.write(question_set_json)
    f.close()

#used to read the json file and print it

def find_all():
    f=open("unanswered_questions.json",'r')
    question_json = f.read()
    question_set_python = json.loads(question_json)
    for question in question_set_python:
        print(question)
    f.close()
