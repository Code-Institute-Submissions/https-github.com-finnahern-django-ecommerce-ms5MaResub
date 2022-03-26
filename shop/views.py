from django.shortcuts import render, get_object_or_404
from .models import Book


def all_products(request):
    """
    A view to show all products in the
    database, including sorting and search results
    """

    books = Book.objects.all()

    context = {
        "books": books,
    }

    return render(request, "shop/shop.html", context)


def product_detail(request, book_id):
    """
    A view to render an individual page for each book
    in the database, displaying more information and allowing
    the user to add it to their cart.
    """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        "book": book,
    }

    return render(request, "shop/product_detail.html", context)
