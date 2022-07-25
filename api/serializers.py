from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = ('id','name',)

class ProjectSerializer(serializers.ModelSerializer):
    techonologies = TechnologiesSerializer(many=True)

    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'featured', 'image', 'technologies', 'link_to_live_version','link_to_source']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'name', 'email', 'message']
