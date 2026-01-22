from rest_framework import serializers
from organizations.models import Organization, OrganizationRegistration
from django.db import transaction
from contacts.api.serializers import ContactSerializer
from contacts.models import Contact

class OrganizationRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationRegistration
        fields = "__all__"
        read_only_fields = ['registration_date','organization','registration_location']


class OrganizationSerializer(serializers.ModelSerializer):
    registration = OrganizationRegistrationSerializer(read_only=True)
    contact = ContactSerializer()

    class Meta:
        model = Organization
        fields = ['id', 'rfc', 'legal_name', 'capital_regime', 'trade_name', 'organization_type', 'registration', 'contact']

    @transaction.atomic
    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        # Create contact
        contact = Contact.objects.create(**contact_data)

        # Create Organization
        organization = Organization.objects.create(
            contact = contact,
            **validated_data
        )
        
        request = self.context['request']
        ip = request.META.get('REMOTE_ADDR')
        # Create OrganizationRegistration
        OrganizationRegistration.objects.create(
            organization=organization,
            registration_location=ip,
        )

        return organization

    @transaction.atomic
    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact', None)

        # Update Organization
        instance.rfc = validated_data.get('rfc', instance.rfc)
        instance.legal_name = validated_data.get('legal_name', instance.legal_name)
        instance.capital_regime= validated_data.get('capital_regime', instance.capital_regime)
        instance.trade_name = validated_data.get('trade_name', instance.trade_name)
        instance.save()

        # Update Contact
        if contact_data:
            contact = instance.contact
            if contact:
                contact_serializer = ContactSerializer(contact, data=contact_data, partial=True)
                contact_serializer.is_valid(raise_exception=True)
                contact_serializer.save()
           
        return instance