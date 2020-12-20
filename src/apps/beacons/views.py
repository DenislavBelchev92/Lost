from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'text': "Beacons",
    }
    return HttpResponse(render(request, 'beacons/index.html', context))
