from django.contrib import admin
from django.urls import path
from client.views import home,post

urlpatterns = [
    path('', home, name='home'),
    path('post/<post_slug>', post, name='post'),
]