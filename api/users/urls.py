from django.urls import path, include
from api.users import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('register/', views.RegisterUserView.as_view()),

]