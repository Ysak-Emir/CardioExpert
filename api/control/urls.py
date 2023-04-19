from django.urls import path, include
from api.control import views

urlpatterns = [
    path('bmi/', views.BMICalculator.as_view()),
    path('bp/', views.BloodPressureCalculator.as_view()),
    path('pulse/', views.PulseCalculator.as_view()),
    path('fluid/', views.FluidCalculator.as_view()),
    path('mno/', views.MnoControlView.as_view()),
    path('lipid/', views.LipidProfileView.as_view()),


]