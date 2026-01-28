from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework import serializers

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        # Get groups of the authenticated user
        groups = user.groups.all()
        group_names = [group.name for group in groups]

        data['user'] = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'second_last_name': user.second_last_name,
            'groups': group_names
        }

        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    
    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])
        user_id = refresh['user_id']
        user = User.objects.get(id=user_id)

        data = super().validate(attrs)
        # Get groups of the authenticated user
        groups = user.groups.all()
        group_names = [group.name for group in groups]

        data['user'] = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'second_last_name': user.second_last_name,
            'groups': group_names
        }

        return data


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField( 
        many=True, 
        queryset=Group.objects.all(),
        required=True,
    ) 

    class Meta: 
        model = User 
        fields = ['id', 'rfc', 'curp', 'first_name', 'last_name', 'second_last_name', 'username', 'email', 'password', 'groups']
        extra_kwargs = { 
            'password': {'write_only': True} 
        }
    
    def validate_groups(self, value): 
        if not value: 
            raise serializers.ValidationError("Debes asignar al menos un grupo al usuario.") 
        return value


    def create(self, validated_data): 
        groups_data = validated_data.pop('groups') 
        password = validated_data.pop('password')
        # Create the user
        user = User.objects.create(**validated_data) 
        user.set_password(password)
        user.save()
        # Assign groups to the user
        user.groups.set(groups_data)

        return user
    
    def update(self, instance, validated_data): 
        # Update groups if they were sent in the request
        if 'groups' in validated_data:
            groups_data = validated_data.pop('groups')
            instance.groups.set(groups_data)

        # Update the password if it was sent in the request
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        # Update the other fields
        return super().update(instance, validated_data)