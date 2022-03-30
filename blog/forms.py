from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    """
    Form for the super user to create new blog posts
    """
    class Meta:
        model = Post
        fields = ["title", "body"]


class EditPostForm(forms.ModelForm):
    """
    Form for the super user to edit existing blog posts.
    """
    class Meta:
        model = Post
        fields = ["title", "body"]
