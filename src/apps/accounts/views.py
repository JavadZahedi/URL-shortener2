import json

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly)

from .serializers import (
    UserListSerializer, UserDetailSerializer, RegistrationSerializer)
from .permissions import IsOwner
from core.customs.viewsets import CustomModelViewSet

from apps.accounts import serializers

# Create your views here.

UserModel = get_user_model()

class UserViewSet(CustomModelViewSet):
    queryset = UserModel.objects.all()
    serializer_classes = {
        'retrieve': UserDetailSerializer,

        'default': UserListSerializer
    }
    permission_classes = {
        'create': (IsAdminUser,),
        'list': (IsAdminUser,),
        'default': (IsAdminUser|IsOwner,)
        # 'default': (AllowAny,)
    }


class SetCSRFCookieView(View):
    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        return JsonResponse({'detail': 'CSRF cookie set'})


class RegistrationView(View):
    def post(self, request):
        request_data = json.loads(request.body)
        serializer = RegistrationSerializer(request_data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return JsonResponse({'detail': 'Success'})
        else:
            return JsonResponse(serializer.errors, status=400)
        

class LoginView(View):
    def post(self, request):
        request_data = json.loads(request.body)
        username = request_data.get('username')
        password = request_data.get('password')
        print(f'username: {username}, password: {password}')

        if username is None or password is None:
            print('OK')
            data = {'detail': 'Both "username" and "password" are required'}
            return JsonResponse(data, status=400)

        user = authenticate(username=username, password=password)

        if user is None:
            data = {'detail': 'Invalid credentials'}
            return JsonResponse(data, status=400)

        if not user.is_active:
            data = {'detail': 'Your account is not active'}
            return JsonResponse(data, status=400)

        login(request, user)
        return JsonResponse({'detail': 'Success'})


class LogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({'detail': 'Success'})
