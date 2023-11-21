from django.contrib import admin
from create_data.models import Subject,Chapter,Question,Choice
# Register your models here.

admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Question)
admin.site.register(Choice)