from django.shortcuts import render
from django.http import HttpResponse
from .models import Beacon
from .forms import BeaconFullForm, BeaconAddForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django import forms

index_context = {
    'beacon_types': Beacon.beacon_choices,
}

# Utilities - start {
def render_add_form(request, debug_text = "", is_add = 1,):
    # Provide empty form
    if is_add:
        form = BeaconAddForm()
    else:
        form = BeaconFullForm()

    context = {
        'form' : form,
    }
    if debug_text:
        context.update({'debug_text': "Please fix the form errors"})

    return HttpResponse(render(request, 'beacons/add.html', context))
# Utilities - end }

@login_required
def index(request):
    return HttpResponse(render(request, 'beacons/index.html', index_context))

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
            beacon = Beacon.objects.create(
                user_id =       request.user.id, 
                name =          form.cleaned_data.get('name'), 
                latitude =      form.cleaned_data.get('latitude'), 
                longitude =     form.cleaned_data.get('longitude'),
                beacon_type =   form.cleaned_data.get('beacon_type'),
                description =   form.cleaned_data.get('description')
            )
            # Update the database
            beacon.save()

            context = {
                'debug_text': " We saved beacon with name " + beacon.name,
            }
            context.update(index_context)
            return HttpResponse(render(request, 'beacons/index.html', context))
        else:
            return render_add_form(request, "Please fix the form errors")
    else:
        return render_add_form(request)

@login_required
def details(request, id=None):
    # If we display a beacon
    try:
        beacon = Beacon.objects.get(id=id)
    except:
        raise Http404("Beacon with id" + int(id) + "exist")

    context = {
        'beacon_id': id,
        'form' : BeaconFullForm(instance=beacon),
        'beacon' : beacon,
    }
    return HttpResponse(render(request, 'beacons/details.html', context))

@login_required
def update(request):

    if request.method == 'POST':
        beacon = Beacon.objects.get(pk=request.POST['beacon_id'])

        if '_delete' in request.POST:
            beacon.delete()
            context = {
                'debug_text': " We deleted beacon with name " + beacon.name ,
            }
            context.update(index_context)
            return HttpResponse(render(request, 'beacons/index.html', index_context))
        else:
            # Assume we are in submit case
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
                    'debug_text': " We updated beacon with name " + beacon.name ,
                }
                context.update(index_context)
                return HttpResponse(render(request, 'beacons/index.html', index_context))

            else:
                # Here we should handle if the form input are invalid
                context = {
                    'debug_text': "Please fix the form errors",
                    'form' : form,
                }
                return HttpResponse(render(request, 'beacons/index.html', context))
    else:
        raise Http404("Page does not exist")
   