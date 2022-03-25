from django.shortcuts import render


def all_products(request):
    """
    A view to return to show all products in the
    database, including sorting and search queries
    """

    return render(request, "shop/shop.html")
