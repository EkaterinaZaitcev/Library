from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer, UserTokenObtainPairSerializer

@swagger_auto_schema(tags=['4. Пользователи'], operation_description="CREATE", responses={200: UserSerializer(many=True)})
class UserCreateAPIView(CreateAPIView):
    """ Регистрация нового пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data["password"])
        user.is_active = True
        user.save()

@swagger_auto_schema(tags=['4. Пользователи'], operation_description="LIST", responses={200: UserSerializer(many=True)})
class UserListAPIView(ListAPIView):
    """ Для просмотра списка профилей """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

@swagger_auto_schema(tags=['4. Пользователи'], operation_description="UPDATE", responses={200: UserSerializer(many=True)})
class UserUpdateAPIView(UpdateAPIView):
    """ Изменение профиля пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

@swagger_auto_schema(tags=['4. Пользователи'], operation_description="RETRIEVE", responses={200: UserSerializer(many=True)})
class UserRetrieveAPIView(RetrieveAPIView):
    """ Просмотр пользователя по ID """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserTokenObtainPairView(TokenObtainPairView):
    """ Получение токена """
    serializer_class = UserTokenObtainPairSerializer
