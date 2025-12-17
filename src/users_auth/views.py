from django.db import IntegrityError
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    # Функция нам не нужна, но с ней удобнее тестировать, сразу видно какие поля заполнять
    # def get(self, request):
    #     serializer = RegisterSerializer()
    #     return Response(serializer.data)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                data = serializer.create(serializer.validated_data)
                return Response(
                    {
                        "access_token": data["access"],
                        "refresh_token": data["refresh"],
                    },
                    status=status.HTTP_201_CREATED,
                )
            except IntegrityError:
                return Response(
                    {"error": "Username already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            serializer.is_valid(raise_exception=True)

            token_data = serializer.validated_data

            return Response(
                {
                    "access_token": token_data.get("access"),
                    "refresh_token": token_data.get("refresh"),
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:

            return Response(
                {"error": "Invalid username or password."},
                status=status.HTTP_400_BAD_REQUEST,
            )
