from django.shortcuts import render
from create_data.models import Subject,Chapter,Question,Choice
from django.http import JsonResponse
from genetic.genetic_exam import createQuestions, createTree

import random
from faker import Faker

def create_data(request):
    message = ''
    if request.method == 'POST':
        newSubject = Subject()
        newSubject.name = request.POST.get('subject_name')
        newSubject.save()
        for key, value in request.POST.items() :
            if key not in ['csrfmiddlewaretoken','subject_name'] :
                chapter = Chapter()
                chapter.name = value
                chapter.subject = newSubject
                chapter.save()
        message = 'Subject added successfully'
        
    return(render(request,'create_data.html',context={'message':message}))


def add_question(request):
    massage = ''
    subjects = Subject.objects.all()
    if request.method == 'POST':
        chapter = Chapter.objects.get(id=request.POST.get('chapter'))
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
            if key not in ['objective','difficulty','csrfmiddlewaretoken','question','chapter'] :
                answer = Choice()
                answer.state = 'f'
                answer.content = value
                answer.question = question
                answer.save()

        massage = 'Question added successfully'


    return(render(request,'add_question.html',context={'subjects':subjects,'massage':massage}))



def get_chapters(request,subjectID):
    if request.method == 'GET':
        chapters = Chapter.objects.filter(subject=subjectID)
        print(chapters)

        response_data = [{
            'id': chapter.id,
            'name': chapter.name
        } for chapter in chapters]

        return JsonResponse(response_data,safe=False)
    else:
        return JsonResponse({'message': 'Only GET requests are allowed for this endpoint.'}, status=405)



def create_exam(request):
    massage = ''
    subjects = Subject.objects.all()
    if request.method == 'POST':

        subject = Subject.objects.get(id=request.POST.get('subject'))
        chapters = subject.chapters.all()

        chaptersToSend = []
        for chp in chapters:
            chaptersToSend.append(str(chp.id))


        examData = {}

        for key in request.POST.keys():
            if key not in ['csrfmiddlewaretoken','subject','totalQuestions']:
                examData[key] = int(request.POST.get(key))

        questions = Question.objects.filter(chapter__subject = subject)
        questionsStates = {key:[0,0,0] for key in examData}

        for question in questions:
            questionsStates[question.difficulty][0] += 1
            questionsStates[question.objective][0] += 1
            questionsStates[str(question.chapter.id)][0] += 1

        createQuestions(questions,chaptersToSend)
        realScore,rate,totalScore,questions = createTree(int(request.POST.get('totalQuestions')),examData,number_nodes=100,number_inherit=200)
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


        return(render(request,'exam.html',context={'questions':questionData,'score':totalScore,'question_states':questionsStates}))
        
    return(render(request,'create_exam.html',context={'subjects':subjects}))


def createRandomQuestions(request):
    fake = Faker()
    difficulty = ['d','s']
    objective = ['r','u','c']

    chapter = Chapter.objects.all()
    for i in range(10):
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