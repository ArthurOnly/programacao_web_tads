from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader

def home(request):
    users = User.objects.order_by('id')
    template = loader.get_template('home.html')
    
    context = {
        'users' : users
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Arthur Medeiros Paiva 20211014040004")