from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets

from .serializers import UserSerializer

# Create your views here.
# django.contrib.auth.models

UserModel = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
