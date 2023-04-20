import datetime

from rest_framework import serializers
from api.medications.models import Medication


class MedicationSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=True)
    class Meta:
        model = Medication
        fields = "id title dosage start_date end_date time".split()

    def create(self, validated_data):
        num_hours = validated_data.pop('num_hours')
        validated_data['end_time'] = validated_data['start_time'] + datetime.timedelta(hours=num_hours)
        return Medication.objects.create(**validated_data)

    def update(self, instance, validated_data):
        num_hours = validated_data.pop('num_hours', None)
        if num_hours:
            validated_data['end_time'] = validated_data['start_time'] + datetime.timedelta(hours=num_hours)
        return super().update(instance, validated_data)

class MedicationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ("title", )





