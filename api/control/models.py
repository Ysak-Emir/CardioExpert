from django.db import models

class BMI(models.Model):
    weight = models.FloatField(blank=False, null=False, verbose_name='Вес')
    height = models.FloatField(blank=False, null=False, verbose_name='Рост')


class BloodPressure(models.Model):
    systolic = models.IntegerField(blank=False, null=False, verbose_name='Систолический')
    diastolic = models.IntegerField(blank=False, null=False, verbose_name='Диастолический')
    
    
class Pulse(models.Model):
    pulse = models.IntegerField(blank=False, null=False, verbose_name='Пульс')
    cycle_duration = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цикл")


class Fluid(models.Model):
    fluid_intake = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, verbose_name="Выпито")
    fluid_output = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, verbose_name="Выделено")
    start_time = models.DateTimeField(auto_now_add=True, verbose_name="Период от:", blank=True)
    end_time = models.DateTimeField(verbose_name="Период до:", blank=True)


class MNO(models.Model):
    mno = models.FloatField(verbose_name="МНО")


class LipidProfile(models.Model):
    cholesterol = models.FloatField(blank=False, null=False, verbose_name="Холестерин")
    ldl = models.FloatField(blank=False, null=False, verbose_name="ЛПНП")
    hdl = models.FloatField(blank=False, null=False, verbose_name="ЛПВП")
    triglycerides = models.FloatField(blank=False, null=False, verbose_name="Триглицериды")