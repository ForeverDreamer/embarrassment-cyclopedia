from rest_framework import permissions


# class IsLogout(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         user = request.user
#         if user.is_authenticated():
#             if user.profile.logout:
#                 return True
#         return False


class IsLogin(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        try:
            if user.profile and not user.profile.logout:
                return True
        except:
            return False
        return False
