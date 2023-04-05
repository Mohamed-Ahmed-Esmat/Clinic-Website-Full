from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    features = Feature()
    features.id = 1
    features.name = 'Feature 1'
    features.description = 'This is the first feature'
    
    return render(request, 'index.html', {'feature': features})

#def counter(request):
 #   text = request.POST['text']
   #  words_count= len(text.split())
#   return render(request, 'counter.html', {'count': words_count})

def contact(request):
    return render(request, 'contact.html')
def news(request):
    return render(request, 'news.html')
def health(request):
    return render(request, 'health.html')

