class Question:
    questions = []
    def __init__(self, param):
        self.id = len(Question.questions)
        self.chapter = param['ch']
        self.difficulty = param['diff']
        self.objective = param['obj']
        Question.questions.append(self)

    def __str__(self):
        return f'{self.id}/{self.chapter}/{self.difficulty}/{self.objective}'

class Rate:
    
    def __init__(self,questions,exam_requirements):
        Rate.exam_requirements = exam_requirements
        self.rate  = {'ch1':0,'ch2':0,'ch3':0,'ch4':0,'ch5':0,'d':0,'s':0,'r':0,'u':0,'c':0,}
        self.scores = {'ch1':0,'ch2':0,'ch3':0,'ch4':0,'ch5':0,'d':0,'s':0,'r':0,'u':0,'c':0,}
        self.totalScore = 0
        self.questions = questions
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
        self.rate  = {'ch1':0,'ch2':0,'ch3':0,'ch4':0,'ch5':0,'d':0,'s':0,'r':0,'u':0,'c':0,}
        self.scores = {'ch1':0,'ch2':0,'ch3':0,'ch4':0,'ch5':0,'d':0,'s':0,'r':0,'u':0,'c':0,}
        self.calculateScore()

    def getRealScore(self):
        realScore = {}
        for key in self.rate.keys():
            realScore[key] = Rate.exam_requirements[key] - self.rate[key]
        return realScore,self.rate,self.totalScore
