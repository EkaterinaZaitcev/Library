# Generated by Django 5.2.3 on 2025-06-24 12:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("library", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Rental",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rental_date",
                    models.DateField(
                        auto_now_add=True,
                        help_text="Введите дату выдачи книги",
                        verbose_name="Дата выдачи книги",
                    ),
                ),
                (
                    "return_date",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату возврата книги",
                        null=True,
                        verbose_name="Дата возврата книги",
                    ),
                ),
                (
                    "is_returned",
                    models.BooleanField(
                        default=False, verbose_name="Флаг возврата книги"
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        default=1,
                        help_text="Выберите книгу",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rental",
                        to="library.book",
                        verbose_name="Книга",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="Выберите пользователя",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="rental",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Выдача книги",
                "verbose_name_plural": "Выдачи книг",
                "ordering": ["pk"],
            },
        ),
    ]
