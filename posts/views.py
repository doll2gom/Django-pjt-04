from django.shortcuts import render, redirect

# Create your views here.

def init(request):
    return redirect('posts:index')

def index(request):
    
    return render(request, 'posts/index.html')

def detail(request):
    return

def create(request):
    return

def answer(request):
    return