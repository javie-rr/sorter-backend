from core.views import BaseViewSet
from areas.models import Area
from areas.api.serializers import AreaSerializer

class AreaViewSet(BaseViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    response_key = "areas"