from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('counter', views.counter, name='counter'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path('health', views.health, name='health'),

]