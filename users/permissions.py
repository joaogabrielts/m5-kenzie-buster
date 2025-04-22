from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_employee

class IsOwnerOrEmployee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_employee
