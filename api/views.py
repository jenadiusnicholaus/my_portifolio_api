
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ProjectSerializer, ContactSerializer
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be viewed.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContactsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contact to be posted.
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


