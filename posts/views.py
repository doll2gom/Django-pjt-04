from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def init(request):
    return redirect('posts:index')

def index(request):
    posts = Post.objects.order_by('-pk')
    page = request.GET.get('page')
    paginator = Paginator(posts, 5)
    try:
        post_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        post_obj = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        post_obj = paginator.get_page(page)
        
    context = {
        'posts': post_obj,
        'paginator': paginator,

    }
    return render(request, 'posts/index.html', context)


def detail(request, posts_pk):
    post = Post.objects.get(pk = posts_pk)
    comment_form = CommentForm()
    comments = post.comment_set.all()
    
    context = {
        'post': post,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@login_required
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


@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('posts:detail', post.pk)
    context = {
        'post1': post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)