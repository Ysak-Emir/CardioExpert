from django.urls import path, include
from api.info import views

urlpatterns = [
    path('category/', views.CategoryInformationListAPIView.as_view()),
    path('subcategory/', views.SubcategoryInformationListAPIView.as_view()),
]