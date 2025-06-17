from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from library.models import Book
from users.models import User


class LibraryTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@yandex.ru',)
        self.author = Author.objects.create(name='Сергей Александрович Есенин',
                                            date_of_birth='1895-09-21')
        self.book = Book.objects.create(
            title='Береза',
            author=self.author,
            genre='поэзия'
        )
        self.client.force_authenticate(user=self.user)

    def test_book_retrieve(self):
        url = reverse('library:books_retrieve', args=(self.book.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.book.title)
