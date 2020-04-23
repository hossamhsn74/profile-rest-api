from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
        allow user to edit only his own profile, cutom permission class 
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """ allow user to update only his own status """

    def has_object_permission(self, request, view, obj):
        """  check if the user is trying to update his own status """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
