from rest_framework import serializers
from .models import TestLocation
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TestLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestLocation
        fields = '__all__'