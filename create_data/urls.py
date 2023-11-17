from django.urls import path
from create_data.views import create_data, add_question

urlpatterns = [
    path('subject/',create_data,name='create.subject'),
    path('question/',add_question,name='create.question'),
]