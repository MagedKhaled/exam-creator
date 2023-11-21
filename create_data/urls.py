from django.urls import path
from create_data.views import create_data, add_question,get_chapters,create_exam,createRandomQuestions

urlpatterns = [
    path('subject/',create_data,name='create.subject'),
    path('question/',add_question,name='create.question'),
    path('exam/',create_exam,name='create.exam'),
    path('random/questions/',createRandomQuestions,name='create.random.questions'),
    path('get/chapters/<subjectID>/',get_chapters,name='create.get.chapters'),
]