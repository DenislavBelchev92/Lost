from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):

    # This is for when we add in admin panel
    fieldsets = [
        (None,              {'fields': ['name']}),
        ('Latitude',        {'fields': ['latitude']}),
        ('Longitude',       {'fields': ['longitude']}),
        ('Location_type',   {'fields': ['location_type']}),

       # ('User ID',  {'fields': ['user_id']}),

    ]

    # This is for when we display in admin panel
    list_display = ('name', 'latitude', 'longitude', 'user_id', 'location_type')

admin.site.register(Location, LocationAdmin)