from rest_framework import serializers

from authors.models import Author
from library.serializers import BookListSerializer


class AuthorSerializer(serializers.ModelSerializer):
    books = BookListSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'preview', 'date_of_birth', 'books',]


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
