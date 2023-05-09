from django.contrib import admin
from django.urls import path
from galeria.views import index,image

urlpatterns = [
    path('', index, name='home'),
    path('image', image, name='image'),
]
