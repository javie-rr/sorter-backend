from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView
from users.api.views import CustomTokenObtainPairView, CustomTokenRefreshView, LogoutView
from rest_framework.routers import DefaultRouter 
from users.api.views import UserViewSet

router_users = DefaultRouter(trailing_slash=False) 
router_users.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('auth/login', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('', include(router_users.urls)),
]