from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        data['user'] = {
            'id': user.id,
            'username': user.username,
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
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

        return data