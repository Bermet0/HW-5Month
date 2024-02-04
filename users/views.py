from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserCreateSerializer, ConfirmationSerializer
from users import serializers
from random import choice


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = request.data.get('username')
    password = request.data.get('password')

    code = ''.join(choice('0123456789') for _ in range(6))

    user = User.objects.create_user(username=username, password=password,
                                    is_active=False)
    user.code = code
    user.save()

    return Response({code},
                    status=status.HTTP_201_CREATED)


@api_view(['POST'])
def confirm_api_view(request):
    serializer = ConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = request.data.get('code')
    try:
        user = User.objects.get(code=code)
    except User.DoesNotExist:
        return Response({'error': 'Invalid confirmation code'},
                        status=status.HTTP_400_BAD_REQUEST)

    user.is_active = True
    user.save()

    return Response({'success': 'User confirmed successfully'},
                    status=status.HTTP_200_OK)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = serializers.UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)  # username=admin, password=123

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



