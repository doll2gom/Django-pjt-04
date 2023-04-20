from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'select1_content', 'image1', 'select2_content', 'image2')
