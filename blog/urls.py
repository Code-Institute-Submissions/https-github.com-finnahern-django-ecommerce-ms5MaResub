from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", views.blog_post, name="blog_post"),
]
