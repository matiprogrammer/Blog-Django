from django import forms
from .models import Comment,Articles


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'content','content')


class PostForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'content', 'image')