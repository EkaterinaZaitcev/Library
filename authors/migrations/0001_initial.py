# Generated by Django 5.2.3 on 2025-06-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                    "name",
                    models.CharField(
                        help_text="Укажите ФИО",
                        max_length=255,
                        verbose_name="ФИО автора",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="materials/preview",
                        verbose_name="Фото автора",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату рождения автора, в формате ГОД-МЕСЯЦ-ДЕНЬ, если она известна",
                        null=True,
                        verbose_name="Дата рождения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
                "ordering": ["name"],
            },
        ),
    ]
