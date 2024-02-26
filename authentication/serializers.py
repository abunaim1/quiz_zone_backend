from django.contrib.auth.models import User
from rest_framework import serializers
from . import models
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Participant
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    image = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'image']

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)

        if password != confirm_password:
            raise serializers.ValidationError({'error': 'Password does not match'})
        return data
    
    def create(self, validated_data):
        image = validated_data.pop('image', None)
        user = User.objects.create_user(**validated_data)
        if image:
            image = default_storage.save(image.name, ContentFile(image.read()))
            user.image = image
        user.is_active = False
        user.save()
        return user
    
    # def save(self):
    #     username = self.validated_data['username']
    #     first_name = self.validated_data['first_name']
    #     last_name = self.validated_data['last_name']
    #     email = self.validated_data['email']
    #     password1 = self.validated_data['password']
    #     password2 = self.validated_data['confirm_password']

    #     if password1 != password2:
    #         raise serializers.ValidationError({'error' : 'Password does not matched'})
        
    #     if User.objects.filter(email=email).exists():
    #         raise serializers.ValidationError({'error' : 'This email already exist!'})
        
    #     image = self.validated_data.get('image')
    #     if image:
    #         file_name = default_storage.save(image.name, ContentFile(image.read()))
    #         account.image = file_name

    #     account = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)

    #     account.is_active = False
    #     account.save()
    #     return account
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
