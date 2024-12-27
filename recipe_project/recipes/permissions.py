from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to allow only the owner of a recipe to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
