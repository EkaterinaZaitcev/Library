from django.contrib import admin
from authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "preview", "date_of_birth")
    search_fields = ["book"]
