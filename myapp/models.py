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

     def __str__(self):
          return f"{self.month} {self.day}"

class Booking(models.Model):
     type = models.CharField(max_length=20, default='')

     def __str__(self):
          return self.type
          
class Patient (models.Model):
     name = models.CharField(max_length=100, default='')
     telephone = models.CharField(max_length=100, default='')
     book_time = models.ForeignKey(Available_Date, on_delete=models.CASCADE, default=1)
     book_type = models.ForeignKey(Booking, on_delete=models.CASCADE, default=1)

     def __str__(self):
          return self.name          