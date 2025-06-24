import pytest


@pytest.fixture(autouse=True)
def use_sqlite_in_tests(settings):
    """
    Перед каждым тестом будем использовать SQLite в памяти.
    """
    settings.DATABASES = {
        'default': {
            "ENGINE": 'django.db.backends.sqlite3',
            'NAME': ':memory:'

        }
    }
