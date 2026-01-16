from rest_framework.routers import DefaultRouter
from organizations.api.views import OrganizationViewSet

router_organizations = DefaultRouter(trailing_slash=False)
router_organizations.register(r'organizations', OrganizationViewSet, basename='organizations')