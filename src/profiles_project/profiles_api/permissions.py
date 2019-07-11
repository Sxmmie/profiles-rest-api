# permissions module contains all the base permissions classes in the django rest framework
from rest_framework import permissions


# Inherits from BasePermission class in rest_framework
class UpdateOwnProfile(permissions.BasePermission):
    """Allows users to edit their own profile"""

    # this function is called every time a request is made to the API
    # result determines whether user has permission or not (boolean true or false)
    def has_object_permission(self, request, view, obj):
        """check user us trying to edit their own profile"""

        # Allow users to view any profile in the system (A non-destructive method, HTTP GET) - permissions.save()
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if user is updating their own profile
        # compare obj.id is the user.id (profile id)
        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow users to update own status"""

    # check if user has permissions to perform this action
    def has_object_permission(self, request, view, obj):
        """check user us trying to edit their own status and not other people's status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        # check the user_profile.id of the status item they're trying to update matches the request.user.id whixh is the same as the logged in user.
        return obj.user_profile.id == request.user.id
