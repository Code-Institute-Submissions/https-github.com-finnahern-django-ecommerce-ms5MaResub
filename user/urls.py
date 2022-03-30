from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),
    path("order_history/", views.order_history, name="order_history"),
]
