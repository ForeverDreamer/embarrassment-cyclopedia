from rest_framework import permissions

from ec import config


class IsBindPhone(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.username == config.TEMP_USER_INFO.get('username'):
            return False
        return True
