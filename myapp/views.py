from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Patient
from .models import Available_Date
from .models import Booking
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)

# Create your views here.
def index(request):
   
    available_date = Available_Date.objects.all()
    booking = Booking.objects.all()
    return render(request, 'index.html', { 'available_date': available_date, 'booking': booking})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        telephone = request.POST.get('Telephone')
        book_time_id = request.POST.get('Available_Dates')
        book_type_id = request.POST.get('Book')
        if book_time_id:
            # Retrieve the corresponding booking and available date objects
            book_time = Available_Date.objects.get(pk=book_time_id)
            book_type = Booking.objects.get(pk=book_type_id)

        patient = Patient(name=name, telephone=telephone, book_time=book_time, book_type=book_type)
        patient.save()
                
    return  render(request,'booked.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')

#def counter(request):
 #   text = request.POST['text']
   #  words_count= len(text.split())
#   return render(request, 'counter.html', {'count': words_count})

def contact(request):
    available_date = Available_Date.objects.all()
    booking = Booking.objects.all()
    return render(request, 'contact.html', {'available_date': available_date, 'booking': booking })
def news(request):
    return render(request, 'news.html')
def health(request):
    return render(request, 'health.html')


def booked(request):
    return render(request, 'booked.html')    
   



