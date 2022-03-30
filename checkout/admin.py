from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin model for the contents of the order.
    """
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin model for placed orders with read-only
    fields for data that should not change
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ("order_number", "date", "user",
                       "delivery_cost", "order_total",
                       "grand_total", "original_cart", "stripe_pid")

    fields = ("order_number", "date", "user", "full_name",
              "email", "phone_number", "country",
              "postcode", "town_or_city", "street_address1",
              "street_address2", "county", "delivery_cost",
              "order_total", "grand_total", "original_cart",
              "stripe_pid")

    list_display = ("order_number", "date", "user", "full_name",
                    "order_total", "delivery_cost", "grand_total",)

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
