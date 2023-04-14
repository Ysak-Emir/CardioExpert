from django.db import models


class Medication(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    dosage = models.IntegerField(max_length=1000, null=False, blank=False)
    time = models.TimeField()


