from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from .models import Admin, Doctor, ProfileBase


User = get_user_model()


class ProfileBaseSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    middle_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=255)
    birth_date = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    updated_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())


class CreateAdminSerializer(ProfileBaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = list(ProfileBaseSerializer().get_fields().keys()) + []


