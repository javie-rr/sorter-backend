from rest_framework.viewsets import ModelViewSet
from organization_types.models import OrganizationType
from organization_types.api.serializers import OrganizationTypeSerializer

class OrganizationTypeViewSet(ModelViewSet):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeSerializer