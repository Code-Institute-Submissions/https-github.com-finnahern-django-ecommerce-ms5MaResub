from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog"),
    path("<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<slug:post>/", views.blog_post, name="blog_post"),
    path("new_post/", views.add_post, name="add_post"),
    path("edit_post/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<slug:post>/", views.edit_post, name="edit_post"),
]
