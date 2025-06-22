from drf_yasg.utils import swagger_auto_schema

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer, UserTokenObtainPairSerializer


@swagger_auto_schema(
    tags=["4. Пользователи"],
    operation_description="CREATE",
    responses={200: UserSerializer(many=True)},
)
class UserCreateAPIView(CreateAPIView):
    """Регистрация нового пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


@swagger_auto_schema(
    tags=["4. Пользователи"],
    operation_description="LIST",
    responses={200: UserSerializer(many=True)},
)
class UserListAPIView(ListAPIView):
    """Для просмотра списка профилей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


@swagger_auto_schema(
    tags=["4. Пользователи"],
    operation_description="UPDATE",
    responses={200: UserSerializer(many=True)},
)
class UserUpdateAPIView(UpdateAPIView):
    """Изменение профиля пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner]


@swagger_auto_schema(
    tags=["4. Пользователи"],
    operation_description="RETRIEVE",
    responses={200: UserSerializer(many=True)},
)
class UserRetrieveAPIView(RetrieveAPIView):
    """Просмотр пользователя по ID"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser | IsOwner]


class UserTokenObtainPairView(TokenObtainPairView):
    """Получение токена"""

    serializer_class = UserTokenObtainPairSerializer
