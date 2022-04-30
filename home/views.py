from django.shortcuts import render


def index(request):
    """
    A view to return the index page.
    """
    return render(request, "home/index.html")

def error_404(request, exception):
    """
    A view to render the 404 template
    """
    return render(request, "home/404.html")
