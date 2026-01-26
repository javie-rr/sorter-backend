from rest_framework.routers import DefaultRouter
from areas.api.views import AreaViewSet

router_areas = DefaultRouter(trailing_slash=False)
router_areas.register(f'areas', AreaViewSet, basename='areas')