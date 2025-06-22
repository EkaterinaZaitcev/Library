from django.urls import path

from .apps import LibraryConfig
from .views import (BookCreateAPIView, BookDestroyAPIView,
                    BookListAPIView, BookRetrieveAPIView, BookUpdateAPIView)

app_name = LibraryConfig.name

urlpatterns = [

    path('list/', BookListAPIView.as_view(), name="books_list"),
    path('create/', BookCreateAPIView.as_view(), name="books_create"),
    path('update/<int:pk>/', BookUpdateAPIView.as_view(), name="books_update"),
    path('retrieve/<int:pk>/', BookRetrieveAPIView.as_view(), name="books_retrieve"),
    path('delete/<int:pk>/', BookDestroyAPIView.as_view(), name="books_delete"),

]
