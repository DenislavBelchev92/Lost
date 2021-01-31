from django.shortcuts import render
from django.http import HttpResponse
from .models import Beacon
from .forms import BeaconFullForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'text': "Beacons",
        'beacons': Beacon.objects.all(),
        'beacon_types': Beacon.beacon_choices,

    }
    return HttpResponse(render(request, 'beacons/index.html', context))

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

            beacon = Beacon.objects.create(
                name=name, 
                user_id=user_id, 
                latitude=latitude, 
                longitude=longitude,
                beacon_type=beacon_type)

            beacon.save()

            context = {
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
        # Return empty form
        form = BeaconFullForm()
        context = {
            'form' : form,
        }
        return HttpResponse(render(request, 'beacons/add.html', context))

@login_required
def details(request, id=None):

    # If we display a beacon
    if id != None:
        beacon = Beacon.objects.get(id=id)
        form = BeaconFullForm(instance=beacon)
    else:
        form = BeaconFullForm()

    context = {
        'form' : form,
    }
    return HttpResponse(render(request, 'beacons/add.html', context))