from rest_framework import generics, filters, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.medications.models import Medication
from api.medications.serializers import MedicationSerializer


class MedicationCreateAPIVIew(generics.CreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permissions_classes = (permissions.IsAuthenticated,)


class MedicationListAPIView(generics.ListAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'dosege', ]
    permission_classes = (permissions.IsAuthenticated,)
