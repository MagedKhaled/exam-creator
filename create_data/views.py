from django.shortcuts import render,redirect
from create_data.models import Subject,Chapter,Question,Choice
from django.http import JsonResponse
from genetic.genetic_exam import createQuestions, createTree
from django.urls import reverse_lazy


import random
import json
from faker import Faker


trees = {}



def create_data(request):
    message = ''
    if request.method == 'POST':
        newSubject = Subject()
        newSubject.name = request.POST.get('subject_name')
        if not request.POST.get('subject_name'):
            message = 'subject name is required'
            return(render(request,'create_data.html',context={'message':message}))
        newSubject.save()
        
        for key, value in request.POST.items() :
            if key not in ['csrfmiddlewaretoken','subject_name'] :
                if not value  :
                    break

                chapter = Chapter()
                chapter.name = value
                chapter.subject = newSubject
                chapter.save()
        message = 'Subject added successfully'
        
    return(render(request,'create_data.html',context={'message':message}))


def add_question(request):
    message = ''
    subjects = Subject.objects.all()
    if request.method == 'POST':
        chapter = Chapter.objects.get(id=request.POST.get('chapter'))
        if not request.POST.get('question'):
            message = 'Question is required'
            return(render(request,'add_question.html',context={'subjects':subjects,'massage':message}))
        
        question = Question()
        question.content = request.POST.get('question')
        question.difficulty = request.POST.get('difficulty')
        question.objective = request.POST.get('objective')
        question.chapter = chapter
        question.save()

        answer = Choice()
        answer.state = 't'
        answer.content = request.POST.get('true_answer')
        answer.question = question

        answer.save()


        for key,value in request.POST.items():
            if key not in ['objective','difficulty','csrfmiddlewaretoken','question','chapter','subject','true_answer'] :
                if request.POST.get('question'):
                    answer = Choice()
                    answer.state = 'f'
                    answer.content = value
                    answer.question = question
                    answer.save()

        message = 'Question added successfully'


    return(render(request,'add_question.html',context={'subjects':subjects,'massage':message}))



def get_chapters(request,subjectID):
    if request.method == 'GET':
        chapters = Chapter.objects.filter(subject=subjectID)
        response_data = [{
            'id': chapter.id,
            'name': chapter.name
        } for chapter in chapters]

        return JsonResponse(response_data,safe=False)
    else:
        return JsonResponse({'message': 'Invalid Method.'}, status=405)



def create_exam(request):
    message = ''
    subjects = Subject.objects.all()
    if request.method == 'POST':

        subject = Subject.objects.get(id=request.POST.get('subject'))
        chapters = subject.chapters.all()

        chaptersToSend = []
        for chp in chapters:
            if (int(request.POST.get(str(chp.id)))) > 0:

                chaptersToSend.append(chp.id)


        examData = {}

        for key in request.POST.keys():
            if key not in ['csrfmiddlewaretoken','subject','totalQuestions']:
                try:
                    examData[key] = int(request.POST.get(key))
                except:
                    message = 'invalid datatype'
                    return(render(request,'create_exam.html',context={'subjects':subjects,'message':message}))
        difficulty = []
        if int(request.POST.get('s'))>0:
            difficulty.append('s')
        if int(request.POST.get('d'))>0:
            difficulty.append('d')

        objective = []
        if int(request.POST.get('r'))>0:
            objective.append('r')
        if int(request.POST.get('u'))>0:
            objective.append('u')
        if int(request.POST.get('c'))>0:
            objective.append('c')
        

        chapters_ids = list(map(int, chaptersToSend))
        questions = Question.objects.filter(chapter__subject=subject, chapter__in=chapters_ids,objective__in=objective,difficulty__in=difficulty)
        
        questionsStates = {key:[0,0,0] for key in examData}

        for question in questions:
            questionsStates[question.difficulty][0] += 1
            questionsStates[question.objective][0] += 1
            questionsStates[str(question.chapter.id)][0] += 1


        try:
            totalQuestions = int(request.POST.get('totalQuestions'))
        except:
            message = 'invalid datatype'
            return(render(request,'create_exam.html',context={'subjects':subjects,'message':message}))
        
        if len(questions) < totalQuestions :
            message = f'The Server has {len(questions)} questions for this subject, please add more questions'
            return(render(request,'create_exam.html',context={'subjects':subjects,'message':message}))

        createQuestions(questions,chaptersToSend)
        realScore,rate,totalScore,questions,tree = createTree(totalQuestions,examData,number_nodes=100,number_inherit=200)

        questionData = []
        for question in questions:
            quest = Question.objects.get(id=question.id)
            choices = list(quest.Choices.all())
            random.shuffle(choices)
            questionData.append(
                [quest,choices]
                )

        
        for key in questionsStates.keys():
            questionsStates[key][1] = rate[key]
            questionsStates[key][2] = examData[key]

        treeIndex = len(trees)
        print(treeIndex)

        trees[treeIndex] = [tree,questionsStates,examData]

        return(render(request,'exam.html',context={'questions':questionData,'score':totalScore,'question_states':questionsStates,'treeIndex':treeIndex}))
        
    return(render(request,'create_exam.html',context={'subjects':subjects,'message':message}))


def createRandomQuestions(request):
    fake = Faker()
    difficulty = ['d','s']
    objective = ['r','u','c']

    chapter = Chapter.objects.all()
    for i in range(10000):
        question = Question()
        question.content = fake.text(150)
        question.difficulty = random.choice(difficulty)
        question.objective = random.choice(objective)
        question.chapter = random.choice(chapter)
        question.save()

        answer = Choice()
        answer.state = 't'
        answer.content = fake.text(50)
        answer.question = question

        answer.save()


        for i in range(3):
            answer = Choice()
            answer.state = 'f'
            answer.content = fake.text(50)
            answer.question = question
            answer.save()

    questions = Question.objects.all()
    return(render(request,'create_random_questions.html',context={'questions':questions}))



def retryExamGenerate(request):

    if request.method == 'POST':
        treeIndex = int(request.POST.get('treeIndex'))
        try:
            tree = trees[treeIndex][0]
            examData = trees[treeIndex][2]
            questionsStates = trees[treeIndex][1]
        except:
            return(redirect(''))
        

        tree.startInherit(200)
        trees[treeIndex] = [tree,questionsStates,examData]
        print(treeIndex)


        realScore,rate,totalScore,questions = tree.rootNode.rate.getRealScore()

        questionData = []
        for question in questions:
            quest = Question.objects.get(id=question.id)
            choices = list(quest.Choices.all())
            random.shuffle(choices)
            questionData.append(
                [quest,choices]
                )
        
        for key in questionsStates.keys():
            questionsStates[key][1] = rate[key]
            questionsStates[key][2] = examData[key]


    
        return(render(request,'exam.html',context={'questions':questionData,'score':totalScore,'question_states':questionsStates,'treeIndex':treeIndex}))
    return(redirect('/'))