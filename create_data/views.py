from django.shortcuts import render
from create_data.models import Subject,Chapter,Question,Choice
from django.http import JsonResponse



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
