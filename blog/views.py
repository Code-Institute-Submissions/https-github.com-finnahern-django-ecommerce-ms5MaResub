from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Post
from .forms import CreatePostForm


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


@user_passes_test(lambda u: u.is_superuser)
def add_post(request):
    """
    A view to display the form allowing super
    users to create new blog posts
    """
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = new_post.title.lower().replace(" ", "-")
            new_post = form.save()
            return render(request, "blog/blog_post.html", {"post": new_post})
    else:
        form = CreatePostForm()
    return render(request, "blog/new_post.html", {"form": form})
