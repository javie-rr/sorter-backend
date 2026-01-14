from rest_framework.routers import DefaultRouter
from organization_types.api.views import OrganizationTypeViewSet

router_organization_types = DefaultRouter(trailing_slash=False)
router_organization_types.register(r'organization-types', OrganizationTypeViewSet, basename='organization_types')
