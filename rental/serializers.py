from rest_framework import serializers

from library.models import Book
from library.serializers import BookListSerializer
from rental.models import Rental
from users.models import User
from users.serializers import UserListSerializer


class RentalSerializer(serializers.ModelSerializer):
    books = BookListSerializer(read_only=True)
    user = UserListSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='library', write_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='users', write_only=True)

    class Meta:
        model = Rental
        fields = [
            'id',
            'rental_date',
            'return_date',
            'book_id',
            'books',
            'user_id',
            'user'
        ]


class RentalCreateSerializer(RentalSerializer):
    class Meta(RentalSerializer.Meta):
        fields = [
            'rental_date',
            'return_date',
            'book_id',
            'user_id'
        ]
