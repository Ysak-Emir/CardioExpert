from django.db import models


class SelfControlDiary(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

