from django.contrib import admin
from library.models import Book, Genre
from rental.models import Rental


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "genre", "preview", "count")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
