from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly)

from .serializers import UserListSerializer, UserDetailSerializer
from .permissions import IsOwner

# Create your views here.
# django.contrib.auth.models

UserModel = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializers = {
        'list': UserListSerializer,
        'default': UserDetailSerializer
    }
    permission_classes = {
        'create': (AllowAny,),
        'list': (IsAdminUser,),
        'default': (IsAdminUser|IsOwner)
    }

    def get_permissions(self):
        default_classes = self.permission_classes['default']
        classes = self.permission_classes.get(self.action, default_classes)
        return [permission() for permission in classes]

    def get_serializer_class(self):
        default_serializer = self.serializers['default']
        return self.serializers.get(self.action, default_serializer)
