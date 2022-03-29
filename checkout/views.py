from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    Renders the checkout page with the current cart contents.
    """
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "There's nothing in your cart! Redirecting...")
        return redirect(reverse("shop"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form
    }

    return render(request, template, context)
