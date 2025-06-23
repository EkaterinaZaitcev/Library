from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from library.models import Book, Genre
from rental.models import Rental
from users.models import User


class AuthorTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@yandex.ru", is_staff=True)
        self.author = Author.objects.create(
            name="Сергей Александрович Есенин", date_of_birth="1895-09-21"
        )
        self.client.force_authenticate(user=self.user)

    def test_author_list(self):
        url = reverse("authors:author-list")
        request = self.client.get(url)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response,
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 1,
                        "name": "Сергей Александрович Есенин",
                        "preview": None,
                        "date_of_birth": "1895-09-21",
                    }
                ],
            },
        )

    def test_author_create(self):
        url = reverse("authors:author-list")
        data = {"name": "Сергей Александрович Есенин", "date_of_birth": "1895-09-21"}
        request = self.client.post(url, data)

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.all().count(), 2)

    def test_author_destroy(self):
        url = reverse("authors:author-detail", args=(self.author.pk,))
        request = self.client.delete(url)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.all().count(), 0)

    def test_author_update(self):
        url = reverse("authors:author-detail", args=(self.author.pk,))
        data = {"date_of_birth": "1895-09-10"}
        request = self.client.patch(url, data)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get("date_of_birth"), "1895-09-10")

    def test_author_retrieve(self):
        url = reverse("authors:author-detail", args=(self.author.pk,))
        data = {"name": "Сергей Александрович Есенин"}
        request = self.client.get(url, data)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get("name"), self.author.name)


class LibraryTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@yandex.ru", is_staff=True)
        self.author = Author.objects.create(
            name="Сергей Александрович Есенин", date_of_birth="1895-09-21"
        )
        self.genre = Genre.objects.create(name="Поэзия")
        self.book = Book.objects.create(
            title="Береза",
            author=self.author,
            author_id=self.author.pk,
            genre=self.genre,
            count=3,
        )
        self.client.force_authenticate(user=self.user)

    def test_book_list(self):
        url = reverse("library:books_list")
        request = self.client.get(url)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response,
            [
                {
                    "id": self.book.pk,
                    "author": self.author.pk,
                    "genre": self.genre.id,
                    "title": "Береза",
                    "preview": None,
                    "count": 3,
                    "quantity": 0,
                    "is_available": True,
                },
            ],
        )

    def test_book_create(self):
        url = reverse("library:books_create")
        data = {
            "id": self.book.pk,
            "author": self.author.pk,
            "genre": self.genre.id,
            "title": "Береза",
            "preview": "",
            "count": 3,
            "quantity": 0,
            "is_available": True,
        }
        request = self.client.post(url, data)

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), 2)

    def test_book_destroy(self):
        url = reverse("library:books_delete", args=(self.book.pk,))
        request = self.client.delete(url)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), 0)

    def test_book_update(self):
        url = reverse("library:books_update", args=(self.book.pk,))
        data = {"count": 3}
        request = self.client.patch(url, data)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get("count"), 3)

    def test_book_retrieve(self):
        url = reverse("library:books_retrieve", args=(self.book.pk,))
        data = {"genre": self.genre.id}
        request = self.client.get(url, data)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get("genre"), self.genre.id)

class RentalTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@yandex.ru", is_staff=True)
        self.author = Author.objects.create(
            name="Сергей Александрович Есенин", date_of_birth="1895-09-21"
        )
        self.genre = Genre.objects.create(name="Поэзия")
        self.book = Book.objects.create(
            title="Береза",
            author=self.author,
            author_id=self.author.pk,
            genre=self.genre,
            count=1,
        )
        self.rental = Rental.objects.create(
            rental_date="2025-06-24", return_date="2025-07-20", user=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_rental_list(self):
        url = reverse("rental:rental_list")
        request = self.client.get(url)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response,
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 1,
                        "user": {"id": 1, "username": ""},
                        "rental_date": "2025-06-24",
                        "return_date": "2025-07-20",
                        "is_returned": False,
                        "book": 1,
                    }
                ],
            },
        )

    def test_rental_create(self):
        url = reverse("rental:rental_list")
        data = {"rental_date": "2025-06-24", "return_date": "2025-07-20"}
        request = self.client.get(url, data)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(Rental.objects.all().count(), 1)

    def test_rental_destroy(self):
        url = reverse("rental:rental_delete", args=(self.rental.pk,))
        request = self.client.delete(url)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Rental.objects.all().count(), 0)
