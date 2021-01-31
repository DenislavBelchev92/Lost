from django.db import models
from django import forms
from .models import Beacon

class BeaconFullForm(forms.ModelForm):
    class Meta:
        model = Beacon
        fields = ['name', 'latitude', 'longitude', 'beacon_type']
