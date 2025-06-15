from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from library.models import Book
from rental.models import Rental
from rental.paginators import RentalPagination
from rental.serializers import RentalSerializer
from users.permissions import IsOwnerOrAdmin


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    pagination_class = RentalPagination

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = request.data
        book = Book.objects.get(id=data['book_id'])
        #Проверка наличия книг
        if book.count == 0:
                raise ValidationError(f'Книга {book.title} отсутствует в библиотеке.')

        response = super().create(request, *args, **kwargs)
        #Уменьшаем количество книг после выдачи
        book.count -= 1
        book.save()

        # Проверка количества книг
        if book.count == 2:
            return Response(
                {f'Книга {book.title} выдана {data}. Осталось 2 экземпляра.'},
                status=status.HTTP_201_CREATED,
            )
        return response

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        updating = self.get_object()

        #Проверка на возврат книги
        if "return_date" in request.data and request.data['return_date']:
            if not updating.return_date:
                updating.book.count += 1
                updating.book.save()

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == ['list', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated(), IsOwnerOrAdmin()]
