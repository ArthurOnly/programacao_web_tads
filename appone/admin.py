from django.contrib import admin
from appone.models import Question, Choice

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
    pass