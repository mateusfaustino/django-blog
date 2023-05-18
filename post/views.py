from django.shortcuts import render
from post.models import Post

def index(request):
    posts = Post.objects.all()
    return

def create(request):
    return

def store(request):
    return

def show(request, post_id):
    post = Post.objects.get(pk=post_id)
    return

def edit(request, post_id):
    return

def update(request, post_id):
    return

def destroy(request,  post_id):
    return