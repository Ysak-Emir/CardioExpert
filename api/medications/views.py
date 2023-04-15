from rest_framework import generics, filters, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.medications.models import Medication
from api.medications.serializers import MedicationSerializer


class MedicationCreateAPIVIew(generics.CreateAPIView):
    """
    Создание препарата
    """
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permissions_classes = (permissions.IsAuthenticated,)


class MedicationListAPIView(generics.ListAPIView):
    """
    Для получения списка лекарств с возможностью поиска.
    """
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('dosege', 'title',)
