from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('counter', views.counter, name='counter'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path('health', views.health, name='health'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
   # path('', views.my_view, name='my_view')
]