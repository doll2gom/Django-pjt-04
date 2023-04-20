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


def detail(request, posts_pk):
    post = Post.objects.get(pk = posts_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


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


def answer(request, post_pk, select_answer):
    post = Post.objects.get(pk=post_pk)
    if request.user in post.select1_users.all() or request.user in post.select2_users.all():
        pass
    else:
        if select_answer == 1:
            post.select1_users.add(request.user)
        elif select_answer == 2:
            post.select2_users.add(request.user)
    return redirect('posts:detail', post_pk )

