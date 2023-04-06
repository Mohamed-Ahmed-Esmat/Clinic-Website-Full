from django.contrib import admin
from .models import Feature
from .models import Available_Resv
from .models import Available_Tel
from .models import Available_Oper
from .models import Booking

# Register your models here.

admin.site.register(Feature)
admin.site.register(Available_Resv)
admin.site.register(Available_Tel)
admin.site.register(Available_Oper)
admin.site.register(Booking)