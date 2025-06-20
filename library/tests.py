from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from library.models import Book
from users.models import User


class LibraryTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create (email='test@yandex.ru', is_staff=True)
        self.author = Author.objects.create(name='Сергей Александрович Есенин',
                                            date_of_birth='1895-09-21')
        self.book = Book.objects.create(
            title='Береза',
            author=self.author,
            genre='поэзия',
            count=1,
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
                "title": "Береза",
                "author": self.author.pk,
                "author_id": self.author.id,
                "genre": "поэзия",
                "count": 1,
                },
            ]
        )

    def test_book_create(self):
        url=reverse('library:books_create')
        data= {
            "title": "Береза",
            "author": self.author.pk,
            "genre": "поэзия",
            "count": 1}
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
        data = {"count":5}
        request = self.client.patch(url, data)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get("count"), 5)

    def test_book_retrieve(self):
        url = reverse('library:books_retrieve', args=(self.book.pk,))
        data = {"genre" : "поэзия"}
        request = self.client.get(url, data)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get("genre"), self.book.genre)
