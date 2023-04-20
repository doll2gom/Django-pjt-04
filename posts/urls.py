from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:posts_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/answer/<int:select_answer>/', views.answer, name='answer'),
]
