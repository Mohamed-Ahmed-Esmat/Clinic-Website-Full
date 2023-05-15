from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('counter', views.counter, name='counter'),
    path('news', views.news, name='news'),
    path('booked', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('health', views.health, name='health'),
    path('login', views.login, name='login'),
    path ('booked',views.booked, name='booked')
   # path('', views.my_view, name='my_view')
]