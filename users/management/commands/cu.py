from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание тестового пользователя"""
    message = "Тестовый пользователь"

    def handle(self, *args, **options):
        user = User.objects.create(
            username='Ivan Petrov',
            email='test@mail.ru',
            is_superuser=False,
            is_staff=False,
            is_active=True,
            phone='+79991231231',
        )
        user.set_password('zaq123')
        user.save()
