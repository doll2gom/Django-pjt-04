from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
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
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    
    context = {
        'form': form,
    }

    return render(request, 'posts/create.html', context)

def answer(request):
    return