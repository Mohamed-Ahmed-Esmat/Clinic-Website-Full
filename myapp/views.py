from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Feature
from .models import Available_Date
from .models import Booking
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)

# Create your views here.
def index(request):
    features = Feature.objects.all()
    available_date = Available_Date.objects.all()
    booking = Booking.objects.all()
    return render(request, 'index.html', {'features': features,  'available_date': available_date, 'booking': booking})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
      
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
        elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
        else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('login')
    return render(request, 'register.html')

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


