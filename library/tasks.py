from django.core.mail import send_mail
from django.utils import timezone

from rental.models import Rental


def check_return_book():
    """Проверка возврата книги"""
    rental_books = Rental.objects.filter(return_date__lte=timezone.now(), is_returned=False)
    for rent in rental_books:
        send_mail(rent)
