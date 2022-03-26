from django.shortcuts import render
from .models import Book


def all_products(request):
    """
    A view to return to show all products in the
    database, including sorting and search results
    """

    books = Book.objects.all()

    context = {
        "books": books,
    }

    return render(request, "shop/shop.html", context)
