# custom permissions that extend from drf's base permission class
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):       # extends from drf's BasePermission
    
    def has_object_permission(self, request, view, obj):    # override has_object_permission
        if request.method in permissions.SAFE_METHODS:      # if request are GET, OPTIONS, or HEAD (non-edting HTTP methods), perm is granted
            return True

        return obj.author == request.user           # author has to be user for other requests
        