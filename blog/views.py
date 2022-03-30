from django.shortcuts import render


def blog_list(request):
    """
    A view to display the blog template.
    """

    template = "blog/blog.html"
    context = {}

    return render(request, template, context)
