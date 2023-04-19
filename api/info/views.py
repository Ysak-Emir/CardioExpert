from rest_framework import generics, permissions

from api.info.models import CategoryInformation, SubcategoryInformation
from api.info.serializers import CategorySerializer, SubcategorySerializer


class CategoryInformationListAPIView(generics.ListAPIView):
    queryset = CategoryInformation.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)


class SubcategoryInformationListAPIView(generics.ListAPIView):
    queryset = SubcategoryInformation.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = (permissions.AllowAny,)
