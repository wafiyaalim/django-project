# api/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import TelegramUser

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'message': 'This is a public endpoint'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': f'Hello {request.user.username}! This is a protected endpoint'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_telegram_users(request):
    users = TelegramUser.objects.all().values('username', 'created_at')
    return Response(list(users))