from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Book


def cart_contents(request):
    """
    Context processor to determine the contents
    and total cost of the shopping cart.
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get("cart", {})

    for book_id, quantity in cart.items():
        book = get_object_or_404(Book, pk=book_id)
        total += quantity * book.price
        product_count += quantity
        cart_items.append({
            "book_id": book_id,
            "quantity": quantity,
            "book": book,
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = total + delivery

    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "grand_total": grand_total,
    }

    return context
