from django.db import models



class Subject(models.Model):
    name = models.CharField(max_length=50)
    

class Chapter(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters')




class Question(models.Model):
    DIFF_CHOICES = (
        ('d','difficult'),
        ('s','simple'),
        )
    
    OBJ_CHOICES = (
        ('r','reminding'),
        ('u','understanding'),
        ('c','creativity'),
        )
    
    content = models.CharField(max_length=1000)
    difficulty = models.CharField(max_length = 1, choices=DIFF_CHOICES)
    objective = models.CharField(max_length = 1, choices = OBJ_CHOICES)

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='Questions')



class Choice(models.Model):
    STATE_CHOICES = (
        ('t','true'),
        ('f','false'),
        )
    
    content = models.CharField(max_length=1000)
    state = models.CharField(max_length = 1, choices = STATE_CHOICES)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='Choices')


