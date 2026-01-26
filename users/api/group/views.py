from django.contrib.auth.models import Group
from rest_framework import viewsets
from users.api.group.serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet): 
    queryset = Group.objects.all() 
    serializer_class = GroupSerializer