# users/permissions.py
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    Assumes the model instance has an `owner` field.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in ['GET','PUT','DELETE','PATCH', 'HEAD', 'OPTIONS']:
            return True
        
        # Write permissions are only allowed to the owner of the object
        return obj.owner == request.user
