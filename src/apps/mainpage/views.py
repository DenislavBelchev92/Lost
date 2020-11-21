from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'text': "Hi bitch",
    }
    return HttpResponse(render(request, 'mainpage/index.html', context))

def login(request):
    context = {
        'login_page': "TRUE",

    }
    return HttpResponse(render(request, 'login/login.html', context))

def register(request):
    context = {
        'register_page': "TRUE",
    }

    return HttpResponse(render(request, 'login/register.html', context))