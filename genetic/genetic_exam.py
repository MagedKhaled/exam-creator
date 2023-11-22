import random
from time import time

from genetic.dataStructure import Tree,Node,Rate,Question



def createQuestions(questions,chapters):
    Question.questions = []
    difficulty = ['difficult','simple']
    objective = ['reminding','understanding','creative']
    for question in questions:    
        # Question({
        #     'id':i,
        #     'chapter':random.choice(chapters),
        #     'difficulty':random.choice(difficulty),
        #     'objective':random.choice(objective),
        # })
        Question({
            'id': str(question.id),
            'chapter': str(question.chapter.id),
            'difficulty':question.difficulty,
            'objective': question.objective,
        })



    Rate.questions = Question.questions



def createTree(number_questions,exam_requirements,number_nodes=100,number_inherit=200):
    
    tree = Tree(exam_requirements,number_nodes,number_questions)
    tree.startInherit(number_inherit)
    x,y,z,u = tree.rootNode.rate.getRealScore()
    return x,y,z,u,tree

    


if __name__ == '__main__' :
    number_questions = 100
    exam_requirements = {'ch1':20,'ch2':17,'ch3':16,'ch4':20,'ch5':27,'difficult':45,'simple':55,'reminding':40,'understanding':35,'creative':25,}

    chapters = ['ch1','ch2','ch3','ch4','ch5']
    createQuestions(range(1000),chapters)
    x,y,z,u = createTree(number_questions,exam_requirements,number_nodes=100,number_inherit=200)

    print(x)
    print(y)
    print(z)
    print(u)
