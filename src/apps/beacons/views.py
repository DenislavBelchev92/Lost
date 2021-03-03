from django.shortcuts import render
from django.http import HttpResponse
from .models import Beacon
from .forms import BeaconFullForm, BeaconAddForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django import forms

@login_required
def index(request):
    context = {
        'beacon_types': Beacon.beacon_choices,
    }
    return HttpResponse(render(request, 'beacons/index.html', context))

@login_required
def per_type(request, beacon_type=None):
    context = {
        'beacons': Beacon.objects.filter(beacon_type=beacon_type),
        'beacon_types': [b_type for b_type in Beacon.beacon_choices if b_type[0] == beacon_type],
    }
    return HttpResponse(render(request, 'beacons/per_type.html', context))

@login_required
# Used for both add/show/update
def add(request, id=None):
    if request.method == 'POST':
        # Validate and add
        form = BeaconFullForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            name = form.cleaned_data.get('name')
            latitude = form.cleaned_data.get('latitude')
            longitude = form.cleaned_data.get('longitude')
            beacon_type = form.cleaned_data.get('beacon_type')
            beacon_description = form.cleaned_data.get('description')

            beacon = Beacon.objects.create(
                name=name, 
                user_id=user_id, 
                latitude=latitude, 
                longitude=longitude,
                beacon_type=beacon_type,
                description=beacon_description
                )

            beacon.save()

            context = {
                'beacons': Beacon.objects.all(),
                'beacon_types': Beacon.beacon_choices,
                'debug_text': " We saved beacon with name " + beacon.name,
            }
            return HttpResponse(render(request, 'beacons/index.html', context))

        else:
            # Here we should handle if the form input are invalid
            context = {
                'debug_text': "Please fix the form errors",
                'form' : form,
            }
            return HttpResponse(render(request, 'beacons/add.html', context))
    else:
        # Provide empty form
        form = BeaconAddForm()
        context = {
            'form' : form,
        }
        return HttpResponse(render(request, 'beacons/add.html', context))

@login_required
def details(request, id=None):
    # If we display a beacon
    try:
        beacon = Beacon.objects.get(id=id)
    except:
        raise Http404("Page does not exist")

    context = {
        'beacon_id': id,
        'form' : BeaconFullForm(instance=beacon),
        'beacon' : beacon,

    }
    return HttpResponse(render(request, 'beacons/details.html', context))

@login_required
def update(request):

    if request.method == 'POST':
        # Validate and add

        beacon = Beacon.objects.get(pk=request.POST['beacon_id'])
        try:
            request.POST['_delete']
        except:
            pass
        else:
            beacon.delete()
            context = {
                'beacon_types': Beacon.beacon_choices,
                'debug_text': " We deleted beacon with name " + beacon.name ,
            }
            return HttpResponse(render(request, 'beacons/index.html', context))

        form = BeaconFullForm(request.POST)
        if form.is_valid():

            beacon.user_id = request.user.id
            beacon.name = form.cleaned_data.get('name')
            beacon.latitude = form.cleaned_data.get('latitude')
            beacon.longitude = form.cleaned_data.get('longitude')
            beacon.beacon_type = form.cleaned_data.get('beacon_type')
            beacon.description = form.cleaned_data.get('description')

            beacon.save()

            context = {
                'beacon_types': Beacon.beacon_choices,
                'debug_text': " We updated beacon with name " + beacon.name ,
            }
            return HttpResponse(render(request, 'beacons/index.html', context))

        else:
            # Here we should handle if the form input are invalid
            context = {
                'debug_text': "Please fix the form errors",
                'form' : form,
            }
            return HttpResponse(render(request, 'beacons/index.html', context))
    else:
        raise Http404("Page does not exist")
   