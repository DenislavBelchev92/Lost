from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name