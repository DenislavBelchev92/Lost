from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Location(models.Model):
    beacon_choices = [
    ('LF', 'Lost and Found'),
    ('SL', 'Stolen item'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    name = models.CharField(max_length=200)
    location_type = models.CharField(
        max_length=2, 
        choices=beacon_choices,
        default='LF',
    )

    def __str__(self):
        return self.name