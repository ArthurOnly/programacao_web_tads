from django.http import HttpResponse
from appone.models import Question
from django.template import loader

def index(request):
    questions = Question.objects.order_by('id')
    template = loader.get_template('questions/index.html')
    
    context = {
        'questions' : questions
    }
    return HttpResponse(template.render(context, request))

def show(request, id):
    question = Question.objects.get(id=id)
    template = loader.get_template('questions/show.html')
    
    context = {
        'question' : question
    }
    return HttpResponse(template.render(context, request))