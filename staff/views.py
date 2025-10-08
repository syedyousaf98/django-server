from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from .serializers import CreateAdminSerializer


@swagger_auto_schema(methods=['post'], request_body=CreateAdminSerializer, tags=['User'])
@api_view(['POST'])
def create_admin_profile(request):
    serializer = CreateAdminSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_200_OK)