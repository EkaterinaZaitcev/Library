from django.db import models

from library.models import Book
from users.models import User


class Rental(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="rental",
        verbose_name="Книга",
        help_text="Выберите книгу",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rental",
        verbose_name="Пользователь",
        help_text="Выберите пользователя",
    )
    rental_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата выдачи книги",
        help_text="Введите дату выдачи книги",
    )
    return_date = models.DateField(
        verbose_name="Дата возврата книги",
        help_text="Введите дату возврата книги",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Выдача книги'
        verbose_name_plural = 'Выдачи книг'

