from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group
from .models import TestLocation
from .serializers import UserSerializer, GroupSerializer, TestLocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class TestLocationViewSet(viewsets.ModelViewSet):
    queryset = TestLocation.objects.all()
    serializer_class = TestLocationSerializer