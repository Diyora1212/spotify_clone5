from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.user.models import User
from apps.user.utils import generate_token
import os
from apps.user.api_endpoints.User.UserCreate.serializers import UserCreateSerializer, ForgotPasswordSerializer


class UserCreateView(APIView):
    def post(self, request):
        serailizer = UserCreateSerializer(data=request.data)
        serailizer.avatar = request.FILES['avatar']
        serailizer.is_valid(raise_exception=True)
        serailizer.save()
        return Response(data={'detail': "Check your inbox we have sent an activation link"})
    # queryset = User.objects.all()
    # serializer_class = UserCreateSerializer
    # parser_classes = [MultiPartParser, FormParser, JSONParser]


class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        user.userprofile.email = email
        user.token = generate_token()
        host_email = os.getenv("EMAIL_HOST_USER")
        activation_link = f"http://localhost:8000/api/v1/user/user-activate/{user.token}"

        send_mail(
            'Reset Password',
            f'Click the link to reset your password: {activation_link}',
            (host_email,),
            [user.userprofile.email],
            fail_silently=False,
        )
        return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)



class ResetPasswordView(APIView):
    def post(self, request):
        activation_token = request.data.get('activation_token')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        if not generate_token(activation_token):
            return Response({'error': 'Invalid activation token.'}, status=400)

        if password1 != password2:
            return Response({'error': 'Passwords do not match.'}, status=400)

        user = generate_token(activation_token)
        user.set_password(password1)
        user.save()

        return Response({'message': 'Password reset successfully.'})


__all__ = ('UserCreateView', 'ForgotPasswordAPIView', 'ResetPasswordView')
