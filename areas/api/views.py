from rest_framework.viewsets import ModelViewSet
from areas.models import Area
from areas.api.serializers import AreaSerializer
from rest_framework.response import Response

class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "areas": serializer.data
        })