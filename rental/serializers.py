from django.utils import timezone
from rest_framework import serializers
from rental.models import Rental
from users.serializers import UserListSerializer


class RentalSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    rental_date = serializers.DateField(read_only=True, default=timezone.now)

    class Meta:
        model = Rental
        fields = "__all__"
