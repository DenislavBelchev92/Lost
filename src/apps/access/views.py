from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                context = {
                    'text': "loged_in " + username,
                }
                return HttpResponse(render(request, 'mainpage/index.html', context))

            else:
                context = {
                    'form' : form,
                    'text': 'Login failed',
                }
                return HttpResponse(render(request, 'access/login.html', context))

                
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

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            user.save()

            context = {
                'text': "You just registered with first_name " + first_name + " last_name " + last_name + " username " + " email " + email + " password " + str(password),
            }
            return HttpResponse(render(request, 'mainpage/index.html', context))
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