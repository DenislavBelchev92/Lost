from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'text': "Hi bitch",
    }
    return HttpResponse(render(request, 'mainpage/index.html', context))