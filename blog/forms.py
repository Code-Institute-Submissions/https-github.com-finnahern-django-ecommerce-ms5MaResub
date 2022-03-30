from django import forms
from django.forms import ModelForm
from .models import Post


class CreatePostForm(forms.ModelForm):
    """
    Form for the super user to create new blog posts
    """
    class Meta:
        model = Post
        fields = ["title", "body"]
