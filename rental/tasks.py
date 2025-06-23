from celery import shared_task
from django.utils import timezone

from rental.models import Rental
from rental.services import send_mail


@shared_task
def check_return_book():
    rental_books = Rental.objects.filter(
        return_date__lte=timezone.now(), is_returned=False
    )
    for rental in rental_books:
        send_mail(rental)
