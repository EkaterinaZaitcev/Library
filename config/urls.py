from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', include('authors.urls', namespace='authors')),
    path('library/', include('library.urls', namespace='library')),
    path('rental/', include('rental.urls', namespace='rental')),
    path('users/', include('users.urls', namespace='users')),

]