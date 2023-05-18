from django.contrib import admin
from django.urls import path
from client.views import home

urlpatterns = [
    path('', home, name='home'),
]