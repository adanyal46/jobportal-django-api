from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['image', 'first_name', 'last_name', 'email', 'password', 'role']
  
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            role=validated_data['role'],
            image=validated_data.get('image')
        )
        return user
    
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'],password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid login credentials")