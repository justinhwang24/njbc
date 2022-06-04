from django.db import models
from datetime import date, datetime
from datetime import time

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=date.today, blank=True)
    time = models.TimeField(default=datetime.now().time(), blank=True)
    location = models.CharField(max_length=1000000)
    details = models.CharField(max_length=1000000)