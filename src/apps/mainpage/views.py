from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm

def index(request):
    context = {
        'text': "Hi bitch",
    }
    return HttpResponse(render(request, 'mainpage/index.html', context))

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            context = {
                'text': "loged_in",
            }
            return HttpResponse(render(request, 'mainpage/index.html', context))
        else:
            print('BAD VALUES PASSED')
    else:
        context = {
            'form' : LoginForm(),
        }
        return HttpResponse(render(request, 'login/login.html', context))

def register(request):
    context = {
        'form' : LoginForm(),
    }

    return HttpResponse(render(request, 'login/register.html', context))