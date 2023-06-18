import json

class QuestionSet:

    def __init__(self):
        self.set_filename="question_set.json"
        self.question_filename="questions.txt"
        self.answer_filename="answers.txt"
    
    def upload_questions_answer_file(self):
        question_set={}
        question_lst=[]
        answer_lst=[]
        qf=open(self.question_filename,'r')
        af=open(self.answer_filename,'r')
        for question in qf.readlines():
            question=question.split('\n')[0]
            question_lst.append(question)

        for answer in af.readlines():
            answer=answer.split('\n')[0]
            answer_lst.append(answer)

        for i in range(0,len(question_lst)):
            temp={answer_lst[i]:question_lst[i]}
            question_set.update(temp)
        
        return question_set

    def insert_question_answer(self,question_set):
        question_file_read=open(self.set_filename,'r')
        question_file_json=question_file_read.read()
        question_file_dict=json.loads(question_file_json)
        question_file_dict={}
        question_file_dict.update(question_set)
        question_file_read=open('question_set.json','w')
        question_file_new_json=json.dumps(question_file_dict)
        question_file_read.write(question_file_new_json)
        question_file_read.close()

    def get_question_set(self):
        question_file_read=open(self.set_filename,'r')
        question_file_json=question_file_read.read()
        question_file_dict=json.loads(question_file_json)
        return question_file_dict