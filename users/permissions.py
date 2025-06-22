from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Определяет и разрешает доступ только владельцу или администратору"""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
