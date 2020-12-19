from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    # These are the fields when we add a location
    # First is a topic so we don't need to specify options for it
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Latitude',  {'fields': ['latitude']}),
        ('Longitude',  {'fields': ['longitude']}),

       # ('User ID',  {'fields': ['user_id']}),

    ]

    list_display = ('name', 'latitude', 'longitude', 'user_id')

admin.site.register(Location, LocationAdmin)