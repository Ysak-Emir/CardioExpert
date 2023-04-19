from rest_framework import serializers
from api.medications.models import Medication


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "id title dosage time".split()


class MedicationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ("title", )
