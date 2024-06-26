from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    #GET : 아무나, PUT / PATCH : 본인만
    def has_obejct_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user