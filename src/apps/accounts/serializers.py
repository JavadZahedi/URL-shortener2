from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

# Create your views here.

UserModel = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, label='گذرواژه')

    class Meta:
        model = UserModel
        fields = (
            'id', 'username', 'password', 'email', 'first_name', 'last_name',
        )

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data.keys():
            user.set_password(validated_data['password'])
            user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'last_login', 'is_superuser', 'is_staff', 'is_active',
            'date_joined', 'user_permissions', 'groups'
        )


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label='گذرواژه')
    password_confirm = serializers.CharField(label='تکرار گذرواژه')

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')

    def validate(self, data):
        if data.get('password') != data.get('password_confirm'):
            raise serializers.ValidationError({
                'password_confirm': _('گذرواژه و تکرار آن با هم برابر نیستند')
            })
