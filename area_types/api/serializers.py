from rest_framework import serializers
from area_types.models import AreaType

class AreaTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AreaType
        fields = "__all__"