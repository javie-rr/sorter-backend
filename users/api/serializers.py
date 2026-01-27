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

        data['user'] = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'second_last_name': user.second_last_name,
        }

        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    
    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])
        user_id = refresh['user_id']
        user = User.objects.get(id=user_id)

        data = super().validate(attrs)

        data['user'] = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'second_last_name': user.second_last_name,
        }

        return data


class UserSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField( 
        queryset=Group.objects.all(), 
        write_only=True
    )

    rol = serializers.SerializerMethodField(read_only=True)

    class Meta: 
        model = User 
        fields = ['id', 'rfc', 'curp', 'first_name', 'last_name', 'second_last_name', 'username', 'email', 'password', 'group', 'rol']
        extra_kwargs = { 
            'password': {'write_only': True} 
        }

    def get_rol(self, obj): 
        return obj.groups.first().name if obj.groups.exists() else None
    
    def create(self, validated_data): 
        group = validated_data.pop('group', None) 
        password = validated_data.pop('password', None)
        user = User(**validated_data) 
        if password: 
            user.set_password(password) 
            user.save()
        if group: 
            user.groups.clear() 
            user.groups.add(group) 
        return user
    
    def update(self, instance, validated_data): 
        group = validated_data.pop('group', None) 
        password = validated_data.pop('password', None) 
        if password: 
            instance.set_password(password) 
        if group: 
            instance.groups.clear() 
            instance.groups.add(group) 
        
        return super().update(instance, validated_data)