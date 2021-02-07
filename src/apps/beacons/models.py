from django.db import models
from django.contrib.auth.models import User

class Beacon(models.Model):
    beacon_choices = [
    ('LF', 'Lost and Found'),
    ('SL', 'Stolen item'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)
    latitude = models.DecimalField(default=0, max_digits=18, decimal_places=15)
    longitude = models.DecimalField(default=0, max_digits=18, decimal_places=15)
    name = models.CharField(max_length=200)
    beacon_type = models.CharField(
        max_length=2, 
        choices=beacon_choices,
        default='LF',
    )

    def __str__(self):
        return self.name