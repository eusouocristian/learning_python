import datetime
import random
import time

from questions import Add, Multiply

class Quiz:
    questions = []
    answers = []
    right_answers = []
    total_correct = 0
    total_wrong = 0

    def __init__(self):
        question_types = (Add, Multiply)
        
        # generate 10 random questions from numbers from 1 to 10
        for _ in range(10):
            random_num1 = random.randint(1, 10)
            random_num2 = random.randint(1, 10)
            question = random.choice(question_types)(random_num1, random_num2) # aqui a magica acontece
            # add questions into self.questions
            self.questions.append(question)


    def take_quiz(self):
        print('You Have 10 math-based questions to answer...')
        time.sleep(4)
        flag = input('Are you ready?? Press Any buttom to continue. :) [...]')         
        
        self.start_time = datetime.datetime.now()
        print(self.start_time.strftime('Quiz started at: %H:%M:%S\n'))

        for index in range(len(self.questions)):

            answer = int(input('{}  = '.format(self.questions[index].text)))
            self.answers.append(answer)

            if self.answers[index] == self.questions[index].answer:
                self.total_correct +=1
            else:
                self.total_wrong += 1

        # print the end time        
        self.end_time = datetime.datetime.now()
        print(self.end_time.strftime('Quiz ended at: %H:%M:%S\n'))
        return self.summary()

    def ask(self, question):
        pass
        # log the start time
        # capture the answer
        # check the answer
        # log the endtime
        # If the answer is right, send back 'True'
        # If the answer is wrong, send 'False'
        # Send back the elapse time


    def summary(self):
        print('You got {}% right'.format(100*self.total_correct/len(self.questions)))
        print('You took {} seconds to do that!'.format(
            (self.end_time-self.start_time).seconds
        ))
        print('Your intelligence index is {}\n'.format(
            100*self.total_correct/(self.end_time-self.start_time).seconds
        ))

        # show how many questions you got right
        # print the total time for the quiz


Quiz().take_quiz()
# pyinstaller quiz.py

