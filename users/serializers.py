from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("is_staff", "is_superuser", "groups", "user_permissions")


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username"]


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, users):
        token = super().get_token(users)

        # Добавление пользовательских полей в токен
        token["username"] = users.username
        token["email"] = users.email

        return token
