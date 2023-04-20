from django.db import models


class TimeData(models.Model):
    time = models.TimeField(verbose_name="Время")
    count = models.IntegerField(default=0, verbose_name="Количество")

    class Meta:
        verbose_name = "Время препарата"
        verbose_name_plural = "Время препаратов"

    def __str__(self):
        return str(self.time)


class Medication(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    dosage = models.IntegerField(null=False, blank=False, verbose_name='Дозировка')
    start_date = models.DateField(verbose_name="Период приема от:")
    end_date = models.DateField(verbose_name="Период приема до:")
    time_data = models.ManyToManyField(TimeData, blank=True)

    class Meta:
        verbose_name = "Препарат"
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return self.title

    @classmethod
    def create_time_data_fields(cls, count):
        for i in range(count):
            field_name = f"time_data_{i}"
            field = models.ForeignKey(TimeData, null=True, blank=True, on_delete=models.CASCADE)
            cls.add_to_class(field_name, field)
