from rest_framework.routers import DefaultRouter
from users.api.group.views import GroupViewSet

router_groups = DefaultRouter(trailing_slash=False)
router_groups.register(r'groups', GroupViewSet, basename='groups')