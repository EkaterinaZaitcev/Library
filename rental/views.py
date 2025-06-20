from rest_framework import  generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rental.models import Rental
from rental.paginators import RentalPagination
from rental.serializers import RentalSerializer
from rental.services import return_book
from users.permissions import IsOwnerOrAdmin


class RentalListApiView(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    pagination_class = RentalPagination
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if IsAuthenticated.has_permission():
            return Rental.objects.all()
        else:
            return Rental.objects.filter(user=self.request.user)


class RentalCreateApiView(generics.CreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def perform_create(self, serializer):
        data = serializer.save(user=self.request.user)
        if data.is_available:
            if data.count >= 0:
                data.count -=1
                data.save()
            else:
                data.is_available = False
                data.save()
                return data
        else:
            raise ValidationError(f"Книга {data.title} отсутствует в наличии.")


class RentalRetrieveApiView(generics.RetrieveAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class RentalUpdateApiView(generics.UpdateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_update(self, serializer):
        data = serializer.save()
        book = data.book
        return_book (data, book)
        data.save()


class RentalDestroyApiView(generics.DestroyAPIView):
    queryset = Rental.objects.all()
    permission_classes = [IsAdminUser,]

    def get_permissions(self):
        if self.action == ['list', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated(), IsOwnerOrAdmin()]
