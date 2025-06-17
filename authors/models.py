from django.db import models


class Author(models.Model):
    """Класс Автор произведения"""

    name = models.CharField(
        max_length=255, verbose_name="ФИО автора", help_text="Укажите ФИО"
    )
    preview = models.ImageField(
        upload_to="materials/preview", verbose_name="Фото автора", blank=True, null=True
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
        help_text="Введите дату рождения автора, в формате ГОД-МЕСЯЦ-ДЕНЬ, если она известна",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Автор - {self.name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["name"]
