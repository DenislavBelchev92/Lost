from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            context = {
                'text': "loged_in " + username,
            }
            return HttpResponse(render(request, 'mainpage/index.html', context))
        else:
            context = {
                'form' : form,
            }
            return HttpResponse(render(request, 'access/login.html', context))
    else:
        context = {
            'form' : LoginForm(),
        }
        return HttpResponse(render(request, 'access/login.html', context))

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            context = {
                'text': "loged_in",
            }
            return HttpResponse(render(request, 'access/register.html', context))
        else:
            context = {
                'form' : form,
            }
            return HttpResponse(render(request, 'access/register.html', context))
    else:
        context = {
            'form' : RegisterForm(),
        }
        return HttpResponse(render(request, 'access/register.html', context))

    return HttpResponse(render(request, 'access/register.html', context))