from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from library.models import Book, Genre
from users.models import User


class AuthorTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@yandex.ru", is_staff=True)
        self.author = Author.objects.create(
            name="Сергей Александрович Есенин", date_of_birth="1895-09-21"
        )
        """self.genre = Genre.objects.create(name='Поэзия', description='')
        self.book = Book.objects.create(
            {"title": "Береза",
            "author": self.author,
            "author_id": self.author.pk,
            "genre": self.genre.pk,
            "count": 6}
        )"""
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
