from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('create_admin_profile', views.create_admin_profile)
]