from django.shortcuts import render
from .models import Post


def blog_list(request):
    """
    A view to display the blog template.
    """
    posts = Post.objects.all()

    template = "blog/blog.html"
    context = {
        "posts": posts
    }

    return render(request, template, context)
