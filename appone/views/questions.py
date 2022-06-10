from django.http import HttpResponse
from appone.models import Question, Choice
from django.template import loader
from django.shortcuts import redirect

def index(request):
    questions = Question.objects.order_by('-pub_date')[:25]
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

def vote(request, id):
    question = Question.objects.get(id=id)
    template = loader.get_template('questions/vote.html')
    
    context = {
        'question' : question
    }
    return HttpResponse(template.render(context, request))

def vote_post(request, id):
    choice = Choice.objects.get(pk = request.POST['choice_id'])
    choice.votes +=1
    choice.save()
    return redirect('questions_result', choice.question.id)

def result(request, id):
    question = Question.objects.get(id=id)
    template = loader.get_template('questions/result.html')
    
    context = {
        'question' : question
    }
    return HttpResponse(template.render(context, request))
