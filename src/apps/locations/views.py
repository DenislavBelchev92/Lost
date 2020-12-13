from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'text': "Locations loged in",
    }
    return HttpResponse(render(request, 'locations/index.html', context))
