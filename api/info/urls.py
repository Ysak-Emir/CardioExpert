from django.urls import path, include
from api.info import views

urlpatterns = [
    path('category_info/', views.CategoryInformationListAPIView.as_view()),
    path('subcategory_info/', views.SubcategoryInformationListAPIView.as_view()),

]