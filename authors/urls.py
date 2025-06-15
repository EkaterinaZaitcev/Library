from django.urls import include, path
from rest_framework.routers import DefaultRouter

from authors.apps import AuthorsConfig
from authors.views import AuthorViewSet


router = DefaultRouter()
router.register(r"", AuthorViewSet)

app_name = AuthorsConfig.name

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += router.urls