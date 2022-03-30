from django.shortcuts import render, get_object_or_404
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


def blog_post(request, year, month, day, post):
    """
    A view to render an individual page for each
    blog post in the database.
    """

    post = get_object_or_404(Post, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    template = "blog/blog_post.html"
    context = {
        "post": post
    }

    return render(request, template, context)
