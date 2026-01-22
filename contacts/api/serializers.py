from rest_framework import serializers
from contacts.models import Contact
from rest_framework.validators import UniqueValidator
from organizations.models import Organization

class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    phone_number = serializers.CharField() 

    class Meta:
        model = Contact
        fields = ['id', 'email', 'phone_number']
        extra_kwargs = { "email": {"validators": []}, "phone_number": {"validators": []},  }

    def validate_email(self, value): 
        contact = self.instance 
        qs = Contact.objects.filter(email=value)
        if contact:
            qs = qs.exclude(pk=contact.pk)
            if contact.email == value: 
                return value 
        if qs.exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso.") 
        return value
    
    def validate_phone_number(self, value): 
        contact = self.instance 
        qs = Contact.objects.filter(phone_number=value)
        if contact:
            qs = qs.exclude(pk=contact.pk)
            if contact.phone_number == value:
                return value 
        if qs.exists():
            raise serializers.ValidationError("Este número de teléfono ya está en uso.") 
        return value