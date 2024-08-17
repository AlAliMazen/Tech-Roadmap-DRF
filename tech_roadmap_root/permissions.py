from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    used to allow only the owner of the profile edit his/her profile
    but can see all available profiles and follow them
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user