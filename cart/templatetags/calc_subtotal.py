from django import template


register = template.Library()


@register.filter(name="calculate_subtotal")
def calculate_subtotal(price, quantity):
    """Calculate each books subtotal to display in the cart"""
    return price * quantity
