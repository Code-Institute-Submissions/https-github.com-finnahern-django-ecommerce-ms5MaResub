from django.contrib import admin
from .models import Book, Genre


class BookAdmin(admin.ModelAdmin):
    """Admin model for books in the store."""
    list_display = (
        "isbn",
        "name",
        "author",
        "genre",
        "price",
        "image",
    )
    ordering = ("isbn",)


class GenreAdmin(admin.ModelAdmin):
    """Admin model for genres"""
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
