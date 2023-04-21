from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('select1_content', 'image1', 'select2_content', 'image2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
