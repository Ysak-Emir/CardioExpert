from django.contrib import admin
from api.medications.models import *

class TimeDataMedication(admin.ModelAdmin):
    list_display = ("id", "time", "count")
    list_display_links = ("time",)


class MedicationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "dosage", "start_date", "end_date")
    list_display_links = ("id", "title")
    search_fields = ("title", "dosage", )
    list_per_page = 12


admin.site.register(Medication, MedicationAdmin)
admin.site.register(TimeData, TimeDataMedication)