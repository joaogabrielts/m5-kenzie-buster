from rest_framework import status, generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
