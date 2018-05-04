from django.shortcuts import render
from django.contrib.auth.models import User
from profiles.models import UserProfile
from rest_framework import routers, serializers, viewsets
from apiapp.serializers import UserSerializer, ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = ProfileSerializer