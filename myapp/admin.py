from django.contrib import admin
from .models import Available_Date
from .models import Booking
from .models import Patient

# Register your models here.

admin.site.register(Available_Date)
admin.site.register(Booking)
admin.site.register(Patient)