from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """
    Проверяет является ли юзер автором
    """
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
