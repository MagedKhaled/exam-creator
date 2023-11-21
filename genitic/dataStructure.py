import random
number_questions = 100

from rateClasses import Question


class Node:
    def __init__(self,rate,rootNode=False) -> None:
        self.childL = None
        self.childR = None
        self.sibling = None
        self.parent = None
        self.rootNode = rootNode
        self.rate = rate
        self.level = 0
        

    def addChild(self,child):
        child.level = self.level+1
        child.parent = self
        
        if not self.childL :
            self.childL = child
            return True
        
        elif not self.childR :
            child.sibling = self.childL
            self.childL.sibling = child
            self.childR = child
            
            return False
        
        else:
            raise('error on construction')


    def printMe(self):
        print('\t'*self.level,self.rate.totalScore)

    def startInherit(self,node):
        gen1 = random.sample(self.rate.questions,int(number_questions/2))
        gen2 = random.sample(node.rate.questions,int(number_questions/2))
        newGen = list(set(gen1+gen2))
        difference = number_questions - len(newGen)
        while difference > 0:
            subGen = random.sample(Question.questions,difference)
            newGen = list(set(newGen+subGen))
            difference = number_questions - len(newGen)

        self.rate.changeQuestions(newGen)
        
            
        
        


class Tree:
    def __init__(self,rootNode) -> None:
        self.rootNode = rootNode
        self.lastNodes = [self.rootNode]
        self.maxLevel = 0
        

    def addNode(self,node):
        isAdded = self.lastNodes[0].addChild(node)
        if not isAdded :
            self.lastNodes.pop(0)
        self.lastNodes.append(node)
        self.maxLevel = node.level

    def printTree(self):
        self.printNode(self.rootNode)

    def printNode(self,node):
        node.printMe()
        if node.childL:
            self.printNode(node.childL)

        if node.childR:
            self.printNode(node.childR)

    def sortTree(self):
        for node in self.lastNodes:
            self.sortNode(node)
            

    def sortNode(self,node):
        

        if node.rate.totalScore < node.parent.rate.totalScore:
            self.switchNodes(node,node.parent)
        
        if not node.parent.rootNode:
            self.sortNode(node.parent)
            
            
                

    def switchNodes(self,node1,node2):
        switcher = node1.rate
        node1.rate = node2.rate
        node2.rate = switcher


    def startInherit(self):
        self.makeNodeInherit(self.rootNode)
        self.sortTree()

    def makeNodeInherit(self,node):
        if node.childL :
            node.childL.startInherit(self.rootNode)
            self.makeNodeInherit(node.childL)
            
        if node.childR :
            node.childR.startInherit(self.rootNode)
            self.makeNodeInherit(node.childR)
            