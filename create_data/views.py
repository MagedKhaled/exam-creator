from django.shortcuts import render

# Create your views here.


def create_data(request):
    if request.method == 'POST':
        print(request.POST)
    return(render(request,'create_data.html'))


def add_question(request):
    if request.method == 'POST':
        print(request.POST)
    return(render(request,'add_question.html'))
