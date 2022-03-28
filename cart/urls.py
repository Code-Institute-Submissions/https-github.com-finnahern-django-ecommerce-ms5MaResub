from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_cart, name="cart"),
    path("add/<book_id>/", views.add_to_cart, name="add_to_cart"),
    path("edit/<book_id>/", views.edit_cart, name="edit_cart"),
    path("remove/<book_id>/", views.remove_from_cart, name="remove_from_cart"),
]
