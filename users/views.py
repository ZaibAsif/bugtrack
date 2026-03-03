from rest_framework import generics, status, views, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema, OpenApiExample
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework.fields import CharField, IntegerField, URLField

from .serializers import SignUpSerializer, LoginSerializer, UserCreateSerializer, AuthResponseSerializer, UserRoleSerializer
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(tags=["Authentication"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = serializer.save()

@extend_schema(tags=["Users"], summary="Change user role (admin only)")
class ChangeUserRoleView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return User.objects.all()
class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        tags=["Authentication"],
        request=LoginSerializer,
        responses={
            200: inline_serializer(
                name="LoginResponse",
                fields={
                    'token': CharField(),
                    'user_id': IntegerField(),
                    'name': CharField(),
                    'email': CharField(),
                    'avatar': URLField(allow_null=True),
                }
            ),
            400: CharField(),
        },
        description="Login with email and password to receive an authentication token."
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'name': user.full_name,
                'email': user.email,
                'avatar': user.avatar_url,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

