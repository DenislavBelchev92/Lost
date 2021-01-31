from django.shortcuts import render
from django.http import HttpResponse
from .models import Beacon
from .forms import BeaconFullForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

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
    try:
        beacon = Beacon.objects.get(id=id)
    except:
        raise Http404("Page does not exist")

    context = {
        'beacon_id': id,
        'form' : BeaconFullForm(instance=beacon),
    }
    return HttpResponse(render(request, 'beacons/details.html', context))

@login_required
def update(request):

    if request.method == 'POST':
        # Validate and add
        form = BeaconFullForm(request.POST)
        if form.is_valid():

            beacon = Beacon.objects.get(pk=request.POST['beacon_id'])

            beacon.user_id = request.user.id
            beacon.name = form.cleaned_data.get('name')
            beacon.latitude = form.cleaned_data.get('latitude')
            beacon.longitude = form.cleaned_data.get('longitude')
            beacon.beacon_type = form.cleaned_data.get('beacon_type')

            beacon.save()

            context = {
                'debug_text': " We updated beacon with name " + beacon.name,
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
        raise Http404("Page does not exist")
   