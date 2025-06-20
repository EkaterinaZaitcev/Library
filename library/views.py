from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from library.models import Book
from library.paginators import BooksPaginator
from library.serializers import BookSerializer
from users.permissions import IsOwnerOrAdmin


@swagger_auto_schema(tags=['2. Библиотека'], operation_description="POST",
                     responses={200: BookSerializer(many=True)})
class BookCreateAPIView(generics.CreateAPIView):
    """Создание новой книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    pagination_class = BooksPaginator
    """Фильтрация и поиск"""
    filter_backends = [filters.DjangoFilterBackend]
    filters_fields = ['author', 'title', 'genre']
    search_fields = ['author', 'title','genre']


@swagger_auto_schema(tags=['2. Библиотека'], operation_description="GET", responses={200: BookSerializer(many=True)})
class BookListAPIView(generics.ListAPIView):
    """Список всех книг"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny]


@swagger_auto_schema(tags=['2. Библиотека'], operation_description="PATCH", responses={200: BookSerializer(many=True)})
class BookRetrieveAPIView(generics.RetrieveAPIView):
    """Информация о книге"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


@swagger_auto_schema(tags=['2. Библиотека'], operation_description="PUT", responses={200: BookSerializer(many=True)})
class BookUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о книге"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


@swagger_auto_schema(tags=['2. Библиотека'], operation_description="DELETE", responses={200: BookSerializer(many=True)})
class BookDestroyAPIView(generics.DestroyAPIView):
    """Удаление книги"""
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
