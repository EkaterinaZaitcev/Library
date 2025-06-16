from django.db import models

from authors.models import Author


class Genre(models.Model):
    """Класс жанра"""
    name = models.CharField(max_length=150, verbose_name='Название жанра')
    description = models.TimeField(verbose_name='Описание жанра', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    """Класс Книги"""

    title = models.CharField(
        max_length=255,
        verbose_name="Название книги",
        help_text="Укажите название книги"
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name="Автор книги",
        help_text="Выберите автора",
        blank=True, null=True
    )
    genre = models.CharField(
        max_length=255,
        verbose_name="Жанр книги",
        help_text="Введите жанр книги",
    )
    preview = models.ImageField(
        upload_to="materials/preview", verbose_name="Превью", blank=True, null=True
    )
    count = models.PositiveIntegerField(
        verbose_name="Количество книг",
        help_text="Введите количество книг в наличии",
        default=1,
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} - {self.author}"
