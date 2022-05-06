from django.http import HttpResponse

def sign_in(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sign_up(request):
    return HttpResponse("Sign up screen")