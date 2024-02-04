from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ConfirmCode


class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserAuthSerializer(UserBaseSerializer):
    pass


class UserCreateSerializer(UserBaseSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class ConfirmationSerializer(serializers.Serializer):
    class Meta:
        model = ConfirmCode

