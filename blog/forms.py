from django import forms
from .models import Post , comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'abstract' , 'body', 'author', 'date', 'photo']

class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['body']