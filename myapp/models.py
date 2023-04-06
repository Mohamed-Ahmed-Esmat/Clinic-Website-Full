from django.db import models

# Create your models here.
class Feature(models.Model):
     name = models.CharField(max_length=100, default='')
     details = models.CharField(max_length=500, default='')

class Available_Date(models.Model):
     day = models.IntegerField(default=31)
     month = models.CharField(max_length=3, default='Dec')
     year = models.IntegerField(default=2023)
     time = models.CharField(max_length=10, default='12:00')

class Booking(models.Model):
     type = models.CharField(max_length=20, default='')