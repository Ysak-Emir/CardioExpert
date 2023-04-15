from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.users import views
from api.users.views import UserLoginAPIView

urlpatterns = [
    path('login_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login_token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login_token2/', UserLoginAPIView.as_view()),
    path('register/', views.RegisterUserAPIView.as_view()),

]