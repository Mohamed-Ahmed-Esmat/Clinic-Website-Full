from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
from .models import Available_Resv
from .models import Available_Tel
from .models import Available_Oper
from .models import Booking

# Create your views here.
def index(request):
    features = Feature.objects.all()
    available_resv = Available_Resv.objects.all()
    available_tel = Available_Tel.objects.all()
    available_oper = Available_Oper.objects.all()
    booking = Booking.objects.all()
    return render(request, 'index.html', {'features': features, 'available_resv': available_resv, 'available_tel': available_tel, 'available_oper': available_oper, 'booking': booking})




#def counter(request):
 #   text = request.POST['text']
   #  words_count= len(text.split())
#   return render(request, 'counter.html', {'count': words_count})

def contact(request):
    available_resv = Available_Resv.objects.all()
    available_tel = Available_Tel.objects.all()
    available_oper = Available_Oper.objects.all()
    booking = Booking.objects.all()
    return render(request, 'contact.html', {'available_resv': available_resv, 'available_tel': available_tel, 'available_oper': available_oper, 'booking': booking })
def news(request):
    return render(request, 'news.html')
def health(request):
    return render(request, 'health.html')

