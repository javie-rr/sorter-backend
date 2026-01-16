from rest_framework import serializers
from organization_types.models import OrganizationType

class OrganizationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationType
        fields = "__all__"