from django.urls import path, include
from api.medications import views

urlpatterns = [
    path('', views.MedicationListAPIView.as_view()),
    path('add/', views.MedicationCreateAPIVIew.as_view()),

]