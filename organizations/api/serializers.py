from rest_framework import serializers
from organizations.models import Organization, OrganizationRegistration
from django.db import transaction

class OrganizationRegistrationSerializer(serializers.ModelSerializer):
    #is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = OrganizationRegistration
        fields = '__all__'
        read_only_fields = ['registration_date','organization','registration_location']

class OrganizationSerializer(serializers.ModelSerializer):
    registration = OrganizationRegistrationSerializer(read_only=True)

    class Meta:
        model = Organization
        fields = "__all__"
    
    @transaction.atomic
    def create(self, validated_data):
        request = self.context['request']
        # Create Organization
        organization = Organization.objects.create(**validated_data)
        
        ip = request.META.get('REMOTE_ADDR')

        #create OrganizationRegistration
        OrganizationRegistration.objects.create(
            organization=organization,
            registration_location=ip,
            #is_active=True
        )
        
        return organization