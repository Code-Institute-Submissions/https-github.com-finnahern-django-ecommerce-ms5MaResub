from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """
    Render the shopping cart page.
    """

    return render(request, "cart/cart.html")


def add_to_cart(request, book_id):
    """
    Add a quantity of the selected book to the shopping cart.
    """

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if book_id in list(cart.keys()):
        cart[book_id] += quantity
    else:
        cart[book_id] = quantity

    request.session["cart"] = cart
    return redirect(redirect_url)


def edit_cart(request, book_id):
    """
    Change the quantity of the selected book in the shopping cart.
    """

    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[book_id] = quantity
    else:
        del cart[book_id]

    request.session["cart"] = cart
    return redirect(reverse("cart"))


def remove_from_cart(request, book_id):
    """
    Remove the selected book from the shopping cart.
    """

    cart = request.session.get("cart", {})

    del cart[book_id]

    request.session["cart"] = cart
    return HttpResponse(status=200)
