from rest_framework import serializers

from api.control.models import BMI, BloodPressure, Pulse, Fluid, MNO, LipidProfile


class BMIInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMI
        fields = '__all__'


class BloodPressureInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPressure
        fields = '__all__'


class PulseInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pulse
        fields = '__all__'


class FluidInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fluid
        fields = '__all__'


class MNOControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = MNO
        fields = '__all__'


class LipidSerializer(serializers.ModelSerializer):
    class Meta:
        model = LipidProfile
        fields = '__all__'



