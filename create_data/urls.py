from django.urls import path
from create_data.views import create_data, add_question,get_chapters

urlpatterns = [
    path('subject/',create_data,name='create.subject'),
    path('question/',add_question,name='create.question'),
    path('get/chapters/<subjectID>/',get_chapters,name='create.question'),
]