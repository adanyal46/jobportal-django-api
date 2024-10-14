from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


# Registration View
class RegisterView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                 'user': {
                    'id': user.id,
                    'email': user.email,
                    'role': user.role,
                    'first_name': user.first_name,
                    'image': user.image.url if user.image else None
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login View
class LoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                 'user': {
                    'id': user.id,
                    'email': user.email,
                    'role': user.role,
                    'first_name': user.first_name,
                    'image': user.image.url if user.image else None
                }
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)