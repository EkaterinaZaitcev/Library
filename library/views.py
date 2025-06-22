from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from library.models import Book
from library.paginators import BooksPaginator
from library.serializers import BookSerializer


@swagger_auto_schema(operation_description="POST",
                     responses={201: BookSerializer(many=True)})
class BookCreateAPIView(generics.CreateAPIView):
    """Создание новой книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAdminUser]
    pagination_class = BooksPaginator
    """Фильтрация и поиск"""
    filter_backends = [filters.DjangoFilterBackend]
    filters_fields = ['author', 'title']
    search_fields = ['author', 'title']


@swagger_auto_schema(operation_description="GET", responses={200: BookSerializer(many=True)})
class BookListAPIView(generics.ListAPIView):
    """Список всех книг"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny]


@swagger_auto_schema(operation_description="PATCH", responses={200: BookSerializer(many=True)})
class BookRetrieveAPIView(generics.RetrieveAPIView):
    """Информация о книге"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny]


@swagger_auto_schema(operation_description="PUT", responses={200: BookSerializer(many=True)})
class BookUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о книге"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAdminUser]


@swagger_auto_schema(operation_description="DELETE", responses={200: BookSerializer(many=True)})
class BookDestroyAPIView(generics.DestroyAPIView):
    """Удаление книги"""
    queryset = Book.objects.all()
    permission_classes = [IsAdminUser]
