from django.shortcuts import render, redirect


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
