from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from library.models import Book, Genre
from rental.models import Rental
from users.models import User


class RentalTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@yandex.ru', is_staff=True)
        self.author = Author.objects.create(name='Сергей Александрович Есенин',
                                            date_of_birth='1895-09-21')
        self.genre = Genre.objects.create(name='Поэзия')
        self.book = Book.objects.create(
            title='Береза',
            author=self.author,
            author_id=self.author.pk,
            genre=self.genre,
            count=1
        )
        self.rental = Rental.objects.create(
            rental_date="2025-06-22",
            return_date="2025-07-20",
            user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_rental_list(self):
        url = reverse('rental:rental_list')
        request = self.client.get(url)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [{
            "id": 1, "user": {"id": 1, "username":''},
            "rental_date": "2025-06-22",
            "return_date": "2025-07-20",
            "is_returned": False,
            "book": 1}]})


    def test_rental_create(self):
        url = reverse("rental:rental_list")
        data = {"rental_date":"2025-06-22", "return_date":"2025-07-20"}
        request = self.client.get(url, data)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(Rental.objects.all().count(), 1)

    def test_rental_destroy(self):
        url = reverse('rental:rental_delete', args=(self.rental.pk,))
        request = self.client.delete(url)

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Rental.objects.all().count(), 0)

