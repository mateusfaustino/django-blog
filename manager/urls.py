from django.contrib import admin
from django.urls import path
from manager.views import index

urlpatterns = [
    path('', index, name='manage.index'),
]