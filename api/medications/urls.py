from django.urls import path, include
from api.medications import views

urlpatterns = [
    path('', views.MedicationListAPIView.as_view()),
    path('add/', views.MedicationCreateAPIVIew.as_view()),
    path('<int:pk>/delete/', views.DeleteMedicationAPIView.as_view()),
    path('delete/', views.DeleteMedicationByNameAPIView.as_view()),
]