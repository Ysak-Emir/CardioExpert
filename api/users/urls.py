from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.users import views
from api.users.views import UserLoginAPIView, LogoutAPIView, PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('login_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login_token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login_token2/', UserLoginAPIView.as_view()),
    path('register/', views.RegisterUserAPIView.as_view(), name='register'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/<int:user_id>/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]

