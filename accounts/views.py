from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.shortcuts import reverse, get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserRegisterSerializer
from .utils.email import send_activation_mail
from .utils.tokens import activation_token_generator, valid_activation_token


User = get_user_model()


class UserRegisterView(APIView):
    @swagger_auto_schema(request_body=UserRegisterSerializer, tags=["auth"])
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = activation_token_generator(user.pk)
        abs_url = reverse('accounts:activation', kwargs={'token': token})
        activation_link = request.build_absolute_uri(abs_url)

        send_activation_mail(
            recipient=user.email,
            subject="Activate your account",
            html_content=activation_link
        )

        return Response(
            {"detail": "User registered successfully. Please check your email to activate your account."},
            status=status.HTTP_201_CREATED
        )


class UserActivationView(APIView):
    @swagger_auto_schema(
        tags=["auth"],
        responses={
            200: "User successfully activated or already active",
            400: "Invalid or expired activation link"
        }
    )
    def post(self, request, token):
        user_id = valid_activation_token(token)
        if not user_id:
            return Response({"detail": "Invalid or expired activation link"}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, pk=user_id)
        if user.is_active:
            return Response({"detail": "User already activated"}, status=status.HTTP_200_OK)

        user.is_active = True
        user.save()

        return Response({"detail": "User successfully activated"}, status=status.HTTP_200_OK)
