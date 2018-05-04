from django.shortcuts import render
from django.contrib.auth.models import User
from profiles.models import UserProfile
from rest_framework import routers, serializers, viewsets



class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
    class Meta:
        model = User
        fields = ('url', 'username')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()

	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'gender', 'city', 'date_of_birth', 'university', 'gpa','experience','user')
