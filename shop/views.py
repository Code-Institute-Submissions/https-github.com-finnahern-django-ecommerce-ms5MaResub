from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book, Genre


def all_products(request):
    """
    A view to show all products in the
    database, including sorting and search results
    """

    books = Book.objects.all()
    genres = Genre.objects.all()
    genre = None
    query = None
    # Initialise empty query set to be populated below
    queries = Book.objects.none()

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse("shop"))
            if "biography" in query.lower():
                queries = queries | Q(genre__exact=genres[0])
            if "classic" in query.lower():
                queries = queries | Q(genre__exact=genres[1])
            if "crime" in query.lower():
                queries = queries | Q(genre__exact=genres[2])
            if "fiction" in query.lower():
                queries = queries | Q(genre__exact=genres[3])
            if ("non" in query.lower() and "fiction" in query.lower()) or "nonfiction" in query.lower():
                queries = queries | Q(genre__exact=genres[4])

            query_array = query.split()
            for x in query_array:
                queries = queries | Q(name__icontains=x) | Q(author__icontains=x)
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
