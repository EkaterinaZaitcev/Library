from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rental.apps import RentalConfig
from rental.views import RentalViewSet


router = DefaultRouter()
router.register(r"", RentalViewSet)

app_name = RentalConfig.name

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += router.urls
