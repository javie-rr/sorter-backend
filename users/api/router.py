from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from users.api.views import CustomTokenObtainPairView, CustomTokenRefreshView, LogoutView

urlpatterns = [
    path('auth/login', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
]