from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rental.models import Rental
from rental.paginators import RentalPagination
from rental.serializers import RentalSerializer
from rental.services import return_book
from users.permissions import IsOwner


@swagger_auto_schema(
    operation_description="GET", responses={200: RentalSerializer(many=True)}
)
class RentalListApiView(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    pagination_class = RentalPagination
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]

    def get_queryset(self):
        if IsAdminUser.has_permission(self.request.user, self.request, self):
            return Rental.objects.all()
        else:
            return Rental.objects.filter(user=self.request.user)


@swagger_auto_schema(
    operation_description="POST", responses={201: RentalSerializer(many=True)}
)
class RentalCreateApiView(generics.CreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def perform_create(self, serializer):
        data = serializer.save(user=self.request.user)
        if data.is_available:
            if data.count >= 0:
                data.count -= 1
                data.save()
            else:
                data.is_available = False
                data.save()
                return data
        else:
            raise ValidationError(f"Книга {data.title} отсутствует в наличии.")


@swagger_auto_schema(
    operation_description="GET", responses={200: RentalSerializer(many=True)}
)
class RentalRetrieveApiView(generics.RetrieveAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAdminUser, IsOwner]


@swagger_auto_schema(
    operation_description="GET", responses={200: RentalSerializer(many=True)}
)
class RentalUpdateApiView(generics.UpdateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAdminUser, IsOwner]

    def perform_update(self, serializer):
        data = serializer.save()
        book = data.book
        return_book(data, book)
        data.save()


@swagger_auto_schema(
    operation_description="GET", responses={200: RentalSerializer(many=True)}
)
class RentalDestroyApiView(generics.DestroyAPIView):
    queryset = Rental.objects.all()
    permission_classes = [IsAdminUser, IsOwner]
