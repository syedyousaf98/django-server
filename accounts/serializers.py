from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User with this email already exist.')
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

