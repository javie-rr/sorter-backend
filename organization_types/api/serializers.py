from rest_framework import serializers
from organization_types.models import OrganizationType
# from organizations.api.serializers import OrganizationSerializer

class OrganizationTypeSerializer(serializers.ModelSerializer):
    
    # organizations = OrganizationSerializer(many=True)

    class Meta:
        model = OrganizationType
        fields = "__all__"