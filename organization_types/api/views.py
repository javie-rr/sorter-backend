from rest_framework.viewsets import ModelViewSet
from organization_types.models import OrganizationType
from organization_types.api.serializers import OrganizationTypeSerializer
from rest_framework.response import Response

class OrganizationTypeViewSet(ModelViewSet):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "organization_types": serializer.data
        })