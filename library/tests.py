from http.client import responses

from django.urls import reverse
from rest_framework import status, request
from rest_framework.test import APITestCase

from authors.models import Author
from library.models import Book, Genre
from users.models import User


class LibraryTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create (email='test@yandex.ru', is_staff=True)
        self.author = Author.objects.create(name='Сергей Александрович Есенин',
                                            date_of_birth='1895-09-21')
        self.genre = Genre.objects.create(name='Поэзия')
        self.book = Book.objects.create(
            title='Береза',
            author=self.author,
            author_id=self.author.pk,
            genre=self.genre,
            count=3
        )
        self.client.force_authenticate(user=self.user)


    def test_book_list(self):
        url = reverse('library:books_list')
        request = self.client.get(url)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response, [
                {
                "id": self.book.pk,
                "author": self.author.pk,
                "genre": self.genre.id,
                "title": "Береза",
                "preview": None,
                "count": 3,
                "quantity": 0,
                "is_available": True
                },
            ]
        )

    def test_book_create(self):
        url=reverse('library:books_create')
        data= {
            "id": self.book.pk,
            "author": self.author.pk,
            "genre": self.genre.id,
            "title": "Береза",
            "preview": "",
            "count": 3,
            "quantity": 0,
            "is_available": True
        }
        request=self.client.post(url, data)

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), 2)


    def test_book_destroy(self):
        url = reverse('library:books_delete', args=(self.book.pk,))
        request = self.client.delete(url)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), 0)

    def test_book_update(self):
        url = reverse('library:books_update', args=(self.book.pk,))
        data = {"count":3}
        request = self.client.patch(url, data)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get("count"), 3)

    def test_book_retrieve(self):
        url = reverse('library:books_retrieve', args=(self.book.pk,))
        data = {"genre" : self.genre.id}
        request = self.client.get(url, data)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get("genre"), self.genre.id)
