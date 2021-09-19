from django.contrib.auth import get_user_model

from rest_framework import serializers

# Create your views here.

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = [
            'pk', 'username', 'password', 'email', 'first_name', 'last_name',
        ]
        write_only_fields = ['password',]