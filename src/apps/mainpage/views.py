from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

def index(request):
    context = {
        'text': "Hi noone",
    }
    if request.user.is_authenticated:
        context = {
            'user': request.user,
            'text': "Hi " + request.user.username + " ",
        }
    return HttpResponse(render(request, 'mainpage/index.html', context))

