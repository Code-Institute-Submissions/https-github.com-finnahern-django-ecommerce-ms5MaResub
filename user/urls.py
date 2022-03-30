from django.urls import path
from . import views

urlpatterns = [
    # path("", views.blog_list, name="blog"),
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),
]
