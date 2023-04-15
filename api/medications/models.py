from django.db import models


class Medication(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    dosage = models.IntegerField(max_length=1000, null=False, blank=False, verbose_name='Дозировка')
    time = models.TimeField(verbose_name='Время')

    class Meta:
        verbose_name = "Препарат"
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return self.title


