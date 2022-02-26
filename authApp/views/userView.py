from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import PasswordField, TokenObtainPairSerializer
from authApp.models.user import User
from rest_framework import generics

from authApp.serializers.userSerializer import UserSerializer

class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()              
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()              
    serializer_class = UserSerializer