from core.views import BaseViewSet
from area_types.models import AreaType
from area_types.api.serializers import AreaTypeSerializer

class AreaTypeViewSet(BaseViewSet):
    queryset = AreaType.objects.all()
    serializer_class = AreaTypeSerializer
    response_key = "area_types"