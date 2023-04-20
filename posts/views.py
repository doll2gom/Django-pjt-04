from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def init(request):
    return redirect('posts:index')

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html', context)

def detail(request):
    return

def create(request):
    return

def answer(request):
    return