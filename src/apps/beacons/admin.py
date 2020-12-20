from django.contrib import admin
from .models import Beacon

class BeaconAdmin(admin.ModelAdmin):

    # This is for when we add in admin panel
    fieldsets = [
        (None,              {'fields': ['name']}),
        ('Latitude',        {'fields': ['latitude']}),
        ('Longitude',       {'fields': ['longitude']}),
        ('Beacon_type',     {'fields': ['beacon_type']}),

       # ('User ID',  {'fields': ['user_id']}),

    ]

    # This is for when we display in admin panel
    list_display = ('name', 'latitude', 'longitude', 'user_id', 'beacon_type')

admin.site.register(Beacon, BeaconAdmin)