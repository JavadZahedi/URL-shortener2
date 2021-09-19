from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly)

from .serializers import UserListSerializer, UserDetailSerializer
from .permissions import IsOwner
from core.customs import CustomModelViewSet

# Create your views here.
# django.contrib.auth.models

UserModel = get_user_model()

class UserViewSet(viewsets.CustomModelViewSet):
    queryset = UserModel.objects.all()
    serializer_classes = {
        'list': UserListSerializer,
        'default': UserDetailSerializer
    }
    permission_classes = {
        'create': (AllowAny,),
        'list': (IsAdminUser,),
        'default': (IsAdminUser|IsOwner)
    }
