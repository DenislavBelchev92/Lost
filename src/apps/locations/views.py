from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'text': "Locations",
    }
    return HttpResponse(render(request, 'locations/index.html', context))