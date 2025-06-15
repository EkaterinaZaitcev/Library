from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from library.models import Book
from library.paginators import BooksPaginator
from library.serializers import BookSerializer
from users.permissions import IsOwnerOrAdmin


class BookCreateAPIView(generics.CreateAPIView):
    """Создание новой книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    pagination_class = BooksPaginator
    """Фильтрация и поиск"""
    filter_backends = [filters.DjangoFilterBackend, ]
    filters_fields = ['author', 'title', 'genre']
    search_fields = ['author', 'title']

class BookListAPIView(generics.ListAPIView):
    """Список всех книг"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny]

class BookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

class BookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

class BookDestroyAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
