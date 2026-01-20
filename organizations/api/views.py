from rest_framework.viewsets import ModelViewSet
from organizations.models import Organization
from organizations.api.serializers import OrganizationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.select_related("registration", "organization_type")
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        queryset = self.queryset
        is_active = self.request.query_params.get('is_active')

        if self.action in ['destroy','activate']:
            return queryset
        # Filter by default active organizations
        if is_active is None:
            return queryset.filter(registration__is_active=True)
        # Allows filtering active/inactive via query param
        return queryset.filter(registration__is_active=is_active.lower() == 'true')
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "organizations": serializer.data
        })
    
    def destroy(self, request, *args, **kwargs):
        organization = self.get_object()
        organization.registration.is_active = False
        organization.registration.save()

        return Response(
            {"detail": "Organización desactivado"},
            status=status.HTTP_204_NO_CONTENT
        )
    
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        organization = self.get_object()
        registration = organization.registration
        registration.is_active = True
        registration.save()

        return Response(
            {"detail": "Organización activado"}, 
            status=status.HTTP_200_OK
        )