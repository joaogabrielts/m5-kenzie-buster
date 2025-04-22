from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import User
from .serializers import UserSerializer

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs["user_id"]
        request_user = self.request.user

        # Verificação de permissões para visualização
        user = User.objects.get(id=user_id)
        if not request_user.is_employee and request_user != user:
            raise PermissionDenied("You do not have permission to access this user.")

        return user


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs["user_id"]
        request_user = self.request.user

        # Verificação de permissões para atualização
        user = User.objects.get(id=user_id)
        if not request_user.is_employee and request_user != user:
            raise PermissionDenied("You do not have permission to update this user.")

        return user
