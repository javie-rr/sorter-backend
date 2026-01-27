from core.views import BaseViewSet
from organization_types.models import OrganizationType
from organization_types.api.serializers import OrganizationTypeSerializer

class OrganizationTypeViewSet(BaseViewSet):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeSerializer
    response_key = "organization_types"