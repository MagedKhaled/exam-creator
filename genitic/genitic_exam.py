import random
from time import time

from dataStructure import Tree,Node
from rateClasses import Question,Rate

number_questions = 100
exam_requirements = {'ch1':20,'ch2':17,'ch3':16,'ch4':20,'ch5':27,'d':45,'s':55,'r':40,'u':35,'c':25,}


def createQuestions():
    chapters = ['ch1','ch2','ch3','ch4','ch5']
    difficulty = ['d','s']
    objective = ['r','u','c']
    for i in range(1000):    
        question = Question({
            'ch':random.choice(chapters),
            'diff':random.choice(difficulty),
            'obj':random.choice(objective),
        })



def createTree():
    rate = Rate(random.sample(Question.questions, number_questions),exam_requirements)
    rootNode = Node(rate,rootNode=True)
    tree = Tree(rootNode)
    for i in range(100):
        rate = Rate(random.sample(Question.questions, number_questions),exam_requirements)
        node = Node(rate)
        tree.addNode(node)
    tree.sortTree()



    for i in range(200):
        tree.startInherit()
    tree.printTree()

    realSore,rate,totalScore = tree.rootNode.rate.getRealScore()


    print(realSore)
    print(rate)
    print(totalScore)


if __name__ == '__main__' :
    createQuestions()
    createTree()
