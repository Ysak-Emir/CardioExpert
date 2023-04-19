from rest_framework import serializers


class BMIInputSerializer(serializers.Serializer):
    weight = serializers.FloatField()
    height = serializers.FloatField()


class BloodPressureInputSerializer(serializers.Serializer):
    systolic = serializers.IntegerField()
    diastolic = serializers.IntegerField()


class PulseInputSerializer(serializers.Serializer):
    pulse = serializers.IntegerField()
    cycle_duration = serializers.DecimalField(max_digits=5, decimal_places=2)


class FluidInputSerializer(serializers.Serializer):
    fluid_intake = serializers.DecimalField(max_digits=6, decimal_places=2)
    fluid_output = serializers.DecimalField(max_digits=6, decimal_places=2)


class MNOControlSerializer(serializers.Serializer):
    mno = serializers.FloatField(min_value=0.1, max_value=10.0)


class LipidSerializer(serializers.Serializer):
    cholesterol = serializers.FloatField()
    ldl = serializers.FloatField()
    hdl = serializers.FloatField()
    triglycerides = serializers.FloatField()


