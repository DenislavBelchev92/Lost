from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from pprint import pprint

users = User.objects.all()
def index(request):
   # return HttpResponse("Hello, world. You're at the polls index.")
   val = str(pprint(users))
   return HttpResponse("OK " + val)