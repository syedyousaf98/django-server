from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileBase(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT, related_name="%(class)s_profile")
    # `%(class)s` is a placeholder that get replaced with the current model class name where the field is defined
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="%(class)s_created")
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="%(class)s_updated")

    class Meta:
        abstract = True # django does not create database table for abstract models


class Admin(ProfileBase):
    admin_id = models.BigAutoField(primary_key=True)


class Doctor(ProfileBase):
    doctor_id = models.BigAutoField(primary_key=True)



