
from django import forms
from .models import Blogs

class PostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','title')