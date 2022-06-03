from django.db import models
from datetime import datetime

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    location = models.CharField(max_length=1000000)
    details = models.CharField(max_length=1000000)