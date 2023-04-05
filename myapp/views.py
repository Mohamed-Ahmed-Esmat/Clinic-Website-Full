from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    features = Feature()
    features.id = 1
    features.name = 'Feature 1'
    features.description = 'This is the first feature'
    
    return render(request, 'test.html', {'feature': features})

def counter(request):
    text = request.POST['text']
    words_count= len(text.split())
    return render(request, 'counter.html', {'count': words_count})

