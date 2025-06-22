from django.urls import path
from rental.apps import RentalConfig
from rental.views import (
    RentalListApiView,
    RentalCreateApiView,
    RentalUpdateApiView,
    RentalRetrieveApiView,
    RentalDestroyApiView,
)

app_name = RentalConfig.name

urlpatterns = [
    path("list/", RentalListApiView.as_view(), name="rental_list"),
    path("create/", RentalCreateApiView.as_view(), name="rental_create"),
    path("update/<int:pk>/", RentalUpdateApiView.as_view(), name="rental_update"),
    path("retrieve/<int:pk>/", RentalRetrieveApiView.as_view(), name="rental_retrieve"),
    path("delete/<int:pk>/", RentalDestroyApiView.as_view(), name="rental_delete"),
]
