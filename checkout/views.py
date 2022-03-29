from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from shop.models import Book
# from cart.context import cart_contents

# import stripe
import json


def checkout(request):
    """
    Renders the checkout page with the current cart contents.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "There's nothing in your cart! Redirecting...")
        return redirect(reverse("shop"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": "test client secret",
    }

    return render(request, template, context)
