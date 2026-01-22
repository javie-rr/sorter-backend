from rest_framework.viewsets import ModelViewSet
from area_types.models import AreaType
from area_types.api.serializers import AreaTypeSerializer
from rest_framework.response import Response

class AreaTypeViewSet(ModelViewSet):
    queryset = AreaType.objects.all()
    serializer_class = AreaTypeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "area_types": serializer.data
        })