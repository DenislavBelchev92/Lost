from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from apps.locations.models import Location
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'text': "You are not supposed to be here noone",
    }
    if request.user.is_authenticated:

        locations = Location.objects.filter(user_id=request.user.id)
        context = {
            'text': "This is your profile page " + request.user.username + " ",
          #  'beacon_types': [type[1] for type in Location.beacon_choices],
            'beacon_types': Location.beacon_choices,
            'locations': locations,
            'location_types': Location.beacon_choices,

        }

    return HttpResponse(render(request, 'profile_page/index.html', context))

