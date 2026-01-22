from rest_framework.routers import DefaultRouter
from area_types.api.views import AreaTypeViewSet

router_area_types = DefaultRouter(trailing_slash=False)
router_area_types.register(r'area-types', AreaTypeViewSet, basename='area_types')