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
        self.rental = Rental.objects.create(
            rental_date="2025-06-20",
            return_date="2025-07-20",
            user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_rental_list(self):
        url = reverse('rental:rental_list')
        request = self.client.get(url)
        response = request.json()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response, [{
            "id": self.rental.pk,
            "rental_date": "2025-06-20",
            "return_date": "2025-07-20",
            "user": {
                "id": self.user.id,
                "username": ""
            },
        },],)

   """def test_rental_create(self):
        url = reverse("rental:rental_list")
        data = {"rental_date":"2025-06-10", "return_date":"2025-07-10"}
        request = self.client.get(url, data)
        print(request)

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rental.objects.all().count(), 2)"""
