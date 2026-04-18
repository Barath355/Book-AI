from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only
        if request.method in ['GET']:
            return True

        # Write only if owner
        return obj.user == request.user