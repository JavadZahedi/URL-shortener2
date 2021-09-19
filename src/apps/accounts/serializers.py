from django.contrib.auth import get_user_model

from rest_framework import serializers

# Create your views here.

UserModel = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = (
            'id', 'username', 'password', 'email', 'first_name', 'last_name',
        )


class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = '__all__'