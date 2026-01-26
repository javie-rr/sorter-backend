from rest_framework import serializers
from areas.models import Area

class AreaSerializer(serializers.ModelSerializer):
    # subareas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Area
        fields = '__all__'