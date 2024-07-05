from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import User, Friend
from .serializers import UserSerializer, FriendSerializer
from .permissions import IsOwnerOrReadOnly 

class UserViewSet(viewsets.ModelViewSet):       # this includes for the CRUD operations
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly] 

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsOwnerOrReadOnly] 


