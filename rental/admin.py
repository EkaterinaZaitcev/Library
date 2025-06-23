from django.contrib import admin
from rental.models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "user", "rental_date", "return_date")
