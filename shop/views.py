from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book


def all_products(request):
    """
    A view to show all products in the
    database, including sorting and search results
    """

    books = Book.objects.all()
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse("shop"))

            queries = Q(name__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

    context = {
        "books": books,
        "search_term": query,
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
