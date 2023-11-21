import random


class Question:
    questions = []
    def __init__(self, questionsParm):
        self.id = questionsParm['id']
        self.chapter = questionsParm['chapter']
        self.difficulty = questionsParm['difficulty']
        self.objective = questionsParm['objective']
        Question.questions.append(self)

    def __str__(self):
        return f'{self.id}/{self.chapter}/{self.difficulty}/{self.objective}'

class Rate:
    questions = []
    def __init__(self,numQuest,exam_requirements):
        Rate.exam_requirements = exam_requirements
        self.rate  = {key:0 for key in Rate.exam_requirements}
        self.scores = {key:0 for key in Rate.exam_requirements}
        self.totalScore = 0
        self.questions = random.sample(Rate.questions,numQuest)
        self.calculateScore()


    def calculateScore(self):
        for question in self.questions:
            self.rate[question.chapter] +=  1
            self.rate[question.difficulty] +=  1
            self.rate[question.objective] +=  1
            
        self.totalScore = 0
        for key in self.rate.keys():
            self.scores[key] = abs(Rate.exam_requirements[key] - self.rate[key])
            self.totalScore += self.scores[key]

    def changeQuestions(self,newQuestions):
        self.questions = newQuestions
        self.rate  = {key:0 for key in Rate.exam_requirements}
        self.scores = {key:0 for key in Rate.exam_requirements}
        self.calculateScore()

    def getRealScore(self):
        realScore = {}
        for key in self.rate.keys():
            realScore[key] = Rate.exam_requirements[key] - self.rate[key]
        return realScore,self.rate,self.totalScore,self.questions
