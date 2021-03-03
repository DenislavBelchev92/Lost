from django.db import models
from django import forms
from .models import Beacon

class BeaconFullForm(forms.ModelForm):
    class Meta:
        model = Beacon
        fields = ['name', 'latitude', 'longitude', 'beacon_type', 'description']
        widgets = {
            'description': forms.Textarea(),
        }
        
class BeaconAddForm(forms.ModelForm):
    class Meta:
        model = Beacon
        fields =['name', 'latitude', 'longitude', 'beacon_type', 'description']

        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }